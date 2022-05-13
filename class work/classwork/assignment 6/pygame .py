import pygame
import sys
import random

pygame.init()
screen_width = 600
screen_height = 900

xSel = 0
ySel = 0

ShowCell = False

pygame.display.set_caption('location plan excerpt')
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

screen.fill(pygame.Color('red'))
pygame.draw.rect(screen, (255,255,255), pygame.Rect(100,100,300,200))

backgrImage = pygame.image.load('mapping.jpg')
backgrImage = pygame.transform.scale(backgrImage, (screen_width, screen_height))
screen.blit(backgrImage, [0,0])

pygame.display.update()
clock = pygame.time.Clock()

lineColor = random.radint (0, 255), random.radint (0, 255), random.radint (0, 255)

rectangles = []
for i in range(10):
    row = []
    for j in range(10):
        r = pygame.Rect(i * (screen_width/10), j * (screen_height/7),
                        (screen_width/10), (screen_height/7))
        row.append(r)
    rectangles.append(row)

    while True:
       screen.blit(backgrImage, [0,0])

    events = pygame.event.get()
    for event in events:

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            # Check exit through esc
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_RIGHT:
                if xSel < 9:
                    xSel +=1
            if event.key == pygame.K_LEFT:
                if xSel > 0:
                    xSel -=1
            if event.key == pygame.K_UP:
                if ySel > 0:
                    ySel -= 1
            if event.key == pygame.K_DOWN:
                if ySel < 9:
                    ySel += 1
            if event.key == pygame.K_RETURN:
                if ShowCell:
                    ShowCell = False
                else:
                    ShowCell = True

                    pygame.draw.rect(screen, pygame.Color(100,100,100), rectangles[xSel][ySel])

    if ShowCell:
        try:
            cellImage = pygame.image.load('GridCells/' + str(xSel) + '_' + str(ySel) + '.png')
            imWidth, imHeight = cellImage.get_size()
            dx = screen_width / imWidth
            dy = screen_height / imHeight
            f = min(dx,dy)
            cellImage = pygame.transform.scale(cellImage, (int(f * imWidth), int(f * imHeight)))
            screen.blit(cellImage, [0,0])
        except FileNotFoundError:
            ShowCell = False

    pygame.display.update()
    clock.tick()