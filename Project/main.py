import pygame
import os
import sys
import MapMaker
import EnemySprites
import TowerSprites

from Builder import *

pygame.mixer.init()

def main():
    pygame.init()

    ### Handling all the sounds
    pygame.mixer.stop()
    background_sound = pygame.mixer.Sound(os.path.join('Sounds', 'collision.ogg'))
    background_sound.set_volume(10)
    background_sound.play(-1)

    shot_sound = pygame.mixer.Sound(os.path.join('Sounds', 'gun.ogg'))
    shot_sound.set_volume(5)

    ### Menu
    b_story = MapChoice(252, 100, 0)
    b_solo = MapChoice(252, 170, 1)
    b_multi = MapChoice(252, 240, 2)
    b_achiev = MapChoice(252, 310, 3)
    b_exit = MapChoice(252, 380, 4)

    ### Tower
    t1_cost = 50
    t2_cost = 60
    t3_cost = 75
    t4_cost = 100

    t1_sprite = TowerSprites.TowerSprite(695, 175, 1)
    t2_sprite = TowerSprites.TowerSprite(725, 175, 2)
    t3_sprite = TowerSprites.TowerSprite(755, 175, 3)
    t4_sprite = TowerSprites.TowerSprite(785, 175, 4)


    ### Map
    mapType = 'clean'
    mapS = MapMaker.Map(mapType, background)
    mapS.mapMaking()

    mode = 'easy'
    count = 0
    tower_selected = None

    others = pygame.sprite.Group(b_story, b_solo, b_multi, b_achiev, b_exit)
    t_sprites = pygame.sprite.Group(t1_sprite, t2_sprite, t3_sprite, t4_sprite)

    clock = pygame.time.Clock()
    noQuit = True
    noUnderQuit = True

    lives = 15
    gold = 200
    score = 0
    countdown = 10
    countdown_2 = countdown
    enemy_type = 'classic'
    next_wave = 0
    win_check = 0
    target_lines = 1
    wait_wave = 1
    uwin = 0
    win_count = 1


    while noQuit:
        clock.tick(30)
        while noUnderQuit:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    noUnderQuit = False
                    noQuit = False

                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    noUnderQuit = False
                    noQuit = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if b_story.rect.collidepoint(pygame.mouse.get_pos()):
                        mapType = 'trica'
                        count = 1
                        noUnderQuit = False

                    if b_solo.rect.collidepoint(pygame.mouse.get_pos()):
                        mapType = 'cisco'
                        print "solo mode button pressed"

                    if b_multi.rect.collidepoint(pygame.mouse.get_pos()):
                        print "multi mode button pressed"

                    if b_achiev.rect.collidepoint(pygame.mouse.get_pos()):
                        print "achiev button pressed"

                    if b_exit.rect.collidepoint(pygame.mouse.get_pos()):
                        noUnderQuit = False
                        noQuit = False


            others.clear(screen, background)
            mapS.mapMaking()
            others.draw(screen)
            pygame.display.flip()

        if count == 1:
            others.clear(screen, background)

            print "-------------------------------------"
            print mapType
            map = MapMaker.Map(mapType, background)
            map.mapMaking()
            waypoints = map.checkTurnPoints()
            print "map making done"

            # set up the grid
            grid = MapMaker.GridControl(mapType, screen, map.getCharList())

            print "grid control done"

            noUnderQuit = True

        while noUnderQuit:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    noQuit = False
                    noUnderQuit = False
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    noQuit = False
                    noUnderQuit = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_r:  # restarts the game
                    del baddieList[:]
                    del towerList[:]
                    baddies.empty()
                    towers.empty()
                    player.money = player.BASECASH
                    player.score = 0
                    player.health = player.BASEHP
                    player.wave = 0
                    player.enemyCount = 0
                    main()



    pygame.quit()

if __name__ == "__main__":
    main()