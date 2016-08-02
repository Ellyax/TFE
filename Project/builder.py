import pygame
import math
import sys
import os

pygame.mixer.init()

player = Player()
info = Info()
baddies = pygame.sprite.Group()
towers = pygame.sprite.Group()

baddieList = list()
towerList = list()
enemyCount = 0

screen = pygame.display.set_mode((825,625))
pygame.display.set_caption("Isim Tower Defense")

background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill ((0,0,0))
screen.blit(background, (0,0))

twrSurf = pygame.Surface((625,625))
twrSurf.set_alpha(255*0.4)
twrSurf.fill((255,0,255))
twrSurf.set_colorkey((255,0,255))

drkSurf = pygame.Surface((625,625))
drkSurf.set_alpha(255*0.6)
drkSurf.fill((20,20,20))


class Player():
    def __init__(self):
        self.health = 25
        self.STARTHEALTH = self.health
        self.gold = 200
        self.STARTGOLD = self.gold
        self.score = 0
        self.wave = 0
        self.enemy_count = 0

class MapChoice(pygame.sprite.Sprite):
    def __init__(self, x, y, type):
        pygame.sprite.Sprite.__init__(self)

        self.img_loader()
        self.img = self.imgList[type]
        self.type = type
        self.rect = self.img.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.selected = 0

    def img_loader(self):
        img_button = pygame.image.load(os.path.join ('Images', 'menu.png'))
        self.imgList = []
        imgSize = (215, 55)
        offset = ((0,0), (0,55), (0,110), (0,165))

        for i in range(4):
            temp_img = pygame.Surface(imgSize)
            temp_img.blit(img_button, (0,0), (offset[i], imgSize))
            self.imgList.append(temp_img)

def dist(first, second, tower_range):
    aim_x = first
    aim_y = first

    if range == 0:
        return 1
    elif (math.sqrt((second.center_x-aim_x)**2 + (second.center_y-aim_y)**2)) <= tower_range :
        return 1

def drawText():
    my_font = pygame.font._SysFont("None", 24)
    p_life = my_font.render("Life : %d" % player.health, 1, (255, 255, 255))
    p_score = my_font.render("Score : %d" % player.score, 1, (255, 255, 255))
    p_gold = my_font.render("Gold : $%d" % player.gold, 1, (255, 255, 255))
    p_wave = my_font.render("Wave : %d" % player.wave, 1, (255, 255, 255))

    placement_x = 665
    placement_y = 60
    screen.blit(p_life, (placement_x, placement_y))
    screen.blit(p_score, (placement_x, placement_y + 25))
    screen.blit(p_gold, (placement_x, placement_y + 50))
    screen.blit(p_wave, (placement_x, placement_y + 75))

class Info():
    def __init__(self):
        self.draw = 0
        self.p_x = 665
        self.p_y = 340

    def setInfo(selfself, power, range, up_cost, level, type):
        to_font = pygame.font.SysFont("None", 20)
        to1_font = pygame.font.SysFont("None", 28)

        if type == 1:
            self.t_type = to_font.render("Type: Classic", 1, (255, 255, 255))
        elif type == 2:
            self.t_type = to_font.render("Type: Fast", 1, (255, 255, 255))

        if level == 2:
            self.t_level = to_font.render("Level: 2 (Max)", 1, (255, 255, 255))
        else:
            self.t_level = to_font.render("Level: %d" % level, 1, (255, 255, 255))

        self.t_power = to_font.render("Damage: %d" % power, 1, (255, 255, 255))

        if range != 0:
            self.t_range = to_font.render("Range: %d" % range, 1, (255, 255, 255))
        else:
            self.t_range = to_font.render("Range: Unlimited", 1, (255, 255, 255))

        self.t_up_cost = to_font.render("Upgrade Cost: $%d" % up_cost, 1, (255, 255, 255))

        if type == 1:
            self.t_speed = to_font.render("Speed: Medium", 1, (255, 255, 255))
        elif type == 2:
            self.t_speed = to_font.render("Speed: Fast", 1, (255, 255, 255))


        if up_cost != 0:
            self.up_text = to_font.render("Press U to upgrade", 1, (255, 255, 255))
        else:
            self.up_text = to_font.render("", 1, (255, 255, 255))
        self.draw = 1
























