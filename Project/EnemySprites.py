import pygame
import os
import sys
from Builder import *

class EasyEnemy(pygame.sprite.Sprite):
    def __init__(self, wave, turnPoints, mode):
        pygame.sprite.Sprite.__init__(self)
        enemyList.append(self)
        enemy.add(self)
        player.enemy_count +=1

        self.goldkill = 5
        self.points = 100
        self.speed = 4
        self.health = wave*5 + 10

        self.wait = 3
        self.node = 1
        self._S, self._E,self._0, self._1, self._2, self._3, self._4, self._5, self._6, self._7, self._8, self._9 = turnPoints

        self.loadImages()
        self.frame = 0
        self.delay = 2
        self.pause = 0

        self.image = self.imgList[0]
        self.rect = self.image.get_rect()

        self.rect.centerx = self._S
        self.rect.centery = self._S
        self.node_x = self._0
        self.node_y = self._0
        self.result = {0: self._S, 1: self._0, 2: self._1, 3: self._2, 4: self._3, 5: self._4, 6: self._5, 7: self._6, 8: self._7, 9: self._8,10: self._9, 11: self._E}


