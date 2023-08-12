import sys
import pygame
import random
from player import player
from plat import Platform
from utils import load_image,load_images
from tilemap import Tilemap
import numpy as np
from particles import Particle

class game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Igni')
        self.resolution = (500,800)
        self.lv_height = 800
        self.screen = pygame.display.set_mode(self.resolution)
        self.display = pygame.Surface(self.resolution)
        self.display.fill((0,0,0))
        self.clock = pygame.time.Clock()
        self.line = False
        self.player = player(self,[10,780],[16,16])
        self.trail = Particle(6)
        self.camera = 0
        self.assets = {
        'Fire': load_images('Tiles/FireTiles'),
        }
        self.tilemap = Tilemap(self,tile_size=16)
        self.tilemap.load('map.json')
        self.platform_bounce = Platform(10)
        self.offset = 0
    def run(self):
        while True:
            self.display.fill((0,0,0))
            self.offset = int((self.player.pos[1]//self.lv_height)*self.lv_height)
            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            if self.line == False:
                                self.line_star = pygame.mouse.get_pos()
                                #self.line_star = (self.line_star[0],self.line_star[1]-self.offset)
                    if event.type == pygame.MOUSEBUTTONUP:
                        if self.line == False:
                            if event.button == 1:
                                self.line_end = pygame.mouse.get_pos()
                                #self.line_end = (self.line_end[0],self.line_end[1]-self.offset)
                                self.line = True
                        if event.button == 3:
                            self.line = False
                            
                    if event.type == pygame.KEYDOWN:
                        if event.key ==pygame.K_SPACE:
                            self.player.jump_up()
            self.tilemap.render(self.display,(0,int(self.offset)))
            if self.line == False:
                self.player.update(self.tilemap,self.offset,(0,0))
            else:
                self.platform_bounce.draw(self.display,self.line_star,self.line_end) #draw line                                                            
                #check for bounce
                if self.player.rect_draw(self.offset).clipline(self.line_star,self.line_end) and self.player.bounces>0:
                    self.platform_bounce.bounce(self.player,self.display)
                    self.player.jump = True
                    self.player.update(self.tilemap,self.offset,(0,0))
                    self.line = False
                    self.player.jump = False
                else:
                    self.player.update(self.tilemap,self.offset,(0,0))
            self.trail.render(self,self.offset)    
            self.player.render(self.display,self.offset) 
            self.screen.blit(self.display,(0,0))
            pygame.display.update() 
            self.clock.tick(60)
game().run()