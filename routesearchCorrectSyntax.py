import random
import csv
from climberInputs import *

govind = []
height = climberInputs.height
legLength = climberInputs.legLength
LeftFoot = (0, 0)
RightFoot = (0, 0)
LeftHand = (0,0)
RightHand = (0,0)

def csv_dict_writer(path, fieldnames, data):
    with open(path, "wb") as out_file:
        writer = csv.DictWriter(out_file,delimiter=',', fieldnames=fieldnames)
        for row in data:
            writer.writerow(row)

def get_reach():
    reach = 1.5*height
    return reach

def distance(x, y):
    xValue = y[0]-x[0]
    yValue = y[1]-x[1]
    distance = ((xValue**2)+(yValue**2))**0.5
    return distance

def BestHand(limb,hand, reach,holds2): 
    #work out the distance between the current limb and all possible holds, 
    #the distance which is just under the reach is the closest 
    if hand != None: 
        BestPointOverall = hand+tuple()
    else:
        BestPointOverall= (0,0)
    pop = -1
    #print(len(holds))
    for x in range (0, len(holds2)):
        Distance = distance(limb, holds2[x])
        #if reach >= 1500:
        if Distance <= reach:
            BestPointCurrent = holds2[x]+tuple()
            #print("reachable")
            if (BestPointCurrent[1] >= BestPointOverall[1]):
                BestPointOverall = BestPointCurrent+tuple()
                pop = x
    if pop != -1:
        BestPointOverall = holds2.pop(pop)
        return BestPointOverall+tuple(),holds2
    else:
        #print("")
        return hand,holds2
    #else:
     #   print("DYNO MODE " + str(reach))
      #  return BestHand(limb, (reach+100))

def BestFoot (limb,holds):
    BestPointOverall = limb
    newLimb = (limb[0],limb[1]+legLength)
    pop = -1
    for x in range (0, len(holds)):
        Distance = distance(limb, holds[x])
        #print(str(Distance)+ " " + str(legLength))
        if Distance <= legLength:
            BestPointCurrent = holds[x]
            if limb == LeftFoot:
                if (BestPointCurrent[1] >= BestPointOverall[1]) and newLimb[0]<=BestPointCurrent[0] and newLimb[1]>=BestPointCurrent[1]:
                    BestPointOverall = BestPointCurrent
                    pop = x
            else:
                if (BestPointCurrent[1] >= BestPointOverall[1]) and newLimb[0]>=BestPointCurrent[0] and newLimb[1]>=BestPointCurrent[1]:
                    BestPointOverall = BestPointCurrent
                    pop = x
    if pop == -1:
        BestPointOverall = limb
    else:
        BestPointOverall = holds.pop(pop)
    return BestPointOverall+tuple(),holds
        
def getHolds(holdsAmount):
    holds = []
    for i in range(0,holdsAmount):
        holdX = (random.randint(0, 100))*10
        holdY = (random.randint(0, 100))*10
        holds.append((holdX,holdY))
    return holds    

def highestHold(holds):
    length = len(holds)-1
    for x in range (0, length):
        if (holds[x][1] == holds[x+1][1]):
            if (holds[x][0] <= holds[x+1][0]):
                temporary = holds[x]
                holds[x] = holds[x+1]
                holds[x+1] = temporary        
        elif (holds[x][1] > holds[x+1][1]):
            temporary = holds[x]
            holds[x] = holds[x+1]
            holds[x+1] = temporary
    highest = holds[length]
    return highest   

reach = get_reach()
"""BestHand(LeftFoot) gives the best right hand
BestHand(RightFoot) gives the best left hand
BestFoot(LeftFoot) gives the best left foot
BestFoot(RightFoot) gives the best right foot"""

