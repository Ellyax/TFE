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
    button1 = MapChoice(75, 100, 0)

    ### Map
    mapType = 'trica'
    mapS = MapMaker.Map(mapType, background)
    print mapType
    mapS.mapMaking()

    mode = 'easy'
    cont = 0
    towerselected = None

    others = pygame.sprite.Group(button1)

    clock = pygame.time.Clock()
    noQuit = True
    noUnderQuit = True

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
                    if button1.rect.collidepoint(pygame.mouse.get_pos()):
                        button1.change()
                        mapType = 'trica'
                        count = 1
                        noUnderQuit = False

            others.clear(screen, background)
            mapS.mapMaking()
            pygame.draw.rect(screen, (51, 117, 20), (60, 85, 505, 300))
            others.draw(screen)
            pygame.display.flip()

        if cont == 1:
            others.clear(screen, background)

            map = MapMaker.Map(mapType, background)
            map.mapMaking()
            waypoints = map.turnPoints()

            # set up the grid
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