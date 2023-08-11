import sys
import pygame
import random
from player import player
from plat import Platform
from utils import load_image,load_images
from tilemap import Tilemap
import numpy as np


class game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Igni')
        self.resolution = (500,800)
        self.screen = pygame.display.set_mode(self.resolution)
        self.display = pygame.Surface(self.resolution)
        self.display.fill((0,0,0))
        self.clock = pygame.time.Clock()
        self.line = False
        self.player = player(self,[10,780],[16,16])
        
        self.assets = {
        'Fire': load_images('Tiles/FireTiles'),
        }
        self.tilemap = Tilemap(self,tile_size=16)
        self.tilemap.load('map.json')
    
    def run(self):
        while True:
            self.display.fill((0,0,0))
            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            if self.line == False:
                                self.line_star = mpos = pygame.mouse.get_pos()
                                print('selected')
                    if event.type == pygame.MOUSEBUTTONUP:
                        if self.line == False:
                            if event.button == 1:
                                self.line_end = mpos = pygame.mouse.get_pos()
                                self.line = True
                                print('drawn')
                        if event.button == 3:
                            print('set to false')
                            self.line = False
                            self.player.jump = False
                            print(self.line)
                    if event.type == pygame.KEYDOWN:
                        if event.key ==pygame.K_SPACE:
                            self.player.jump_up()
                            print('jump')
            self.tilemap.render(self.display)

            if self.line == False:
                self.player.update(self.tilemap,(0,0))
            else:
                self.platform = Platform(self) #draw line                                                            
                #check for bounce
                if self.player.rect().clipline(self.line_star,self.line_end) and self.player.bounces>0 and self.player.jump == False:
                    self.platform.bounce(self)
                    self.player.jump = True
                    self.player.update(self.tilemap,(0,0))
                else:
                    self.player.update(self.tilemap,(0,0))
            
            self.player.render(self.display)
            self.screen.blit(self.display,(0,0))
            pygame.display.update() 
            self.clock.tick(60)
game().run()