import sys
import pygame
import time
import random
import os
import consts as c
import pause as p
import leaderboard
import game_over
import main_menu

show_leaderboard = False
def leaderboard():
    global show_leaderboard
    leaderboard = open("..\\res\\leaderboard.txt", "r+")
    while show_leaderboard:
        pygame.display.set_caption("Skybound")
        c.screen.fill(c.black)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                main_menu.quit_game()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    c.screen.fill(c.black)
                    show_leaderboard = False
                    
        leaderboard_text = "Leaderboard"
        leaderboard_text_render = c.menu_font.render(leaderboard_text, 1, c.red, 150)
        leaderboard_text_rect = leaderboard_text_render.get_rect()
        leaderboard_text_rect.center = (c.screen_width/2, 50)
        c.screen.blit(leaderboard_text_render, leaderboard_text_rect)

        lines = [line.rstrip('\n') for line in open('..\\res\\leaderboard.txt')]
        
        lines.sort(key=lambda x: int(x.split("-----")[-1]), reverse=True)
                        
        score_y = 0
        scores = 0
        for name_and_score in lines:
            if scores < 10:
                name = name_and_score.split(" ----- ")
                name = name[0]
                score = name_and_score.split("----- ")
                score = score[1]
                
                name_text_render = c.leaderboard_font.render(name, 1, c.white, 150)
                name_text_rect = name_text_render.get_rect()
                name_text_width = name_text_render.get_width()
                name_text_height = name_text_render.get_height()
                name_text_rect.x = c.screen_width/2-150-name_text_width
                name_text_rect.y = 97.5 + score_y
                c.screen.blit(name_text_render, name_text_rect)

                score_text_render = c.score_font.render(score, 1, c.white, 150)
                score_text_rect = score_text_render.get_rect()
                score_text_rect.center = (c.screen_width/2+200, (120 + score_y))
                c.screen.blit(score_text_render, score_text_rect)

                pygame.draw.line(c.screen, c.white, [c.screen_width/2-125, 122 + score_y], [c.screen_width/2+125, 122 + score_y], 5)
                
                score_y += 50
                scores += 1
            
        main_menu.button("Return", 0, c.screen_height-75, 200, 80, c.blue, c.darker_blue, "return")
        pygame.display.update()
