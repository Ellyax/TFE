import pygame
import sys
import os

from Builder import *

class Map:
    def __init__(self, map, background):
        self.mapFile = os.path.join('Images', map + 'map.txt')
        self.linesList = None
        self.turnPoints = None
        self.charList = None

        self.ig_map_area = pygame.image.load(os.path.join('Images', map + 'map.png'))
        tiles = pygame.image.load(os.path.join('Images', 'tiles.png'))
        self.ig_menu = pygame.image.load(os.path.join('Images', 'sidebar.png'))
        self.TILESIZE = 25

        self.display = pygame.display.get_surface()

        self.tilesList = []
        tileSize = (25,25)
        offset = ((0,0), (0,25))

        for i in range(2):
            temp_tile = pygame.Surface(tileSize)
            temp_tile.blit(tiles, (0,0), (offset[i], tileSize))
            self.tilesList.append(temp_tile)



    def mapMaking(self):
        file = open(self.mapFile, 'r')
        self.linesList = file.readlines()
        self.charList = self.linesList

        ig_map_area_rect = self.ig_map_area.get_rect()
        ig_map_area_rect.topleft = (0, 0)
        self.display.blit(self.ig_map_area, ig_map_area_rect)


        for i in range(len(self.linesList)):
            self.linesList[i] = self.linesList[i].strip()
            for j in range(len(self.linesList[i])):
                if self.linesList[i][j] != 'X':
                    tile = self.loadTile(self.linesList[i][j], i, j)
                    tileRect = tile.get_rect()
                    tileRect.left = self.TILESIZE * j
                    tileRect.top = self.TILESIZE * i
                    self.display.blit(tile, tileRect)


        ig_menu_rect = self.ig_menu.get_rect()
        ig_menu_rect.topleft = (625, 0)
        self.display.blit(self.ig_menu, ig_menu_rect)



    def loadTile(self, char, i, j):
        image = self.tilesList[1]

        #if char == 'X':
        #    image = self.tilesList[0]
        if char == 'O':
            image = self.tilesList[1]
        elif char == 'S':
            image = self.tilesList[1]
            self._S = (self.TILESIZE * j + 12, self.TILESIZE * i +12)
        elif char == 'E':
            image = self.tilesList[1]
            self._E = (self.TILESIZE * j + 12, self.TILESIZE * i +12)


        if char == '0':
            self._0 = (self.TILESIZE*j+12,self.TILESIZE*i+12)
        elif char == '1':
            self._1 = (self.TILESIZE * j + 12, self.TILESIZE * i + 12)
        elif char == '2':
            self._2 = (self.TILESIZE * j + 12, self.TILESIZE * i + 12)
        elif char == '3':
            self._3 = (self.TILESIZE * j + 12, self.TILESIZE * i + 12)
        elif char == '4':
            self._4 = (self.TILESIZE * j + 12, self.TILESIZE * i + 12)
        elif char == '5':
            self._5 = (self.TILESIZE * j + 12, self.TILESIZE * i + 12)
        elif char == '6':
            self._6 = (self.TILESIZE * j + 12, self.TILESIZE * i + 12)
        elif char == '7':
            self._7 = (self.TILESIZE * j + 12, self.TILESIZE * i + 12)
        elif char == '8':
            self._8 = (self.TILESIZE * j + 12, self.TILESIZE * i + 12)
        elif char == '9':
            self._9 = (self.TILESIZE * j + 12, self.TILESIZE * i + 12)

        return image

    def getCharList(self):
        return self.charList

    def checkTurnPoints(self):
        self.turnPoints = [self._S, self._E, self._0, self._1, self._2, self._3, self._4, self._5, self._6, self._7, self._8, self._9]
        return self.turnPoints






class GridControl:
    def __init__(self, map, screen, grid):
        self.charList = grid
        self.TILESIZE = 25
        self.surf = pygame.Surface((self.TILESIZE,self.TILESIZE))
        self.m_x = -100
        self.m_y = -100
        self.C_red = (255,0,0)
        self.C_green = (0,255,0)
        self.C_yellow = (255,255,0)
        self.C_empty = (0,0,0)
        self.chosenColor = self.C_empty
        self.surf.set_alpha(255*0.4)
        self.surf.fill(self.chosenColor)
        self.doubleClik = 2
        self.clickLocX = -1000
        self.clickLocY = -1000

    def click(self):
        self.doubleClik = 2
        mux, muy = pygame.mouse.get_pos()
        self.clickLocX = mux/self.TILESIZE
        self.clickLocY = muy/self.TILESIZE
        self.m_x = self.clickLocX*self.TILESIZE
        self.m_y = self.clickLocY*self.TILESIZE

        if (self.m_x < 625) and (self.m_y < 625):
            tile = self.checkTile(self.charList[self.clickLocY][self.clickLocX])
            self.chosenColor = tile

        self.surf.fill(self.chosenColor)

    def unclick(self):
        self.doubleClik -= 1
        if self.doubleClik == 0:
            self.m_x = -100
            self.m_y = -100
            self.chosenColor = self.C_empty

    def checkTile(self, char):

        if char == 'X':
            return self.C_green
        elif char =='T':
            return self.C_yellow
        else:
            return self.C_red

    def setTower(self):
        if (self.chosenColor == self.C_green):
            changeChar = list(self.charList[self.clickLocY])
            changeChar[self.clickLocX] = 'T'
            changeChar = "".join(changeChar)
            self.charList[self.clickLocY] = changeChar
            self.chosenColor = self.C_yellow
            self.surf.fill(self.chosenColor)
            return (self.m_x, self.m_y)

    def removeTower(self):
        if (self.chosenColor == self.C_yellow):
            changeChar = list(self.charList[self.clickLocY])
            changeChar[self.clickLocX] = 'X'
            changeChar = "".join(changeChar)
            self.drawSelection()
            self.charList[self.clickLocY] = changeChar
            self.chosenColor = self.C_green
            self.surf.fill(self.chosenColor)

    def checkTower(self):
        if self.chosenColor != self.C_empty:
            tile = self.checkTile(self.charList[self.clickLocY][self.clickLocX])
            if tile == self.C_green:
                return 'No'
            else:
                return 'Yes'
