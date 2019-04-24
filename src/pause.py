import sys
import pygame
import time
import random
import os
import consts as c
import main_menu


is_paused = False
def paused(gamemode):
    paused_text = "Paused"
    paused_text_render = c.menu_font.render(paused_text, 1, c.white, 150)
    pygame.display.set_caption("Skybound")
    global is_paused
    while is_paused:
        for event in pygame.event.get():
            if event.type == pygame.display.quit:
                main_menu.quit_game()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    is_paused = False
                if event.key == pygame.K_1:
                    is_paused = False
                elif event.key == pygame.K_2:
                    if gamemode == "practice":
                        main_menu.start_practice()
                    elif gamemode == "solo":
                        main_menu.start_solo()
                elif event.key == pygame.K_3:
                    is_paused = False
                    c.screen.fill(c.black)
                    time.sleep(0.05)
                    main_menu.menu()
        
        paused_text_rect = paused_text_render.get_rect()
        paused_text_rect.center = ((c.screen_width/2, (c.screen_height/3)/2))
        c.screen.blit(paused_text_render, paused_text_rect)

        main_menu.button("Resume", c.screen_width/2-155, c.screen_height/3.25, 310, 100, c.blue, c.darker_blue, "resume")
        if gamemode == "practice":
            main_menu.button("Restart", c.screen_width/2-155, c.screen_height/1.86, 310, 100, c.blue, c.darker_blue, "restart_practice")
        elif gamemode == "solo":
            main_menu.button("Restart", c.screen_width/2-155, c.screen_height/1.86, 310, 100, c.blue, c.darker_blue, "restart")
        main_menu.button("Exit to Main Menu", c.screen_width/2-155, c.screen_height/1.3, 310, 100, c.blue, c.darker_blue, "return_from_game")

        pygame.display.update()
    c.screen.fill(c.black)

def paused_vs():
    paused_text = "Paused"
    paused_text_render = c.menu_font.render(paused_text, 1, c.white, 150)
    pygame.display.set_caption("Skybound")
    global is_paused
    while is_paused:
        for event in pygame.event.get():
            if event.type == pygame.display.quit:
                main_menu.quit_game()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    is_paused = False
                if event.key == pygame.K_1:
                    is_paused = False
                elif event.key == pygame.K_2:
                    is_paused = False
                    c.screen.fill(c.black)
                    time.sleep(0.05)
                    main_menu.menu()
                    
        paused_text_rect = paused_text_render.get_rect()
        paused_text_rect.center = ((c.screen_width/2, (c.screen_height/3)/2))
        c.screen.blit(paused_text_render, paused_text_rect)

        main_menu.button("Resume", c.screen_width/2-155, c.screen_height/2.6, 310, 100, c.blue, c.darker_blue, "resume")
        main_menu.button("Exit to Main Menu", c.screen_width/2-155, c.screen_height/1.625, 310, 100, c.blue, c.darker_blue, "return_from_game")

        pygame.display.update()
    c.screen.fill(c.black)
