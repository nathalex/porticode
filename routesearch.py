holds = [(200,300), (100,400), (600,200), (400,400), (500, 300), (400,100), (800,300), (700,100), (200,200),
        (200,700), (100,800), (600,600), (400,800), (500, 700), (400,500), (800,700), (700,500), (200,600),
        (200,1100), (100,1200), (600,1000), (400,1200), (500, 1100), (400,900), (800,1100), (700,900), (200,1000),
        (600,800), (100,100), (700,1200)]

LeftFoot = (400,1200)
RightFoot = (0,0)
LeftHand = (0,0)
RightHand = (0,0)
height = 180
legLength = 100

def get_reach():
    reach = 300
    return reach

def distance(x, y):
    xValue = y[0]-x[0]
    yValue = y[1]-x[1]
    distance = (xValue**2+yValue**2)**0.5
    return distance

def BestHand(limb): 
    #work out the distance between the current limb and all possible holds, 
    #the distance which is just under the reach is the closest 
    BestPointOverall = (0,0)
    for x in range (0, len(holds)-1):
        Distance = distance(limb, holds[x])
        if Distance <= reach:
            BestPointCurrent = holds[x]
            if (BestPointCurrent[1] >= BestPointOverall[1]):
                BestPointOverall = BestPointCurrent
    return BestPointOverall

def BestFoot (limb):
    BestPointOverall = (0,0)
    newLimb = (limb[0],limb[1]+legLength)
    for x in range (0, len(holds)-1):
        Distance = distance(limb, holds[x])
        if Distance <= legLength:
            BestPointCurrent = holds[x]
            if limb == LeftFoot:
                if (BestPointCurrent[1] >= BestPointOverall[1]) and newLimb[0]<=BestPointCurrent[0] and newLimb[1]>=BestPointCurrent[1]:
                    BestPointOverall = BestPointCurrent
            else:
                if (BestPointCurrent[1] >= BestPointOverall[1]) and newLimb[0]>=BestPointCurrent[0] and newLimb[1]>=BestPointCurrent[1]:
                    BestPointOverall = BestPointCurrent
    return BestPointOverall
        


reach = get_reach()
#BestHand(LeftFoot) gives the best right hand
#BestHand(RightFoot) gives the best left hand
#BestFoot(LeftFoot) gives the best left foot
#BestFoot(RightFoot) gives the best right foot
print("Your best right hand position is " + str(BestHand(LeftFoot)))
print("Your best left foot position is " + str(BestFoot(LeftFoot)))

