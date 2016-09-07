import pygame
import os
import sys
from Builder import *

class Tower(pygame.sprite.Sprite):
    def __init__(self, xy, type):
        pygame.sprite.Sprite.__init__(self)
        towerList.append(self)
        x, y = xy
        self.lvl = 1
        self.tilesList = None
        self.loadTiles()
        self.type = type

        if self.type == 1:
            self.image = self.tilesList[0]
            self.BASED_DMG = 5
            self.dmg = self.BASED_DMG
            self.cost = 50
            self.range = 100
            self.reload = 15
            self.reloadNum = 0
            self.upgrade_cost = 100

        elif self.type == 2:
            self.image = self.tilesList[1]
            self.BASED_DMG = 15
            self.dmg = self.BASED_DMG
            self.cost = 60
            self.range = 100
            self.reload = 25
            self.reloadNum = 0
            self.upgrade_cost = 120

        elif self.type == 3:
            self.image = self.tilesList[2]
            self.BASED_DMG = 5
            self.dmg = self.BASED_DMG
            self.cost = 75
            self.range = 300
            self.reload = 10
            self.reloadNum = 0
            self.upgrade_cost = 150

        elif self.type == 4:
            self.image = self.tilesList[3]
            self.BASED_DMG = 70
            self.dmg = self.BASED_DMG
            self.cost = 100
            self.range = 100
            self.reload = 100
            self.reloadNum = 0
            self.upgrade_cost = 200

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.surf_x, self.surf_y = self.rect.center
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
        for enemy in enemyList:
            aim_x = enemy.rect.centerx
            aim_y = enemy.rect.bottom-13
            if self.range == 0:
                enemy.health -= self.dmg
                return (aim_x, aim_y)
            elif dist((aim_x, aim_y), self.rect, self.range) == 1:
                enemy.health -= self.dmg
                return (aim_x, aim_y)

    def upgrade(self):
        if self.lvl == 1:
            self.lvl = 2

            if self.type == 1:
                self.dmg = 15
                self.range = 100
                self.reload = 15
                self.upgrade_cost = 200

            elif self.type == 2:
                self.dmg = 35
                self.range = 100
                self.reload = 25
                self.upgrade_cost = 240

            elif self.type == 3:
                self.dmg = 10
                self.range = 400
                self.reload = 10
                self.upgrade_cost = 300

            elif self.type == 4:
                self.dmg = 180
                self.range = 100
                self.reload = 100
                self.upgrade_cost = 400

            return

        if self.lvl == 2:
            if self.type == 1:
                self.dmg = 40
                self.range = 100
                self.reload = 15
                self.upgrade_cost = 0

            elif self.type == 2:
                self.dmg = 80
                self.range = 140
                self.reload = 30
                self.upgrade_cost = 0

            elif self.type == 3:
                self.dmg = 30
                self.range = 600
                self.reload = 10
                self.upgrade_cost = 0

            elif self.type == 4:
                self.dmg = 540
                self.range = 150
                self.reload = 90
                self.upgrade_cost = 40

            return


class TowerSprite(pygame.sprite.Sprite):
    def __init__(self, x, y, type):
        pygame.sprite.Sprite.__init__(self)

        self.tilesList = None
        self.loadTiles()
        self.type = type

        if self.type == 1:
            self.image = self.tilesList[0]
            self.BASED_DMG = 5
            self.cost = 50
            self.range = 100
            self.speed = 'average'

        if self.type == 2:
            self.image = self.tilesList[2]
            self.BASED_DMG = 15
            self.cost = 60
            self.range = 100
            self.speed = 'average'

        if self.type == 3:
            self.image = self.tilesList[1]
            self.BASED_DMG = 5
            self.cost = 75
            self.range = 300
            self.speed = 'fast'

        if self.type == 4:
            self.image = self.tilesList[3]
            self.BASED_DMG = 70
            self.cost = 100
            self.range = 100
            self.speed = 'slow'

        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.y = y
        self.dataFont = pygame.font.SysFont("None", 20)

    def loadTiles(self):
        img = pygame.image.load(os.path.join('Images', 'tower.png'))
        self.tilesList = []
        tileSize = (25, 25)
        offset = ((0,0), (0,25), (25,0), (25,25))

        for i in range(4):
            temp_tile = pygame.Surface(tileSize)
            temp_tile.blit(img, (0, 0), (offset[i], tileSize))
            self.tilesList.append(temp_tile)

    def update(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.txtDraw()

    def txtDraw(self):
        t_damage = self.dataFont.render("Degats de base : %d"% self.BASED_DMG, 1, (255, 255, 255))
        t_range = self.dataFont.render("Portee : %d"% self.range, 1, (255, 255, 255))
        t_cost = self.dataFont.render("Cout : %d"% self.cost, 1, (255, 255, 255))
        t_speed = self.dataFont.render("Vitesse : " + self.speed, 1, (255, 255, 255))

        pos_x = 665
        pos_y = 200

        screen.blit(t_damage, (pos_x, pos_y))
        screen.blit(t_range, (pos_x, pos_y+25))
        screen.blit(t_cost, (pos_x, pos_y+50))
        screen.blit(t_speed, (pos_x, pos_y+75))
























