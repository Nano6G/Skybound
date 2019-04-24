import sys
import pygame
import consts as c
import main_menu


def gamemode():
    gamemode_text = "Gamemode"
    gamemode_text_render = c.menu_font.render(gamemode_text, 1, c.red, 150)
    global show_gamemode
    show_gamemode = True
    pygame.display.set_caption("Skybound")
    while show_gamemode:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                main_menu.quit_game()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    main_menu.show_menu = True
                    main_menu.menu()
                if event.key == pygame.K_1:
                    main_menu.start_solo()
                elif event.key == pygame.K_2:
                    main_menu.start_practice()
                elif event.key == pygame.K_3:
                    main_menu.start_vs()
                
        c.screen.fill(c.black)
        c.clock.tick(c.fps)

        gamemode_text_rect = gamemode_text_render.get_rect()
        gamemode_text_rect.center = (c.screen_width/2, 50)
        c.screen.blit(gamemode_text_render, gamemode_text_rect)
        
        main_menu.button("Classic", (c.screen_width/2)-125, c.screen_height/4.33, main_menu.box_w, main_menu.box_h, c.blue, c.darker_blue, "solo")
        main_menu.button("Practice", (c.screen_width/2)-125, c.screen_height/2.36, main_menu.box_w, main_menu.box_h, c.blue, c.darker_blue, "practice")
        main_menu.button("Versus", (c.screen_width/2)-125, c.screen_height/1.625, main_menu.box_w, main_menu.box_h, c.blue, c.darker_blue, "vs")
        
        main_menu.button("Return", 0, c.screen_height-75, 200, 80, c.blue, c.darker_blue, "return")
        
        pygame.display.update()
    c.screen.fill(c.black)
