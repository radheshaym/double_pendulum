#Name : Radhesham Nemade
#Subject : Double Pendulum System

import pygame
import os
import math
import random
from points import points
import formulae

os.environ["SDL_VIDEO_CENTERED"] = '1'

width, height = 1396, 1080
SIZE = (width, height)
pygame.init()
pygame.display.set_caption("Double Pendulum")
fps = 40
screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

white = (255, 255, 255)
black = (0, 0, 0)

Violet1 = (125, 0, 255)
Violet2 = (150, 0, 255)
Violet3 = (175, 0, 255)
Violet4 = (200, 0, 255)
Violet5 = (225, 0, 255)
Violet6 = (250, 0, 255)

Mag1 = (255, 0, 250)
Mag2 = (255, 0, 225)
Mag3 = (255, 0, 200)
Mag4 = (255, 0, 175)
Mag5 = (255, 0, 150)
Mag6 = (255, 0, 125)

Rasp1 = (255, 0, 120)
Rasp2 = (255, 0, 100)
Rasp3 = (255, 0, 75)
Rasp4 = (255, 0, 50)
Rasp5 = (255, 0, 25)
Rasp6 = (255, 0, 5)

Blue1 = (0, 0, 255)
Blue2 = (25, 0, 255)
Blue3 = (50, 0, 255)
Blue4 = (75, 0, 255)
Blue5 = (100, 0, 255)
Blue6 = (120, 0, 255)
 

Ocean1 = (0, 120, 255)
Ocean2 = (0, 100, 255)
Ocean3 = (0, 75, 255)
Ocean4 = (0, 50, 255)
Ocean5 = (0, 25, 255)
Ocean6 = (0, 5, 255)


Cyan1 = (0, 255, 255)
Cyan2 = (0, 225, 255)
Cyan3 = (0, 200, 255)
Cyan4 = (0, 175, 255)
Cyan5 = (0, 150, 255)
Cyan6 = (0, 125, 255)


Turq1 = (0, 255, 125)
Turq2 = (0, 255, 150)
Turq3 = (0, 255, 175)
Turq4 = (0, 255, 200)
Turq5 = (0, 255, 225)
Turq6 = (0, 255, 250)


Green1 = (0, 255, 0)
Green2 = (0, 255, 25)
Green3 = (0, 255, 50)
Green4 = (0, 255, 75)
Green5 = (0, 255, 100)
Green6 = (0, 255, 120)


Sgreen1 = (120, 255, 0)
Sgreen2 = (100, 255, 0)
Sgreen3 = (75, 255, 0)
Sgreen4 = (50, 255, 0)
Sgreen5 = (25, 255, 0)
Sgreen6 = (5, 255, 0)

Yellow1 = (255, 255, 0)
Yellow2 = (225, 255, 0)
Yellow3 = (200, 255, 0)
Yellow4 = (175, 255, 0)
Yellow5 = (150, 255, 0)
Yellow6 = (125, 255, 0)

Orange1 = (255, 125, 0)
Orange2 = (255, 150, 0)
Orange3 = (255, 175, 0)
Orange4 = (255, 200, 0)
Orange5 = (255, 225, 0)
Orange6 = (255, 250, 0)

Red1 = (255, 0, 0)
Red2 = (255, 25, 0)
Red3 = (255, 50, 0)
Red4 = (255, 75, 0)
Red5 = (255, 100, 0)
Red6 = (255, 120, 0)

a = [Violet6, Violet5, Violet4, Violet3, Violet2, Violet1,
    Blue6, Blue5, Blue4, Blue3, Blue2, Blue1,
    Ocean6, Ocean5, Ocean4, Ocean3, Ocean2, Ocean1,
    Cyan6, Cyan5, Cyan4, Cyan3, Cyan2, Cyan1,
    Turq6, Turq5, Turq4, Turq3, Turq2, Turq1,
    Green6, Green5, Green4, Green3, Green2, Green1,
    Sgreen6, Sgreen5, Sgreen4, Sgreen3, Sgreen2, Sgreen1,
    Yellow6, Yellow5, Yellow4, Yellow3, Yellow2, Yellow1,
    Orange6, Orange5, Orange4, Orange3, Orange2, Orange1,
    Red6, Red5, Red4, Red3, Red2, Red1,
    Rasp6, Rasp5, Rasp4, Rasp3, Rasp2, Rasp1,
    Mag6, Mag5, Mag4, Mag3, Mag2, Mag1
     ]

mass1 = 10
mass2 = 10
length1 = 150
length2 = 150

angle_velocity1 = [0]*72
angle_velocity2 = [0]*72
angle_acc1 = [0] * 72
angle_acc2 = [0] * 72
angle1 = [math.pi*15/16] * 72
angle2 = [math.pi*15/16] * 72
gravity = 0.1
j = 999999
for i in range(72):
    angle1[i] *= j * 0.000001
    angle2[i] *= j * 0.000001
    j-=1



starting_point = (int(width / 2), int(height / 2))
x1 = [0] * 72
y1 = [0] * 72
x2 = [0] * 72
y2 = [0] * 72
x_offset = starting_point[0]
y_offset = starting_point[1]

running = True

while running:
    clock.tick(fps)
    screen.fill(black)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    for i in range(72): 
        angle_acc1[i] = formulae.firstaccn(angle1[i],angle2[i],mass1,mass2,length1,length2,gravity,angle_velocity1[i],angle_velocity2[i])
        angle_acc2[i] = formulae.secondaccn(angle1[i], angle2[i], mass1, mass2, length1, length2, gravity, angle_velocity1[i], angle_velocity2[i])
    
        x1[i] = float(length1 * math.sin(angle1[i]) + x_offset)
        y1[i] = float(length1 * math.cos(angle1[i]) + y_offset)

        x2[i] = float(x1[i] + length2 * math.sin(angle2[i]))
        y2[i] = float(y1[i] + length2 * math.cos(angle2[i]))
    
        angle_velocity1[i] += angle_acc1[i]
        angle_velocity2[i] += angle_acc2[i]

        angle1[i] += angle_velocity1[i]
        angle2[i] += angle_velocity2[i]
 
        pygame.draw.line(screen, a[i], starting_point, (x1[i], y1[i]), 1)
        pygame.draw.line(screen, a[i], (x1[i], y1[i]), (x2[i], y2[i]), 1)
        pygame.draw.circle(screen,a[i], (int(x2[i]), int(y2[i])), 0)
        pygame.draw.circle(screen,a[i], (int(x1[i]), int(y1[i])), 0)
    
    
        



    pygame.display.update()
pygame.quit()
