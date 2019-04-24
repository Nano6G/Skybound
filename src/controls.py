import sys
import pygame
import time
import random
import os
import consts as c
import main_menu

on_controls = False
def show_controls():
    #Sets the title text for this UI page
    help_text = "Help"
    help_text_render = c.menu_font.render(help_text, 1, c.red, 150)
    #Sets the help text
    controls_text = "Controls:\nMenus:\nEsc --- Return\n1/2/3/4 --- Menu Buttons\nEnter --- Submit Name\n\nIn-Game:\nClassic:\nEsc --- Pause\nR --- Restart\nW/Up --- Charge Jump\nA/Left --- Move Left\nS/Down --- Move Down Faster\nD/Right --- Move Right\n\nPractice:\nPage Up --- Increase Score\nPage Down --- Decrease Score\n\nVersus:\nWASD --- BLUE player\nArrow Keys --- RED player"
    gamemodes_text = "Gamemodes:\n\nClassic: As per the title, the original experience of Skybound, charge your jumps and aim for that top spot on the leaderboard.\n\nPractice: The testing grounds for Skybound, feel free to set your score to whatever you want to see how well you can do with a fast camera.\n\nVersus: The local multiplayer gamemode to go head to head against your friends, see who can survive the longest."
    global on_controls
    while on_controls:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    c.screen.fill(c.black)
                    on_controls = False
            if event.type == pygame.display.quit:
                main_menu.quit_game()
                
        c.screen.fill(c.black)

        help_text_rect = help_text_render.get_rect()
        help_text_rect.center = (c.screen_width/2, 50)
        c.screen.blit(help_text_render, help_text_rect)
        
        c.blit_multiline_text(c.screen, controls_text, (30, 50), c.all_help_font)
        c.blit_multiline_text(c.screen, gamemodes_text, (400, c.screen_height/6), c.all_help_font)
        

        
        main_menu.button("Return", 0, c.screen_height-75, 200, 80, c.blue, c.darker_blue, "return")
        pygame.display.update()
    c.screen.fill(c.black)
