import pygame
import time
import consts as c
import pause as p
import game_over
import leaderboard as lb
import player
import vs
import gamemode
import solo
import practice
import controls
import sys

box_w = 250
box_h = 100

player_obj = player.Player()
player_obj2 = player.Player()

#Button function to pass in button variables for displaying on screen
def button(msg, x, y, w, h, c1, c2, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x < mouse[0] and mouse[0] < x+w and y < mouse[1] and mouse[1] < y+h:
        box = pygame.draw.rect(c.screen, c1, (x,y,w,h))
        box.center = ((c.screen_width)/2, y)

        if click[0] == 1 and action != None:
            if action == "play":
                time.sleep(0.15)
                show_menu = False
                gamemode.show_gamemode = True
                gamemode.gamemode()
            elif action == "solo":
                start_solo()
            elif action == "vs":
                start_vs()
            elif action == "restart_vs":
                start_vs()
            elif action == "return_from_game":
                p.is_paused = False
                c.screen.fill(c.black)
                time.sleep(0.25)
                menu()
            elif action == "return_from_over":
                game_over.over = False
                c.screen.fill(c.black)
                time.sleep(0.2)
                show_menu = True
                menu()
            elif action == "quit":
                quit_game()
            elif action == "return":
                lb.show_leaderboard = False
                c.screen.fill(c.black)
                menu()
            elif action == "leaderboard":
                lb.show_leaderboard = True
                lb.leaderboard()
            elif action == "restart":
                start_solo()
            elif action == "restart_practice":
                start_practice()
            elif action == "submit_name":
                submit_to_leaderboard(c.score)
                game_over.game_over(True)
            elif action == "submit_name_vs":
                submit_to_leaderboard(c.winner_score)
                game_over.vs_over(c.colour_of_winner, True)
            elif action == "resume":
                p.is_paused = False
            elif action == "practice":
                start_practice()
            elif action == "controls":
                controls.on_controls = True
                controls.show_controls()

    else:
        box = pygame.draw.rect(c.screen, c2, (x,y,w,h))
        box.center = (((c.screen_width)/2)-x, (c.screen_height)/2-y)

    box_text_render = c.boxfont.render(msg, 1, c.white, 150)
    box_text_rect = box_text_render.get_rect()
    if action != "return" and action != "resume" and action != "restart" and action != "return_from_game" and action != "submit_name" and action != "submit_name_vs" and action != "return" and action != "restart_practice" and action != "restart_vs" and action != "return_from_over":
        box_text_rect.center = (x+125, y+50)
        c.screen.blit(box_text_render, box_text_rect)
    elif action == "return_from_over":
        box_text_rect.center = (x+150, y+50)
        c.screen.blit(box_text_render, box_text_rect)
    elif action == "submit_name" or action == "submit_name_vs":
        box_text_rect.center = (x+90, y+50)
        c.screen.blit(box_text_render, box_text_rect)
    elif action == "return":
        box_text_rect.center = (x+100, y+40)
        c.screen.blit(box_text_render, box_text_rect)
    else:
        box_text_rect.center = (x+155, y+50)
        c.screen.blit(box_text_render, box_text_rect)
        
    
#Menu function to display the main menu with title and buttons
def menu():
    logo = pygame.image.load("..\\res\\logo.png")
    pygame.transform.scale(logo, (600, 80))
    game_over.over = False
    global show_menu
    show_menu = True
    while show_menu:
        for event in pygame.event.get():
            if event.type == pygame.display.quit:
                quit_game()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    time.sleep(0.1)
                    show_menu = False
                    gamemode.show_gamemode = True
                    gamemode.gamemode()
                elif event.key == pygame.K_2:
                    lb.show_leaderboard = True
                    lb.leaderboard()
                elif event.key == pygame.K_3:
                    controls.on_controls = True
                    controls.show_controls()
                elif event.key == pygame.K_4:
                    quit_game()
                
        c.screen.fill(c.black)
        c.clock.tick(c.fps)

        pygame.display.set_caption("Skybound")

        logo_rect = logo.get_rect()
        logo_rect.center = (c.screen_width/2, 50)
        c.screen.blit(logo, logo_rect)

        button("Play", c.screen_width/2-125, 150, box_w, box_h, c.blue, c.darker_blue, "play")
        button("Leaderboard", c.screen_width/2-125, 270, box_w, box_h, c.blue, c.darker_blue, "leaderboard")
        button("Help", c.screen_width/2-125, 390, box_w, box_h, c.blue, c.darker_blue, "controls")
        button("Quit", c.screen_width/2-125, 510, box_w, box_h, c.blue, c.darker_blue, "quit")
        
        pygame.display.update()

#Multiple functions to complete starting/restarting actions for each gamemode
def start_solo():
    time.sleep(0.05)
    c.second_timer = 0
    c.name = ''
    c.levels = []
    c.cameraY = 0
    c.offset = 0
    c.score = 0
    c.generate_platforms = True
    c.level_timer = 0
    c.camera_movement = 0.01
    player_obj = player.Player()
    lb.show_leaderboard = False
    gamemode.show_gamemode = False
    game_over.over = False
    p.is_paused = False
    show_menu = False
    c.screen.fill(c.black)
    solo.solo()
def start_practice():
    time.sleep(0.05)
    c.second_timer = 0
    c.name = ''
    c.levels = []
    c.cameraY = 0
    c.offset = 0
    c.generate_platforms = True
    c.level_timer = 0
    c.camera_movement = 0.01
    player_obj = player.Player()
    player_obj.__init__()
    show_menu = False
    c.playing_gamemode = True
    game_over.over = False
    c.score = 0
    practice.practice()
def start_vs():
    time.sleep(0.05)
    c.second_timer = 0
    c.playing_vs = True
    c.name = ''
    c.levels = []
    c.cameraY = 0
    c.offset = 0
    c.score = 0
    c.score2 = 0
    c.generate_platforms = True
    c.level_timer = 0
    c.camera_movement = 0.01
    player_obj = player.Player()
    player_obj2 = player.Player()
    lb.show_leaderboard = False
    gamemode.show_gamemode = False
    game_over.over = False
    p.is_paused = False
    show_menu = False
    vs.vs()
def submit_to_leaderboard(score):
    leaderboard = open("..\\res\\leaderboard.txt", "a+")
    name_and_score = c.name + " ----- " + str(round(score)) + "\n"
    leaderboard.write(name_and_score)
    leaderboard.close()
def quit_game():
    pygame.display.quit()
    pygame.quit()
    sys.exit()
    
