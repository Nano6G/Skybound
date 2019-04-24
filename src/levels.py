import sys
import pygame
import time
import random
import os
import consts as c
import main_menu
import player

class Platform():
    def __init__(self, x, y, width, height):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.colour = (random.randint(10,255), random.randint(10,255), random.randint(10,255))
    def draw(self):
        pygame.draw.rect(c.screen, self.colour, [self.x, self.y-c.cameraY, self.width, self.height], 0)
    def get_rect_1(self):
        return pygame.Rect(self.x+1, self.y+1, self.width-20, self.height-0.1)
    def get_rect_2(self):
        return pygame.Rect(self.x-1, self.y+10, self.width+1, 0)

class Level:
    def __init__(self, platforms, offset, axis):
        self.platforms = [Platform(p.x, p.y-offset, p.width, p.height) for p in platforms]
        if axis == "y":
            self.offset = -offset
        elif axis == "x":
            self.offset = offset
        
    def draw(self):
        for platform in self.platforms:
            platform.draw()

floor = Platform(0, 650, 1280, 300)
floor.colour = c.black

#650 = floor, 0 = roof
#0 = left, 1200 = right
#1st set of platforms
p_1 = Platform(300, 450, 200, 20)
p_2 = Platform(900, 500, 200, 20)
p_3 = Platform(0, 300, 200, 20)
p_4 = Platform(450, 225, 200, 20)
p_5 = Platform(500, 650, 200, 20)
p_6 = Platform(1000, 300, 200, 20)
platforms_1 = [p_1, p_2, p_3, p_4, p_5, p_6]

#2nd set of platforms
p2_1 = Platform(1000, 600, 200, 20)
p2_2 = Platform(500, 650, 200, 20)
p2_3 = Platform(100, 200, 200, 20)
p2_4 = Platform(450, 400, 200, 20)
p2_5 = Platform(900, 200, 200, 20)
platforms_2 = [p2_1, p2_2, p2_3, p2_4, p2_5]
