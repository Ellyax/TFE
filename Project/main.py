import pygame
import os
import sys
import MapMaker
import EnemySprites
import TowerSprites

from Builder import *

pygame.mixer.init()

def main():
    pygame.init()

    ### Handling all the sounds
    pygame.mixer.stop()
    background_sound = pygame.mixer.Sound(os.path.join('Sounds', 'collision.ogg'))
    background_sound.set_volume(10)
    background_sound.play(-1)

    shot_sound = pygame.mixer.Sound(os.path.join('Sounds', 'gun.ogg'))
    shot_sound.set_volume(5)

    ### Menu


    ### Map

