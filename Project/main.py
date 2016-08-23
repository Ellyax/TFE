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

    t1_sprite = TowerSprites.TowerSprite(680, 140, 1)
    t2_sprite = TowerSprites.TowerSprite(710, 140, 2)
    t3_sprite = TowerSprites.TowerSprite(740, 140, 3)
    t4_sprite = TowerSprites.TowerSprite(770, 140, 4)


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
    gold = 2000
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
        if count == 0:
            noUnderQuit = True
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
                            mapType = 'wait'
                            count = 1
                            noUnderQuit = False

                        if b_solo.rect.collidepoint(pygame.mouse.get_pos()):
                            mapType = 'trica'
                            count = 2
                            noUnderQuit = False

                        if b_multi.rect.collidepoint(pygame.mouse.get_pos()):
                            mapType = 'wait'
                            count = 3
                            noUnderQuit = False

                        if b_achiev.rect.collidepoint(pygame.mouse.get_pos()):
                            mapType = 'wait'
                            count = 4
                            noUnderQuit = False

                        if b_exit.rect.collidepoint(pygame.mouse.get_pos()):
                            noUnderQuit = False
                            noQuit = False


                others.clear(screen, background)
                mapS.mapMaking()
                others.draw(screen)
                pygame.display.flip()

        ### ------------------  MODE STORY  ------------------
        if count == 1:
            others.clear(screen, background)
            map = MapMaker.Map(mapType, background)
            map.mapMaking()
            noUnderQuit = True
            while noUnderQuit:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        noUnderQuit = False
                        noQuit = False

                    elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                        noUnderQuit = False
                        noQuit = False

                    elif event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                        count = 0
                        noUnderQuit = False
                    pygame.display.flip()




        ### ------------------  MODE SOLO  ------------------
        if count == 2:
            others.clear(screen, background)
            map = MapMaker.Map(mapType, background)
            map.mapMaking()
            waypoints = map.checkTurnPoints()
            grid = MapMaker.GridControl(mapType, screen, map.getCharList())
            noUnderQuit = True



        ### ------------------  MODE MULTI  ------------------
        if count == 3:
            others.clear(screen, background)
            map = MapMaker.Map(mapType, background)
            map.mapMaking()
            multiFont = pygame.font.SysFont("None", 30)
            multi_txt = multiFont.render("En construction. Appuyez sur R pour revenir au menu principal", 1, (255, 255, 255))
            screen.blit(multi_txt, (0, 213))
            noUnderQuit = True
            while noUnderQuit:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        noUnderQuit = False
                        noQuit = False

                    elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                        noUnderQuit = False
                        noQuit = False

                    elif event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                        count = 0
                        noUnderQuit = False
                    pygame.display.flip()



        ### ------------------  MODE ACHIEV  ------------------
        if count == 4:
            others.clear(screen, background)
            map = MapMaker.Map(mapType, background)
            map.mapMaking()
            achievFont = pygame.font.SysFont("None", 30)
            achiev1_txt = achievFont.render("Tuer 1000 ennemis :", 1, (255, 255, 255))
            achiev2_txt = achievFont.render("Finir le mode histoire :", 1, (255, 255, 255))
            achiev3_txt = achievFont.render("Survivre 20 vagues en mode solo :", 1, (255, 255, 255))
            achiev4_txt = achievFont.render("Obtenir plus de 100.000 points en mode solo :", 1, (255, 255, 255))
            achiev1_result_txt = achievFont.render("X", 1, (255, 0, 0))
            achiev2_result_txt = achievFont.render("X", 1, (255, 0, 0))
            achiev3_result_txt = achievFont.render("X", 1, (255, 0, 0))
            achiev4_result_txt = achievFont.render("X", 1, (255, 0, 0))
            screen.blit(achiev1_txt, (10, 30))
            screen.blit(achiev2_txt, (10, 90))
            screen.blit(achiev3_txt, (10, 150))
            screen.blit(achiev4_txt, (10, 210))
            screen.blit(achiev1_result_txt, (500, 30))
            screen.blit(achiev2_result_txt, (500, 90))
            screen.blit(achiev3_result_txt, (500, 150))
            screen.blit(achiev4_result_txt, (500, 210))
            noUnderQuit = True
            while noUnderQuit:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        noUnderQuit = False
                        noQuit = False

                    elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                        noUnderQuit = False
                        noQuit = False

                    elif event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                        count = 0
                        noUnderQuit = False
                    pygame.display.flip()



        ### ------------------  BOUCLE DE JEU  ------------------
        if count != 0:
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
                        m_x, m_y = pygame.mouse.get_pos()
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
                            if towerselected.upgrade_cost <= player.gold:
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

                for tower in towerList:
                    if tower.reloadNum >= tower.reload:
                        enemy_point = tower.target()
                        if enemy_point:
                            tower.reloadNum = 0
                        if (enemy_point != None):
                            if tower.type == 1:
                                pygame.draw.line(screen, (255, 255, 255), tower.rect.center, enemy_point, 2)
                            if tower.type == 2:
                                pygame.draw.line(screen, (0, 0, 0), tower.rect.center, enemy_point, 5)
                            if tower.type == 3:
                                pygame.draw.line(screen, (255, 255, 255), tower.rect.center, enemy_point, 1)
                            if tower.type == 4:
                                pygame.draw.line(screen, (255, 255, 255), tower.rect.center, enemy_point, 3)
                            shot_sound.play()
                    else:
                        tower.reloadNum += 1

                enemy.draw(screen)

                # For drawing the enemy healthbar
                for en in enemyList:
                    pygame.draw.line(screen, (0, 0, 0), (en.rect.left, en.rect.top - 2), (en.rect.right, en.rect.top - 2), 3)
                    pygame.draw.line(screen, (255, 0, 0), (en.rect.left, en.rect.top - 2), (en.rect.left + (en.health * 1.0 / en.start_health * 1.0) * en.rect.width, en.rect.top - 2), 3)

                screen.blit(grid.surf, (grid.m_x, grid.m_y))
                drawText()
                info.drawInfo()
                if player.wave == 5:
                    screen.blit(drkSurf, (0, 0))

                if wait_wave == True:
                    pygame.draw.rect(screen, (100, 100, 50), (0, 625 - 40, 625, 40))
                    to1Font = pygame.font.SysFont("None", 30)
                    spaceTxt = to1Font.render("Appuyer sur la barre d'espace pour lancer la prochaine vague", 1, (255, 255, 255))
                    screen.blit(spaceTxt, (10, 625 - 25))

                if uwin == 1:
                    pygame.draw.rect(screen, (51, 117, 20), (200, 200, 210, 98))
                    to1Font = pygame.font.SysFont("None", 30)
                    spaceTxt = to1Font.render("You Win!", 1, (255, 255, 255))
                    scoreTxt = to1Font.render("Final Score: %d" % player.score, 1, (255, 255, 255))
                    restText = to1Font.render("To restart, press R", 1, (255, 255, 255))
                    screen.blit(spaceTxt, (255, 213))
                    screen.blit(scoreTxt, (213, 213 + 30))
                    screen.blit(restText, (213, 213 + 60))
                if uwin == 2:
                    pygame.draw.rect(screen, (51, 117, 20), (200, 200, 210, 98))
                    to1Font = pygame.font.SysFont("None", 30)
                    spaceTxt = to1Font.render("You Lose!", 1, (255, 255, 255))
                    scoreTxt = to1Font.render("Final Score: %d" % player.score, 1, (255, 255, 255))
                    restText = to1Font.render("To restart, press R", 1, (255, 255, 255))
                    screen.blit(spaceTxt, (255, 213))
                    screen.blit(scoreTxt, (213, 213 + 30))
                    screen.blit(restText, (213, 213 + 60))


                pygame.display.flip()
    pygame.quit()

if __name__ == "__main__":
    main()