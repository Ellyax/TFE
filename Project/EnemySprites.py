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
        self._S, self._E, self._0, self._1, self._2, self._3, self._4, self._5, self._6, self._7, self._8, self._9 = turnPoints

        self.loadImages()
        self.frame = 0
        self.delay = 2
        self.pause = 0

        self.image = self.imgList[0]
        self.rect = self.image.get_rect()

        self.rect.centerx, self.rect.centery = self._S
        self.node_x, self.node_y = self._0
        self.result = {0: self._S, 1: self._0, 2: self._1, 3: self._2, 4: self._3, 5: self._4, 6: self._5, 7: self._6, 8: self._7, 9: self._8,10: self._9, 11: self._E}
        self.d = 0

        if mode == 'hard':
            self.health *= 2
            self.goldkill *= 1.5

        self.start_health = self.health
        self.distance = 0

    def update(self):
        if self.health <= 0:
            player.score += self.points
            player.gold += self.goldkill
            self.kill()
            enemyList.remove(self)
            player.enemy_count -= 1
        self.animate()
        self.move()

    def move(self):
        if ((self.node_x - self.speed) < (self.rect.centerx) and self.d == 1):
            self.rect.centerx = self.node_x
        if ((self.node_y - self.speed) < (self.rect.centery) and self.d == 2):
            self.rect.centery = self.node_y
        if ((self.node_x + self.speed) > (self.rect.centerx) and self.d == 3):
            self.rect.centerx = self.node_x
        if ((self.node_y + self.speed) > (self.rect.centery) and self.d == 4):
            self.rect.centery = self.node_y

        if self.rect.centerx < self.node_x :
            self.rect.centerx += self.speed
            self.d = 1
        if self.rect.centery <  self.node_y :
            self.rect.centery += self.speed
            self.d = 2
        if self.rect.centerx > self.node_x:
            self.rect.centerx -= self.speed
            self.d = 3
        if self.rect.centery > self.node_y:
            self.rect.centery -= self.speed
            self.d = 4

        if (self.rect.centerx == self.node_x) and (self.rect.centery == self.node_y) :
            if self.node < 11:
                self.node += 1
                self.node_x, self.node_y = self.result[self.node]
            else:
                self.wait -= 1
                if self.wait <= 0:
                    player.health -= 1
                    self.kill()
                    enemyList.remove(self)
                    player.enemy_count -= 1
        self.distance += self.speed

    def loadImages(self):
        img = pygame.image.load(os.path.join ('Images', 'enemy1.png'))
        self.imgList = []
        imgSize = (25, 50)
        offset = ((0, 0), (25, 0), (50, 0), (0, 50), (0, 100), (25, 50), (25, 100), (50, 50), (50, 100))

        for i in range(9):
            temp_img = pygame.Surface(imgSize)
            temp_img.blit(img, (0, 0), (offset[i], imgSize))
            t_color = temp_img.get_at((1,1))
            temp_img.set_colorkey(t_color)
            self.imgList.append(temp_img)

    def animate(self):
        self.pause += 1
        if self.pause >= self.delay:
            self.pause = 0
            self.frame += 1
            if self.frame >= len(self.imgList):
                self.frame = 0
            self.image = self.imgList[self.frame]





class BossEnemy(pygame.sprite.Sprite):
    def __init__(self, wave, turnPoints, mode):
        pygame.sprite.Sprite.__init__(self)
        enemyList.append(self)
        enemy.add(self)
        player.enemy_count +=1

        self.goldkill = 200
        self.points = 10000
        self.speed = 5
        self.health = wave*20 + 1000

        self.wait = 3
        self.node = 1
        self._S, self._E, self._0, self._1, self._2, self._3, self._4, self._5, self._6, self._7, self._8, self._9 = turnPoints

        self.loadImages()
        self.frame = 0
        self.delay = 2
        self.pause = 0

        self.image = self.imgList[0]
        self.rect = self.image.get_rect()

        self.rect.centerx, self.rect.centery = self._S
        self.node_x, self.node_y = self._0
        self.result = {0: self._S, 1: self._0, 2: self._1, 3: self._2, 4: self._3, 5: self._4, 6: self._5, 7: self._6, 8: self._7, 9: self._8,10: self._9, 11: self._E}
        self.d = 0

        if mode == 'hard':
            self.health *= 2
            self.goldkill *= 1.5

        self.start_health = self.health
        self.distance = 0

    def update(self):
        if self.health <= 0:
            player.score += self.points
            player.gold += self.goldkill
            self.kill()
            enemyList.remove(self)
            player.enemy_count -= 1
        self.animate()
        self.move()

    def move(self):
        if ((self.node_x - self.speed) < (self.rect.centerx) and self.d == 1):
            self.rect.centerx = self.node_x
        if ((self.node_y - self.speed) < (self.rect.centery) and self.d == 2):
            self.rect.centery = self.node_y
        if ((self.node_x + self.speed) > (self.rect.centerx) and self.d == 3):
            self.rect.centerx = self.node_x
        if ((self.node_y + self.speed) > (self.rect.centery) and self.d == 4):
            self.rect.centery = self.node_y

        if self.rect.centerx < self.node_x :
            self.rect.centerx += self.speed
            self.d = 1
        if self.rect.centery <  self.node_y :
            self.rect.centery += self.speed
            self.d = 2
        if self.rect.centerx > self.node_x:
            self.rect.centerx -= self.speed
            self.d = 3
        if self.rect.centery > self.node_y:
            self.rect.centery -= self.speed
            self.d = 4

        if (self.rect.centerx == self.node_x) and (self.rect.centery == self.node_y) :
            if self.node < 11:
                self.node += 1
                self.node_x, self.node_y = self.result[self.node]
            else:
                self.wait -= 1
                if self.wait <= 0:
                    player.health -= 1
                    self.kill()
                    enemyList.remove(self)
                    player.enemy_count -= 1
        self.distance += self.speed

    def loadImages(self):
        img = pygame.image.load(os.path.join ('Images', 'enemy2.png'))
        self.imgList = []
        imgSize = (25, 50)
        offset = ((0, 0), (25, 0), (50, 0), (0, 50), (0, 100), (25, 50), (25, 100), (50, 50), (50, 100))

        for i in range(9):
            temp_img = pygame.Surface(imgSize)
            temp_img.blit(img, (0, 0), (offset[i], imgSize))
            t_color = temp_img.get_at((1,1))
            temp_img.set_colorkey(t_color)
            self.imgList.append(temp_img)

    def animate(self):
        self.pause += 1
        if self.pause >= self.delay:
            self.pause = 0
            self.frame += 1
            if self.frame >= len(self.imgList):
                self.frame = 0
            self.image = self.imgList[self.frame]

























