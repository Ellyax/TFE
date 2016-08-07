import pygame
import os
import sys
from Builder import *

class Tower(pygame.sprite.Sprite):
    def __init__(self, xy, type):
        pygame.sprite.Sprite.__init__(self)
        towerList.append(self)
        x = xy
        y = xy
        self.level = 1
        self.tilesList = None
        self.loadTiles()
        self.type = type

        if self.type == 1:
            self.tile = self.tilesList[0]
            self.BASED_DMG = 5
            self.dmg = self.BASED_DMG
            self.cost = 50
            self.range = 100
            self.reload = 15
            self.reloadNum = 0
            self.upgrade_cost = 100

        elif self.type == 2:
            self.tile = self.tilesList[1]
            self.BASED_DMG = 15
            self.dmg = self.BASED_DMG
            self.cost = 60
            self.range = 100
            self.reload = 25
            self.reloadNum = 0
            self.upgrade_cost = 120

        elif self.type == 3:
            self.tile = self.tilesList[2]
            self.BASED_DMG = 5
            self.dmg = self.BASED_DMG
            self.cost = 75
            self.range = 300
            self.reload = 10
            self.reloadNum = 0
            self.upgrade_cost = 150

        elif self.type == 4:
            self.tile = self.tilesList[3]
            self.BASED_DMG = 70
            self.dmg = self.BASED_DMG
            self.cost = 100
            self.range = 100
            self.reload = 100
            self.reloadNum = 0
            self.upgrade_cost = 200

        self.rect = self.tile.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.surf_x = self.rect.center
        self.surf_y = self.rect.center
        self.surf_x -= 100
        self.surf_y -= 100

    def update(self):
        i = 1

    def loadTiles(self):
        img = pygame.image.load(os.path.join('Images', 'tower.png'))
        self.tilesList = []
        tileSize = (25, 25)
        offset = ((0, 0), (25, 0), (0, 25), (25,25))

        for i in range(4):
            temp_tile = pygame.Surface(tileSize)
            temp_tile.blit(img, (0,0), (offset[i], tileSize))
            self.tilesList.append(temp_tile)

    def target(self):