holds = getHolds(200)
#holds = [(130, 480), (320, 30), (510, 180), (630, 220), (250, 690), (720, 260), (900, 590), (190, 570), (120, 160), (800, 270), (1000, 280), (10, 640), (380, 800), (400, 300), (330, 730), (470, 680), (810, 760), (280, 170), (800, 760), (330, 20), (110, 210), (960, 370), (270, 380), (990, 650), (290, 230), (210, 40), (360, 110), (860, 130), (570, 630), (800, 880), (590, 620), (130, 680), (670, 230), (850, 730), (360, 300), (510, 880), (990, 240), (120, 230), (620, 540), (440, 150), (490, 570), (720, 520), (400, 750), (520, 690), (150, 340), (120, 60), (560, 330), (820, 210), (570, 470), (800, 600), (710, 100), (550, 430), (940, 40), (680, 930), (710, 810), (770, 860), (410, 660), (30, 790), (20, 290), (150, 510), (490, 400), (120, 370), (170, 420), (530, 150), (490, 770), (140, 720), (910, 790), (220, 220), (190, 370), (730, 920), (510, 80), (780, 480), (240, 570), (590, 140), (190, 930), (30, 20), (170, 630), (810, 70), (760, 670), (980, 560), (310, 330), (910, 310), (330, 150), (310, 70), (670, 890), (750, 370), (210, 710), (220, 410), (520, 660), (540, 220), (0, 790), (420, 670), (480, 480), (590, 340), (40, 460), (1000, 720), (980, 600), (360, 400), (650, 660), (480, 430), (700, 170), (630, 780), (10, 330), (430, 120), (40, 530), (650, 570), (310, 780), (510, 480), (520, 770), (190, 230), (410, 800), (470, 40), (830, 60), (370, 520), (90, 340), (140, 310), (900, 420), (170, 680), (340, 10), (830, 940), (930, 640), (650, 950), (320, 910), (400, 260), (40, 600), (660, 360), (980, 200), (560, 420), (700, 300), (960, 410), (310, 560), (50, 20), (390, 60), (320, 410), (570, 290), (230, 460), (590, 360), (30, 950), (750, 610), (870, 50), (230, 920), (290, 300), (370, 840), (630, 890), (500, 780), (860, 660), (900, 860), (490, 20), (480, 370), (260, 490), (680, 50), (270, 970), (820, 460), (50, 360), (890, 860), (720, 670), (230, 920), (590, 40), (120, 190), (40, 840), (730, 270), (1000, 900), (800, 570), (820, 190), (790, 650), (130, 610), (600, 0), (340, 300), (190, 720), (610, 800), (860, 350), (160, 380), (480, 240), (110, 330), (740, 980), (710, 160), (550, 820), (200, 130), (990, 50), (250, 90), (760, 720), (20, 80), (110, 200), (320, 700), (560, 520), (390, 760), (740, 420), (270, 270), (230, 0), (80, 400), (660, 490), (390, 990), (130, 550), (90, 530), (100, 120), (40, 110)]

highest = highestHold(holds)
atTop = False
steps = 0
RightHand = None
rhb = None
lhb = None
rfb = None
lfb = None
while atTop == False:
    if steps == 30:
        print("You're not tall enough")
        break
    if RightHand != None:
        rhb = RightHand+tuple()
        lhb = LeftHand+tuple()
        rfb = RightFoot+tuple()
        lfb = LeftFoot+tuple()
    RightHand,holds = BestHand(LeftFoot,RightHand, reach,holds)
    if (rhb != None) and (RightHand != rhb) and (rhb != (0,0)):
        holds.append(rhb+tuple())

    LeftHand,holds = BestHand(RightFoot,LeftHand, reach,holds)

    if (lhb != None) and (LeftHand != lhb) and (lhb != (0,0)):
        holds.append(lhb+tuple())
    RightFoot,holds = BestFoot(RightFoot,holds)
    if (rfb != None) and (RightFoot != rfb) and (rfb != (0,0)):
        holds.append(rfb+tuple())
    LeftFoot,holds = BestFoot(LeftFoot,holds)
    if (lfb != None) and (LeftFoot != lfb) and (lfb != (0,0)):
        holds.append(lfb+tuple())
    if RightHand == LeftHand:
        print("You are in dangerous land boi")
        print(holds)
        #RightHand = BestHand(LeftFoot, RightHand, reach+50,holds)
    if (RightHand or LeftHand) == highest:
        atTop = True
    steps = steps + 1
        #reach = reach + 20
    govindlol = (LeftFoot, RightFoot, LeftHand, RightHand)
    govind.append(govindlol)
read_list = []
with open('govindread.csv', 'w') as csvfile:
    writefile= csv.writer(csvfile, delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for i in range (0,len(govind)):
        for y in range (0,4):
            writefile.writerow(govind[i][y])
#fieldnames = govind[0]
#for values in fieldnames[1:]:
#    inner_dict = dict(zip(fieldnames, values))
#    read_list.append(inner_dict)
steps = str(steps)
print("Congrats you can reach the top in "+ steps +" number of steps")
print(govind)

#Need to be able to recurse this, get through moves one at a time, foot, foot, hand hand
#But if they are unable to move (same spot is returned), append the last spots and do it again
# Return as a set of positions, but not if there is a state that 