import sys
import pygame
import time
import random
import os
import consts as c
import main_menu
import pause
import game_over
import levels as l
import player

def vs():
    c.playing_vs = True
    all_platforms = [l.platforms_1, l.platforms_2]
    c.score2 = 0
    #Main program loop to display framerate and handle exiting
    while c.playing_vs:
        if c.second_timer == 0:
            main_menu.player_obj = player.Player()
            main_menu.player_obj2 = player.Player()
            main_menu.player_obj.x = c.screen_width-main_menu.player_obj.player_width
            
        #Screen reset to avoid multiple blits overlaying
        c.screen.fill(c.black)

        if main_menu.player_obj.rect.top - c.cameraY > c.screen_height:
            game_over.vs_over("Blue", False)
        elif main_menu.player_obj2.rect.top - c.cameraY > c.screen_height:
            game_over.vs_over("Red", False)

        if c.score < ((-main_menu.player_obj.y)+570)/10:
            c.score = ((-main_menu.player_obj.y)+570)/10
        if c.score2 < ((-main_menu.player_obj2.y)+570)/10:
            c.score2 = ((-main_menu.player_obj2.y)+570)/10
            
        score_text = "Score:{0:.0f}".format(c.score)
        scoretext = c.score_font.render(score_text, 1, c.red, 150)
        c.screen.blit(scoretext, (5, 0))

        score_text2 = "Score:{0:.0f}".format(c.score2)
        scoretext = c.score_font.render(score_text2, 1, c.blue, 150)
        c.screen.blit(scoretext, (5, 40))
        
        #Applies gravity to the players
        main_menu.player_obj.movey += c.gravity
        main_menu.player_obj2.movey += c.gravity
        
        #Draws and updates the players
        main_menu.player_obj.draw(c.red)
        main_menu.player_obj.update()
        
        main_menu.player_obj2.draw(c.blue)
        main_menu.player_obj2.update()
        
        l.floor.draw()
        
        #Generates sets of platforms from the all_platforms list with increasing c.offset to allow the players to jump up/higher
        if c.level_timer % c.max_level_timer == 0 and c.generate_platforms == True:
            c.levels.append(l.Level(random.choice(all_platforms), 650 * c.level_timer/c.max_level_timer, "y"))
            
        #Only allows generation of platforms within a set window of the players so that the game does not generate infinite platforms and slow down
        if len(c.levels) > 0:
            if (main_menu.player_obj2.y)+1000 < c.levels[0].offset:
                c.levels.pop(0)
            elif (main_menu.player_obj.y)+1000 < c.levels[0].offset:
                c.levels.pop(0)
            elif (main_menu.player_obj2.y)-1000 > c.levels[-1].offset:
                c.generate_platforms = False
            elif (main_menu.player_obj.y)-1000 > c.levels[-1].offset:
                c.generate_platforms = False
            else:
                c.generate_platforms = True
                c.level_timer += 1
        
        #Draws the generated platforms from the levels list onto the screen
        for level in c.levels:
            level.draw()

        #Continually moves the camera upwards once a set amount of time has passed
        c.cameraY -= c.camera_movement
        c.camera_movement = max(c.score/500, c.score2/500)

        if main_menu.player_obj.y-80 < c.cameraY:
            c.cameraY = main_menu.player_obj.y-80
        if main_menu.player_obj2.y-80 < c.cameraY:
            c.cameraY = main_menu.player_obj2.y-80

        main_menu.player_obj.jump_charge_increase = min(1, c.score/1000)
        main_menu.player_obj2.jump_charge_increase = min(1, c.score/1000)

        #Sets frames per second for the game
        milliseconds = c.clock.tick(c.fps)
        
        #Primary loop for input handling
        for event in pygame.event.get():
            if event.type == pygame.display.quit:
                main_menu.quit_game()
            #Handles the pressing of a key
            if event.type == pygame.KEYDOWN:
                #PLAYER 2 CONTROLS
                if event.key == c.up:
                    if main_menu.player_obj2.on_platform == True:
                        main_menu.player_obj2.player_speed = 3
                        main_menu.player_obj2.charging = True
                        main_menu.player_obj2.draw(c.blue)
                        main_menu.player_obj2.update()
                if event.key == pygame.K_ESCAPE:
                    pause.is_paused = True
                    pause.paused_vs()
                if event.key == c.left:
                    main_menu.player_obj2.control_x(-1)
                if event.key == c.right:
                    main_menu.player_obj2.control_x(1)
                if event.key == c.down:
                    main_menu.player_obj2.control_y(10)

                #PLAYER 1 CONTROLS
                if event.key == c.up2:
                    if main_menu.player_obj.on_platform == True:
                        main_menu.player_obj.player_speed = 3
                        main_menu.player_obj.charging = True
                        main_menu.player_obj.draw(c.red)
                        main_menu.player_obj.update()
                if event.key == pygame.K_LEFT:
                    main_menu.player_obj.control_x(-1)
                if event.key == pygame.K_RIGHT:
                    main_menu.player_obj.control_x(1)
                if event.key == pygame.K_DOWN:
                    main_menu.player_obj.control_y(10)
                    
            #Handles the releasing of a key
            if event.type == pygame.KEYUP:
                if event.key == c.up:
                    if main_menu.player_obj2.on_platform == True:
                        main_menu.player_obj2.update()
                        main_menu.player_obj2.control_y(-15*main_menu.player_obj2.jump_charge - main_menu.player_obj2.jump_charge_increase*8)
                        main_menu.player_obj2.player_speed = 10
                        main_menu.player_obj2.jump_charge = 0
                        main_menu.player_obj2.charging = False
                        main_menu.player_obj2.on_platform = False
                if event.key == c.left:
                    main_menu.player_obj2.control_x(0)
                if event.key == c.right:
                    main_menu.player_obj2.control_x(0)
                if event.key == c.down:
                    main_menu.player_obj2.control_y(0)

                if event.key == c.up2:
                    if main_menu.player_obj.on_platform == True:
                        main_menu.player_obj.update()
                        main_menu.player_obj.control_y(-15*main_menu.player_obj.jump_charge - main_menu.player_obj.jump_charge_increase*8)
                        main_menu.player_obj.player_speed = 10
                        main_menu.player_obj.jump_charge = 0
                        main_menu.player_obj.charging = False
                        main_menu.player_obj.on_platform = False
                if event.key == pygame.K_LEFT:
                    main_menu.player_obj.control_x(0)
                if event.key == pygame.K_RIGHT:
                    main_menu.player_obj.control_x(0)
                if event.key == pygame.K_DOWN:
                    main_menu.player_obj.control_y(0)
                    
        #Sets screen boundaries and whether either player is on the floor or on a wall
        if main_menu.player_obj.x >= c.screen_width-main_menu.player_obj.player_width:
            main_menu.player_obj.x = c.screen_width - main_menu.player_obj.player_width
        if main_menu.player_obj.x <= 0:
            main_menu.player_obj.x = 0
            
        if main_menu.player_obj2.x >= c.screen_width-main_menu.player_obj2.player_width:
            main_menu.player_obj2.x = c.screen_width - main_menu.player_obj2.player_width
        if main_menu.player_obj2.x <= 0:
            main_menu.player_obj2.x = 0
                    
        #Print framerate in window caption
        pygame.display.set_caption("Skybound     FPS: {0:.0f}".format(c.clock.get_fps()))
        
        #Updates the display and increments the timers accordingly
        pygame.display.update()
        c.second_timer += 1
    pygame.display.quit()
