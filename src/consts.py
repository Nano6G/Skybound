import sys
import pygame
import time
import os

#Initialising pygame functions
pygame.init()
pygame.font.init()
pygame.display.init()

#OS funtion to centre the screen on load
os.environ["SDL_VIDEO_CENTERED"]="1"
#Display constants
screen_width = 1280
screen_height = 650
#Sets frames per second for the game to run at
fps = 60
#Initialises the pygame screen with preset width and height
screen = pygame.display.set_mode([screen_width,screen_height])
#Creates pygame clock object
clock = pygame.time.Clock()

#Control Constants
left = ord("a")
right = ord("d")
up = ord("w")
up2 = pygame.K_UP
down = ord("s")
space = pygame.K_SPACE

#Main variables and constants
#Gravity to apply to player each frame
gravity = 0.4
#Scores for both classic and versus gamemodes
score = 0
score2 = 0
#Booleans to check whether a game is in progress
playing_solo = False
playing_vs = False
#Name value of the user
name = ''
#List of platforms to add to and to generate
levels = []
#Self-explanatory winner details
colour_of_winner = ''
winner_score = 0

#Camera constant to move platforms down so player is constantly moving upwards
cameraY = 0
#Offset used to generate platforms seperately rather than on top of each other
offset = 0
#Boolean to ensure platforms are only generated within a certain range of the player so the game is not slowed down
generate_platforms = True
level_timer = 0
max_level_timer = 60
#Camera mvoement to change how fast the cameraY variable changes
camera_movement = 0

#Self explanatory colour constants
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 155, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
lighter_blue = (0, 128, 255)
darker_blue = (0, 0, 153)

#Font constants
boxfont = pygame.font.Font("..\\res\\JuliusSansOne.ttf", 28)
score_font = pygame.font.SysFont('Courier New', 40)
final_score_font = pygame.font.SysFont('Courier New', 50)
menu_font = pygame.font.Font("..\\res\\JuliusSansOne.ttf", 70)
controls_font = pygame.font.Font("..\\res\\JuliusSansOne.ttf", 40)
all_help_font = pygame.font.Font("..\\res\\JuliusSansOne.ttf", 20)
leaderboard_font = pygame.font.Font("..\\res\\JuliusSansOne.ttf", 40)


"""Function to blit text on multiple lines.
Function checks if the stack of text can fit in the length of the
screen and once the stack of words exceeds the surface width,
a line break is added. Concept used from https://stackoverflow.com/questions/42014195/rendering-text-with-multiple-lines-in-pygame
"""
def blit_multiline_text(surface, text, pos, font, colour=white):
    words = [word.split(' ') for word in text.splitlines()]
    space = font.size(' ')[0]
    max_width, max_height = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, 0, colour)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]
                y += word_height
            surface.blit(word_surface, (x,y))
            x += word_width + space
        x = pos[0]
        y += word_height
        
