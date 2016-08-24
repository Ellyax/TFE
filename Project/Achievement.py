import pygame
import os
from Builder import *

class Achiev:
    def __init__(self):
        self.achievement_file = os.path.join('Images', 'achievement.txt')
        listAch = self.readFile()
        self.achiev1 = int(listAch[0])
        self.achiev2 = int(listAch[1])
        self.achiev3 = int(listAch[2])
        self.achiev4 = int(listAch[3])
        self.achiev5 = listAch[4]
        print self.achiev3

    def readFile(self):
        file = open(self.achievement_file, 'r')
        self.linesAchiev = file.readlines()
        listAchiev = []
        for i in range(len(self.linesAchiev)):
            listAchiev.append(self.linesAchiev[i])
        return listAchiev

