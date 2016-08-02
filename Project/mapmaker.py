import pygame
import sys
import os

from Builder import *

class Map:
    def __init__(self, map, background):
        # TODO : verifier l utilisation d un fichier txt pr la map ou l utilisation d une image background
        self.mapFile = os.path.join('Images', map + 'map.txt')
        self.linesList = None
        self.wayPoint = None
        self.charList = None

        # TODO : verifier l utilisation d une tile grise pr dessiner le path plutot qu une image de background
        tiles = pygame.image.load(os.path.join('Images', 'tiles.png'))
        self.ig_map_area = pygame.image.load(os.path.join('Images', map + 'map.png'))
        self.ig_menu = pygame.image.load(os.path.join('Images', 'ig_menu.png'))
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
        self.lineList = file.readlines()
        self.charList = self.linesList

        for i in range(len(self.linesList)):
            self.linesList[i] = self.linesList[i].strip()
            for j in range(len(self.linesList[i])):
                tile = self.loadTile(self.linesList[i][j], i, j)
                tileRect = tile.get_rect()
                tileRect.left = self.TILESIZE * j
                tileRect.top = self.TILESIZE * i
                self.display.blit(tile, tileRect)

        ig_map_area_rect = self.ig_map_area.get_rect()
        ig_map_area_rect.topleft=(0, 0)

        ig_menu_rect = self.ig_menu.get_rect()
        ig_menu_rect.topleft = (625, 0)
        self.display.blit(self.ig_menu, ig_menu_rect)

    def loadTile(self, char, i, j):
        if char == 'X':
            tile = self.tilesList[0]
        elif char == 'O':
            tile = self.tilesList[1]

        if char == '0':
            self._0 = (self.TILESIZE * j + 12, self.TILESIZE * i + 12)
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

        return tile

    def getCharList(self):
        return self.charList

    def turnPoints(self):
        self.turnPoints = [self._0, self._1, self._2, self._3, self._4, self._5, self._6, self._7, self._8, self._9]
        return self.turnPoints
