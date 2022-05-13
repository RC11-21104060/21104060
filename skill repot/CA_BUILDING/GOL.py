import pygame, sys, csv
import random
import copy
from Cells import *
from Functions import *
# os.chdir(sys.path[0])
# sys.path.append('./bvSimFiles/') # Add location of local packages to path

# Define Game parameters
# screen size
screen_width = 1000
screen_height = 1000

gridX = 59
gridY = 59

# make directory for storing
# saveDir = 'Data/LM-' + simID
# if not os.path.exists(saveDir):
#     os.makedirs(saveDir)
#
# # write file headers for the new file
# epochStats = open(saveDir + '/epochStats.csv', "w")
# epochStats.write('solornonsseal,lamierjaune,AlgerianIris,solidagovir,lierregri ,sureaurou,Nerprunal,Pruneliers,TamarisdeFrance,TamarisAfrique ,Sureaunoir,SumacdeVirginie,Largeleaved,Europeanash,Sycamoremaple,Beechs,Sessileoak,Pedunculateoak,Redoak,empty\n')
# epochStats.close()

# initialise the game window
pygame.init()
pygame.display.set_caption('GOL')

# set the game surface
screen = pygame.display.set_mode((screen_width, screen_height))

# a clock to keep track of the game progress
clock = pygame.time.Clock()

# Any commands that draw the initial state of the game
screen.fill(pygame.Color('White'))

# Update before the first frame
pygame.display.update()

# Any objects you might need/use
currentState = []
nextState = []
for i in range(gridX):
    row = []
    rowNS = []
    for j in range(gridY):
        r = pygame.Rect(i * (screen_width/gridX), j * (screen_height/gridY),
                        (screen_width/gridX)-1, (screen_height/gridY)-1)
        c = Cell('dead', r, (i,j))
        row.append(c)
        rowNS.append(None)
    currentState.append(row)
    nextState.append(rowNS)

read('state000000.csv', currentState)
#read_Fertility('fertility_state.csv', currentState)

# The game loop, in here the behaviour of the game is defined.
# This loop is executed every frame.

counter = 0
while True:
    # Get key events to check if something is going on through some form of input.
    write(currentState, counter)
    # print("currentState object type: ",type(currentState))
    # print("currentState: ",currentState)

    events = pygame.event.get()
    for event in events:
        # Check exit through x button window
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(pygame.Color('White'))

    for row in currentState:
        # print("current sate row: ",row)
        for c in row:
            # print("current sate c: ",c)
            next = get_next_state(c.location, currentState)
            # print("current sate c.location: ",c.location)
            # print("next: ",next)
            nextState[c.x][c.y] = next
            # print(f"nextState cordinates: {c.x,c.y}")

    # define any drawings
    for row in currentState:
        for c in row:
            next = nextState[c.x][c.y]
            c.changeType(next)
            pygame.draw.rect(screen, c.colour, c.rect)
    # print("nextState object type: ",type(nextState))
    # print("nextState: ",nextState)

    # At the end of the loop update the screen and game time.
    pygame.display.update()
    # write(nextState, counter)
    #
    counter += 1
    pygame.time.wait(500)
    clock.tick()

# yList = ['firstExt']
# #xList = ['wolfEn',
# #          'wolfRe',
# #          'wolfFa',
# #          'rabbitEn',
# #          'rabbitRe',
# #          'rabbitFa',
# #          'wolfNum',
# #          'rabbitNum',
# #          'grassNum',
# #          'debrisNum']
# xList = ['SubmergedEnergy',
#           'SubmergedSprawl',
#           'SubmergedConsumption',
#           'floatingEnergy',
#           'floatingSprawl',
#           'floatingConsumption',
#           'aquaticEnergy',
#           'aquaticSprawl',
#           'aquaticConsumption',
#           'herbEnergy',
#           'herbSprawl',
#           'herbConsumption',
#           'woodyEnergy',
#           'woodySprawl',
#           'woodyConsumption',
#           'SubmergedNum',
#           'floatingNum',
#           'aquaticNum',
#           'herbNum',
#           'woodyNum',
#           'waterNum',
#           'debrisNum']
