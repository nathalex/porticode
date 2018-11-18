import random

"""holds = [(200,300), (100,400), (600,200), (400,400), (500, 300), (400,100), (800,300), (700,100), (200,200),
        (200,700), (100,800), (600,600), (400,800), (500, 700), (400,500), (800,700), (700,500), (200,600),
        (200,1100), (100,1200), (600,1000), (400,1200), (500, 1100), (400,900), (800,1100), (700,900), (200,1000),
        (600,800), (100,100), (700,1200)]"""

height = 200
legLength = height-20
LeftFoot = (0, 0)
RightFoot = (0, 0)
LeftHand = (0,0)
RightHand = (0,0)

def get_reach():
    reach = height
    return reach

def distance(x, y):
    xValue = y[0]-x[0]
    yValue = y[1]-x[1]
    distance = (xValue**2+yValue**2)**0.5
    return distance

def BestHand(limb, reach): 
    #work out the distance between the current limb and all possible holds, 
    #the distance which is just under the reach is the closest 
    BestPointOverall = (0,0)
    pop = -1
    #print(len(holds))
    for x in range (0, len(holds)):
        Distance = distance(limb, holds[x])
        #if reach >= 1500:
         #   print(str(Distance)+ " " + str(reach))
        if Distance <= reach:
            BestPointCurrent = holds[x]
            #print("reachable")
            if (BestPointCurrent[1] >= BestPointOverall[1]):
                BestPointOverall = BestPointCurrent
                pop = x
    if pop != -1:
        BestPointOverall = holds.pop(pop)
        return BestPointOverall
    #else:
        #print("DYNO MODE " + str(reach))
        #return BestHand(limb, (reach+100))

def BestFoot (limb):
    BestPointOverall = (0,0)
    newLimb = (limb[0],limb[1]+legLength)
    pop = -1
    for x in range (0, len(holds)):
        Distance = distance(limb, holds[x])
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
    return BestPointOverall
        
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

holds = getHolds(500)
highest = highestHold(holds)

atTop = False
print(highest)
steps = 0
while atTop == False:
    RightHand = BestHand(LeftFoot, reach)
    holds.append(RightHand)
    LeftHand = BestHand(RightFoot, reach)
    holds.append(LeftHand)
    RightFoot = BestFoot(RightFoot)
    holds.append(RightFoot)
    LeftFoot = BestFoot(RightFoot)
    holds.append(LeftFoot)
    print(steps, LeftHand)
    print(steps, RightHand)
    if RightHand == LeftHand:
        RightHand = BestHand(LeftFoot, reach+50)
    if (RightHand or LeftHand) == highest:
        atTop = True
    else:
        steps = steps + 1
        #reach = reach + 20
steps = str(steps)
print("Congrats you can reach the top in "+ steps +" number of steps")

#Need to be able to recurse this, get through moves one at a time, foot, foot, hand hand
#But if they are unable to move (same spot is returned), append the last spots and do it again
# Return as a set of positions, but not if there is a state that 