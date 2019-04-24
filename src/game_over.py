import sys
import pygame
import time
import random
import os
import consts as c
import main_menu

removing_timer = 1
removing_timer_max = 20
removing = False

submitted = False


over = False
def game_over(submitted):
    pygame.display.set_caption("Skybound")
    global over
    removing_timer = 1
    removing_timer_max = 60
    removing = False
    while over:
        c.clock.tick(60)
        c.screen.fill(c.black)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                main_menu.quit_game()
            if event.type == pygame.KEYDOWN:
                #If the user presses enter and hasn't submitted their name to the leaderboard yet, that happens
                if event.key == pygame.K_RETURN and submitted == False:
                    main_menu.submit_to_leaderboard(c.score)
                    game_over(True)
                #Backspace to remove characters from the name
                if event.key == pygame.K_BACKSPACE:
                    removing_timer = removing_timer_max
                    removing = True
                if len(c.name) < 15 and submitted == False:
                    c.name += event.unicode
                if event.key == pygame.K_ESCAPE:
                    over = False
                    c.screen.fill(c.black)
                    time.sleep(0.1)
                    main_menu.menu()
                if event.key == pygame.K_2:
                    if submitted:
                        over = False
                        c.screen.fill(c.black)
                        time.sleep(0.1)
                        main_menu.menu()
                if event.key == pygame.K_1 or event.key == pygame.K_r:
                    if submitted:
                        main_menu.start_solo()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_BACKSPACE:
                    removing = False
        
        if removing and removing_timer % removing_timer_max == 0:
            c.name = c.name[:-1]
        
        over_text = "Game Over"
        over_text_render = c.menu_font.render(over_text, 1, c.red, 150)
        over_text_rect = over_text_render.get_rect()
        over_text_rect.center = ((c.screen_width/2, 50))
        c.screen.blit(over_text_render, over_text_rect)

        score_text = "Final Score:{0:.0f}".format(c.score)
        scoretext_render = c.final_score_font.render(score_text, 1, c.white, 150)
        scoretext_rect = scoretext_render.get_rect()
        scoretext_rect.center = c.screen_width/2, c.screen_height/2-200 
        c.screen.blit(scoretext_render, scoretext_rect)

        name_text = ("Name: " + c.name)
        name_text_render = c.controls_font.render(name_text, 1, c.white, 150)
        name_text_rect = name_text_render.get_rect()
        name_text_rect.center = ((c.screen_width/2, c.screen_height/2-100))
        c.screen.blit(name_text_render, name_text_rect)

        if submitted:
            submitted_text_render = c.boxfont.render("Name and Score Submitted to Leaderboard", 1, c.white, 150)
            submitted_text_rect = submitted_text_render.get_rect()
            submitted_text_rect.center = (c.screen_width/2, (c.screen_height/2)-25)
            c.screen.blit(submitted_text_render, submitted_text_rect)
        else:
            main_menu.button("Submit", c.screen_width/2-90, c.screen_height/2-50, 180, 100, c.blue, c.darker_blue, "submit_name")
        
        main_menu.button("Play Again", c.screen_width/2-150, c.screen_height/2+80, 300, 100, c.blue, c.darker_blue, "restart")
        main_menu.button("Exit to Main Menu", c.screen_width/2-150, c.screen_height/2+200, 300, 100, c.blue, c.darker_blue, "return_from_over")
        
        pygame.display.update()

        removing_timer += 1

def vs_over(colour_of_winner, submitted):
    pygame.display.set_caption("Skybound")
    over = True
    removing_timer = 1
    removing_timer_max = 60
    removing = False
    while over:
        c.clock.tick(60)
        c.screen.fill(c.black)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                main_menu.quit_game()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and submitted == False:
                    main_menu.submit_to_leaderboard(c.winner_score)
                    vs_over(c.colour_of_winner, True)
                if event.key == pygame.K_BACKSPACE:
                    removing_timer = removing_timer_max
                    removing = True
                if len(c.name) < 15 and submitted == False:
                    c.name += event.unicode
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_2:
                    game_over.over = False
                    c.screen.fill(c.black)
                    time.sleep(0.1)
                    main_menu.menu()
                if event.key == pygame.K_1 or event.key == pygame.K_r:
                    if submitted:
                        main_menu.start_vs()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_BACKSPACE:
                    removing = False
        
        if removing and removing_timer % removing_timer_max == 0:
            c.name = c.name[:-1]

        c.colour_of_winner = colour_of_winner

        if colour_of_winner == "Red":
            winner_text_colour = c.red
            loser_text_colour = c.blue
            c.winner_score = c.score
            loser_score = c.score2
            colour_of_loser = "Blue"
        elif colour_of_winner == "Blue":
            winner_text_colour = c.blue
            loser_text_colour = c.red
            c.winner_score = c.score2
            loser_score = c.score
            colour_of_loser = "Red"
        else:
            winner_text_colour = c.red
            c.winner_score = 10
            loser_score = 5
            colour_of_loser = "Green"

        score_text = "{}'s Score:{}".format(colour_of_winner, round(c.winner_score))
        scoretext_render = c.score_font.render(score_text, 1, winner_text_colour, 150)
        scoretext_rect = scoretext_render.get_rect()
        scoretext_rect.center = 625, c.screen_height/2-220 
        c.screen.blit(scoretext_render, scoretext_rect)

        score_text2 = "{}'s Score:{}".format(colour_of_loser, round(loser_score))
        scoretext_render2 = c.score_font.render(score_text2, 1, loser_text_colour, 150)
        scoretext_rect2 = scoretext_render2.get_rect()
        scoretext_rect2.center = 625, c.screen_height/2-170
        c.screen.blit(scoretext_render2, scoretext_rect2)
            
        over_text = "{} Player Wins".format(colour_of_winner)
        over_text_render = c.menu_font.render(over_text, 1, winner_text_colour, 150)
        over_text_rect = over_text_render.get_rect()
        over_text_rect.center = ((c.screen_width/2, (c.screen_height/3)-180))
        c.screen.blit(over_text_render, over_text_rect)

        name_text = ("Name: " + c.name)
        name_text_render = c.controls_font.render(name_text, 1, c.white, 150)
        name_text_rect = name_text_render.get_rect()
        name_text_rect.center = ((c.screen_width/2, c.screen_height/2-100))
        c.screen.blit(name_text_render, name_text_rect)

        if submitted:
            submitted_text_render = c.boxfont.render("Name and Score Submitted to Leaderboard", 1, c.white, 150)
            submitted_text_rect = submitted_text_render.get_rect()
            submitted_text_rect.center = (c.screen_width/2, (c.screen_height/2))
            c.screen.blit(submitted_text_render, submitted_text_rect)
        else:
            main_menu.button("Submit", c.screen_width/2-90, c.screen_height/2-50, 180, 100, c.blue, c.darker_blue, "submit_name_vs")
        
        main_menu.button("Play Again", c.screen_width/2-150, 400, 300, 100, c.blue, c.darker_blue, "restart_vs")
        main_menu.button("Exit to Main Menu", c.screen_width/2-150, 525, 300, 100, c.blue, c.darker_blue, "return_from_over")
        
        pygame.display.update()
        removing_timer += 1
