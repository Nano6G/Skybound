import main_menu
import os
import pygame

#OS funtion to centre the screen on load
os.environ["SDL_VIDEO_CENTERED"]="1"

#Initialising pygame functions
pygame.init()
pygame.font.init()
pygame.display.init()
pygame.display.set_caption("Skybound")
pygame.display.update()

#Calls menu to function to display the title and buttons
main_menu.menu()
