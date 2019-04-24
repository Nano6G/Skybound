import sys
import pygame
import time
import random
import consts as c
import levels as l
import game_over
import main_menu

class Player():
    def __init__(self):
        self.movex = 0
        self.movey = 0
        self.x = 0
        self.y = c.screen_height-80
        self.on_wall = False
        self.on_platform = False
        self.on_wall_value = 0
        self.charging = False
        self.pressing_down = False
        self.jump_charge = 0
        self.player_width = 50
        self.player_height = 80
        self.player_speed = 10
        self.jump_charge_increase = 0
        self.rect = pygame.Rect(self.x, self.y, self.player_width, self.player_height)
    #Control x/y functions for the player to apply velocity with user input
    def control_x(self, direction):
        self.movex = self.player_speed*direction
    def control_y(self, y):
        self.movey = y
    def draw(self, colour):
        #Self explanatory draw function for the player with methods to change player width and height according to the current jump charge
        height_decrease = (self.player_height*self.jump_charge)/2
        width_increase = (self.player_width*self.jump_charge)
        pygame.draw.rect(c.screen, colour, [self.x-width_increase/2, self.y-c.cameraY+height_decrease, self.player_width+width_increase, self.player_height-height_decrease], 0)
    def update(self):
        #Update function handles collisions between the player and the platforms as well as the charging of the player jump
        self.x += self.movex
        for level in c.levels:
            for platform in level.platforms:
                if self.rect.colliderect(platform.get_rect_2()):
                    platform_rect = platform.get_rect_2()
                    if self.movex > 0:
                        self.x = platform_rect.left - self.player_width
                        self.rect.right = platform_rect.left
                        self.movex = 0
                        
                    if self.movex < 0:
                        self.x = platform_rect.right
                        self.rect.left = platform_rect.right
                        self.movex = 0
                    
        self.y += self.movey
        for level in c.levels:
            for platform in level.platforms:
                if self.rect.colliderect(platform.get_rect_1()):
                    platform_rect = platform.get_rect_1()
                    if self.movey > 0 and self.rect.bottom > platform_rect.top:
                        self.on_platform = True
                        self.y = platform_rect.top - self.player_height
                        self.rect.bottom = platform_rect.top
                        self.movey = 0
                        
                    if self.movey < 0 and self.on_platform == False:
                        self.y = platform_rect.bottom
                        self.rect.top = platform_rect.bottom
                        self.movey = 0
                if self.pressing_down == True:
                    self.rect.bottom = platform.get_rect_1().top
        if self.rect.colliderect(l.floor.get_rect_1()):
            floor_rect = l.floor.get_rect_1()
            if self.movey > 0:
                        self.on_platform = True
                        self.y = floor_rect.top - self.player_height
                        self.rect.bottom = floor_rect.top
                        self.movey = 0
                    
        self.rect.x = self.x
        self.rect.y = self.y
        if self.charging and self.jump_charge <= 1:
            self.jump_charge += 0.05 + self.jump_charge_increase
        if self.jump_charge > 1:
            self.jump_charge = 1
