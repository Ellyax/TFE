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

    se = 0
    lives = 15
    gold = 200
    score = 0
    countdown = 10
    countdown_2 = countdown
    enemy_type = 'easy'
    next_wave = 0
    win_check = 0
    target_lines = 1
    wait_wave = True
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
                        count = 1
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
            print mapType
            others.clear(screen, background)
            map = MapMaker.Map(mapType, background)
            map.mapMaking()
            waypoints = map.checkTurnPoints()
            grid = MapMaker.GridControl(mapType, screen, map.getCharList())
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
                    del enemyList[:]
                    del towerList[:]
                    enemy.empty()
                    towers.empty()
                    player.gold = player.STARTGOLD
                    player.score = 0
                    player.health = player.STARTHEALTH
                    player.wave = 0
                    player.enemy_count = 0
                    main()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    m_x = pygame.mouse.get_pos()
                    m_y = pygame.mouse.get_pos()
                    if m_x < 625:
                        grid.click()
                    else:
                        grid.unclick()
                    info.unclick()
                    twrSurf.fill((255, 0, 255))

                    for tower in towerList:
                        if tower.rect.collidepoint(pygame.mouse.get_pos()):
                            towerselected = tower
                            pygame.draw.circle(twrSurf, (153, 204, 255), towerselected.rect.center, towerselected.range, towerselected.range)
                            info.setInfo(towerselected.dmg, towerselected.range, towerselected.upgrade_cost, towerselected.lvl, towerselected.type)

                    if t1_sprite.rect.collidepoint(pygame.mouse.get_pos()):
                        if grid.checkTower() == 'No':
                            if player.gold >= t1_cost:
                                towers.add(TowerSprites.Tower(grid.setTower(), 1))
                                player.gold -= t1_cost

                    if t2_sprite.rect.collidepoint(pygame.mouse.get_pos()):
                        if grid.checkTower() == 'No':
                            if player.gold >= t2_cost:
                                towers.add(TowerSprites.Tower(grid.setTower(), 2))
                                player.gold -= t2_cost

                    if t3_sprite.rect.collidepoint(pygame.mouse.get_pos()):
                        if grid.checkTower() == 'No':
                            if player.gold >= t3_cost:
                                towers.add(TowerSprites.Tower(grid.setTower(), 3))
                                player.gold -= t3_cost

                    if t4_sprite.rect.collidepoint(pygame.mouse.get_pos()):
                        if grid.checkTower() == 'No':
                            if player.gold >= t4_cost:
                                towers.add(TowerSprites.Tower(grid.setTower(), 4))
                                player.gold -= t4_cost


                if event.type == pygame.KEYDOWN and event.key == pygame.K_u:
                    if towerselected != None:
                        if towerselected.ugrade_cost <= player.gold:
                            player.gold -= towerselected.upgrade_cost
                            towerselected.upgrade()
                            info.setInfo(towerselected.dmg, towerselected.range, towerselected.upgrade_cost, towerselected.lvl, towerselected.type)
                            pygame.draw.circle(twrSurf, (153, 204, 255), towerselected.rect.center, towerselected.range, towerselected.range)

                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    if wait_wave == True:
                        wait_wave = False
                        if player.wave <= 4:
                            player.wave += 1

            if player.wave <= 5:
                if next_wave == 1:
                    if enemy_type == 'easy':
                        enemy_type = 'easy'
                        next_wave = 0
                        win_check = 0
                        wait_wave = True
                        countdown_2 = 10
                    else:
                        enemy_type = 'easy'
                        next_wave = 0
                        win_check = 0
                        wait_wave = True
                        countdown_2 = 5

            if player.wave == 5 and se == 0:
                countdown = 300
                pygame.mixer.stop()
                se = 1

            if player.health > 0:
                if wait_wave == True:
                    i = 1
                else:
                    if player.wave == 5:
                        if countdown == 0:
                            if win_check < win_count:
                                EnemySprites.EasyEnemy(player.wave, map.checkTurnPoints(), mode)
                                win_check += 1
                                countdown = 50

                            if (win_count == win_check) and (player.enemy_count == 0):
                                uwin = 1
                        else:
                            countdown -= 1

                    else:
                        if countdown == 0:
                            if enemy_type == 'easy':
                                if win_check <= player.wave * 3 + 10:
                                    EnemySprites.EasyEnemy(player.wave, map.checkTurnPoints(), mode)
                                    win_check += 1
                                if player.enemy_count == 0:
                                    next_wave = 1
                            else:
                                if win_check <= player.wave * 3 + 5:
                                    EnemySprites.EasyEnemy(player.wave, map.checkTurnPoints(), mode)
                                    win_check += 1
                                if player.enemy_count == 0:
                                    next_wave = 1
                            countdown = countdown_2
                        else:
                            countdown -= 1

            else:
                uwin = 2
                # player Loses The Game

            enemy.clear(screen, background)
            towers.clear(screen, background)
            t_sprites.clear(screen, background)

            enemy.update()
            towers.update()
            map.mapMaking()
            others.update()
            t_sprites.update()
            screen.blit(twrSurf, (0, 0))
            t_sprites.draw(screen)
            towers.draw(screen)











            pygame.display.flip()

            m__x = pygame.mouse.get_pos()
            m__y = pygame.mouse.get_pos()
            pygame.display.set_caption(str(m__x) + " , " + str(m__y))

    pygame.quit()

if __name__ == "__main__":
    main()