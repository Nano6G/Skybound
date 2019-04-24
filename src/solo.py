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
import gamemode


def solo():
    all_platforms = [l.platforms_1, l.platforms_2]
    c.playing_solo = True
    #Main program loop to display framerate and handle exiting
    while c.playing_solo:
        #Sets frames per second for the game
        milliseconds = c.clock.tick(c.fps)
        
        #Screen reset to avoid multiple blits overlaying
        c.screen.fill(c.black)
        
        #When first ran, the player object is set using the Player class
        if c.second_timer == 0:
            main_menu.player_obj = player.Player()
            
        #If the player is below the bottom of the screen, they lose and the game over function is ran
        if main_menu.player_obj.rect.top - c.cameraY > c.screen_height:
            gamemode.show_gamemode = False
            game_over.over = True
            c.playing_solo = False
            game_over.game_over(False)
        
        #Applies gravity to the player by adding a set value to their y velocity each frame
        main_menu.player_obj.movey += c.gravity
        
        #Draws and updates the player
        main_menu.player_obj.draw(c.red)
        main_menu.player_obj.update()

        #Draws the floor for the player to start on (Player can only land and jump on platforms)
        l.floor.draw()
        
        #Generates sets of platforms from the all_platforms list with increasing offset to allow the player to jump up/higher
        if c.level_timer % c.max_level_timer == 0 and c.generate_platforms == True:
            c.levels.append(l.Level(random.choice(all_platforms), 650 * c.level_timer/c.max_level_timer, "y"))
            
        #Only allows generation of platforms within a set window of the player so that the game does not generate infinite platforms and slow down
        if len(c.levels) > 0:
            if (main_menu.player_obj.y)+1000 < c.levels[0].offset:
                c.levels.pop(0)
            elif (main_menu.player_obj.y)-1000 > c.levels[-1].offset:
                c.generate_platforms = False
            else:
                c.generate_platforms = True
                c.level_timer += 1
        
        #Draws the generated platforms from the levels list onto the screen
        for level in c.levels:
            level.draw()

        #Continually moves the camera upwards after the player moves off the ground
        c.cameraY -= c.camera_movement
        c.camera_movement = c.score/500

        if main_menu.player_obj.y-150 < c.cameraY:
            c.cameraY = main_menu.player_obj.y-150
            
        """Calculate and display the score for the player,
        the score is calculated by using the player's y co-ordinate
        and turning it into relative magnitude number"""
        
        if c.score < ((-main_menu.player_obj.y)+570)/10:
            c.score = ((-main_menu.player_obj.y)+570)/10
        score_text = "Score:{0:.0f}".format(c.score)
        scoretext = c.score_font.render(score_text, 1, c.white, 150)
        c.screen.blit(scoretext, (5, 0))
        
        #Increases how fast the player charges their jump to make the game possible once the camera movement becomes faster
        main_menu.player_obj.jump_charge_increase = c.score/1000
        
        #Primary loop for input handling.
        for event in pygame.event.get():
            if event.type == pygame.display.quit:
                main_menu.quit_game()
            #Handles the pressing of a key
            if event.type == pygame.KEYDOWN:
                if event.key == c.space or event.key == c.up or event.key == c.up2:
                    if main_menu.player_obj.on_platform == True:
                        main_menu.player_obj.player_speed = 3
                        main_menu.player_obj.charging = True
                        main_menu.player_obj.draw(c.red)
                        main_menu.player_obj.update()
                if event.key == pygame.K_ESCAPE:
                    pause.is_paused = True
                    pause.paused("solo")
                if event.key == c.left or event.key == pygame.K_LEFT:
                    main_menu.player_obj.control_x(-1)
                if event.key == c.right or event.key == pygame.K_RIGHT:
                    main_menu.player_obj.control_x(1)
                if event.key == c.down or event.key == pygame.K_DOWN:
                    main_menu.player_obj.control_y(10)
                if event.key == ord("r"):
                    main_menu.start_solo()
                    
            #Handles the releasing of a key
            if event.type == pygame.KEYUP:
                if event.key == c.space or event.key == c.up or event.key == c.up2:
                    if main_menu.player_obj.on_platform == True:
                        main_menu.player_obj.update()
                        main_menu.player_obj.control_y(-15*main_menu.player_obj.jump_charge - main_menu.player_obj.jump_charge_increase*8)
                        main_menu.player_obj.player_speed = 10
                        main_menu.player_obj.jump_charge = 0
                        main_menu.player_obj.charging = False
                        main_menu.player_obj.on_platform = False
                if event.key == c.left or event.key == pygame.K_LEFT:
                    main_menu.player_obj.control_x(0)
                if event.key == c.right or event.key == pygame.K_RIGHT:
                    main_menu.player_obj.control_x(0)
                if event.key == c.down or event.key == pygame.K_DOWN:
                    main_menu.player_obj.control_y(0)
        
        #Sets screen boundaries and whether the player is on the floor or on a wall
        if main_menu.player_obj.x >= c.screen_width - main_menu.player_obj.player_width:
            main_menu.player_obj.x = c.screen_width - main_menu.player_obj.player_width
        if main_menu.player_obj.x <= 0:
            main_menu.player_obj.x = 0
                    
        #Print framerate in the window caption
        pygame.display.set_caption("Skybound     FPS: {0:.0f}".format(c.clock.get_fps()))

            
        #Updates the display and increments the timers accordingly
        pygame.display.update()
        c.second_timer += 1
        
    pygame.display.quit()
