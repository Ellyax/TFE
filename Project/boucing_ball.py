import sys
import pygame
import os

width = 1024
height = 768
size = width, height
speed_1 = [2, 3]
speed_2 = [4, 1.7]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

ball = pygame.image.load("Images/ball.gif")
ball_2 = pygame.image.load("Images/ball1.gif")
ballrect = ball.get_rect()
ballrect_2 = ball_2.get_rect()

pygame.mixer.init()
pygame.mixer.stop()
son = pygame.mixer.Sound(os.path.join('Sounds', 'gun.ogg'))
son_2 = pygame.mixer.Sound("Sounds/collision.ogg")
son_2.set_volume(20)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    ballrect = ballrect.move(speed_1)
    if ballrect.left < 0 or ballrect.right > width:
        speed_1[0] = -speed_1[0]
        son.play()
        #print "poc"
    if ballrect.top < 0 or ballrect.bottom > height:
        speed_1[1] = -speed_1[1]
        son.play()
        #print "poc"

    ballrect_2 = ballrect_2.move(speed_2)
    if ballrect_2.left < 0 or ballrect_2.right > width:
        speed_2[0] = -speed_2[0]
        son_2.play()
        #print "poc_2"
    if ballrect_2.top < 0 or ballrect_2.bottom > height:
        speed_2[1] = -speed_2[1]
        son_2.play()
        #print "poc_2"

    screen.fill(black)
    screen.blit(ball, ballrect)
    screen.blit(ball_2, ballrect_2)
    pygame.display.flip()

