import pygame
import os

class Achiev:
    def __init__(self):
        self.achievement_file = os.path.join('Images', 'achievement.txt')
        listAch = self.readFile()
        self.achiev1 = listAch[0]
        self.achiev2 = listAch[1]
        self.achiev3 = listAch[2]
        self.achiev4 = listAch[3]

    def readFile(self):
        file = open(self.achievement_file, 'r')
        self.linesAchiev = file.readlines()
        listAchiev = []
        for i in range(len(self.linesAchiev)):
            listAchiev.append(self.linesAchiev[i])
        return listAchiev
