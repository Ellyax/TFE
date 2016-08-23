import pygame
import math
import os

pygame.mixer.init()

class Player():
    def __init__(self):
        self.health = 25
        self.STARTHEALTH = self.health
        self.gold = 2000
        self.STARTGOLD = self.gold
        self.score = 0
        self.wave = 0
        self.enemy_count = 0

class MapChoice(pygame.sprite.Sprite):
    def __init__(self, x, y, type):
        pygame.sprite.Sprite.__init__(self)

        self.img_loader()
        self.image = self.imgList[type]
        self.type = type
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.selected = 0

    def img_loader(self):
        img_button = pygame.image.load(os.path.join ('Images', 'menu.png'))
        self.imgList = []
        imgSize = (140, 40)
        offset = ((0,0), (0,40), (0,79), (0,119), (0,158))

        for i in range(5):
            temp_img = pygame.Surface(imgSize)
            temp_img.blit(img_button, (0,0), (offset[i], imgSize))
            self.imgList.append(temp_img)

def dist(first, second, tower_range):
    aim_x, aim_y = first

    if range == 0:
        return 1
    elif (math.sqrt((second.centerx-aim_x)**2 + (second.centery-aim_y)**2)) <= tower_range :
        return 1

def drawText():
    my_font = pygame.font.SysFont("None", 20)
    p_life = my_font.render("Vie : %d" % player.health, 1, (255, 255, 255))
    p_score = my_font.render("Score : %d" % player.score, 1, (255, 255, 255))
    p_gold = my_font.render("Argent : $%d" % player.gold, 1, (255, 255, 255))
    p_wave = my_font.render("Vague : %d" % player.wave, 1, (255, 255, 255))

    placement_x = 665
    placement_y = 20
    screen.blit(p_life, (placement_x, placement_y))
    screen.blit(p_score, (placement_x, placement_y + 25))
    screen.blit(p_gold, (placement_x, placement_y + 100))
    screen.blit(p_wave, (placement_x, placement_y + 50))

class Info():
    def __init__(self):
        self.draw = 0
        self.p_x = 665
        self.p_y = 340


    def setInfo(self, power, range, up_cost, level, type):
        to_font = pygame.font.SysFont("None", 20)

        if type == 1:
            self.t_type = to_font.render("Type: Classique", 1, (255, 255, 255))
        elif type == 2:
            self.t_type = to_font.render("Type: Rapide", 1, (255, 255, 255))
        elif type == 3:
            self.t_type = to_font.render("Type: Classique", 1, (255,255,255))
        elif type == 4:
            self.t_type = to_font.render("Type: Lente", 1, (255, 255, 255))


        if level == 2:
            self.t_level = to_font.render("Niveau : 2 (Max)", 1, (255, 255, 255))
        else:
            self.t_level = to_font.render("Niveau : %d" % level, 1, (255, 255, 255))

        self.t_power = to_font.render("Degats : %d" % power, 1, (255, 255, 255))

        if range != 0:
            self.t_range = to_font.render("Portee: %d" % range, 1, (255, 255, 255))
        else:
            self.t_range = to_font.render("Portee: Illimitee", 1, (255, 255, 255))

        self.t_up_cost = to_font.render("Cout d'amelioration: $%d" % up_cost, 1, (255, 255, 255))

        if type == 1:
            self.t_speed = to_font.render("Vitesse de tir: Moyenne", 1, (255, 255, 255))
        elif type == 2:
            self.t_speed = to_font.render("Vitesse de tir: Rapide", 1, (255, 255, 255))
        elif type == 3:
            self.t_speed = to_font.render("Vitesse de tir: Moyenne", 1, (255, 255, 255))
        elif type == 4:
            self.t_speed = to_font.render("Vitesse de tir: Lente", 1, (255, 255, 255))


        if up_cost != 0:
            self.up_text = to_font.render("'U' pour ameliorer", 1, (255, 255, 255))
        else:
            self.up_text = to_font.render("", 1, (255, 255, 255))
        self.draw = 1

    def drawInfo(self):
        if self.draw == 1:
            screen.blit(self.t_type, (self.p_x, self.p_y))
            screen.blit(self.t_level, (self.p_x, self.p_y + 25))
            screen.blit(self.t_power, (self.p_x, self.p_y + 50))
            screen.blit(self.t_range, (self.p_x, self.p_y + 75))
            screen.blit(self.t_speed, (self.p_x, self.p_y + 100))
            screen.blit(self.t_up_cost, (self.p_x, self.p_y + 125))
            screen.blit(self.up_text, (self.p_x, self.p_y + 150))

    def unclick(self):
        self.draw = 0


player = Player()
info = Info()
enemy = pygame.sprite.Group()
towers = pygame.sprite.Group()

enemyList = list()
towerList = list()
enemy_count = 0

screen = pygame.display.set_mode((825,625))
pygame.display.set_caption("HeH Tower Defense")

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




















