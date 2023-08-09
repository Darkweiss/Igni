import sys
import pygame
import random
from player import player
from plat import Platform
import numpy as np
class game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Igni')
        self.screen = pygame.display.set_mode((1280,500))
        self.display = pygame.Surface((1280,500))
        self.display.fill((0,0,0))
        self.clock = pygame.time.Clock()
        self.line = False
        self.player = player(self,[500,50],[50,50])
    def run(self):
        while True:
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
                            print(self.line)
            self.display.fill((0,0,0))             
            #draw line
            if self.line == False:
                self.player.update((0,0))
            else:
                self.platform = Platform(self)                                                                
                temp1x,temp1y = self.platform.plat_coords(self)[0]
                temp2x,temp2y = self.platform.plat_coords(self)[1]
                #make the point closest to the y axis the first one
                if temp1y>=temp2y:
                    pt1x = temp2x
                    pt1y = temp2y
                    pt2x = temp1x
                    pt2y = temp1y                    
                else:
                    pt1x = temp1x
                    pt1y = temp1y                
                    pt2x = temp2x
                    pt2y = temp2y
                #Klemi ideja - normalised vectors of platform and object forces - sum them up
                #theta = np.arctan( (pt2y-pt1y)/(pt2x-pt1x))*180/np.pi        
                midpointx = (pt1x + pt2x)/2
                midpointy = (pt1y + pt2y)/2
                slope = (pt2y-pt1y)/(pt2x-pt1x)
                bnc_slope = -1/slope
                interc = midpointy - bnc_slope*midpointx
                pygame.draw.line(self.display, (0, 255, 0), (midpointx,midpointy), (pt2x,pt2x*bnc_slope+interc),10)
                vec_norm = [pt2x-midpointx, (pt2x*bnc_slope+interc)-midpointy]
                vec_norm = vec_norm/np.linalg.norm(vec_norm)
                vec_pl = - (self.player.velocity/np.linalg.norm(self.player.velocity))
                pygame.draw.line(self.display, (255, 255, 0), self.player.square.center, (self.player.square.center[0]+int(vec_pl[0]),self.player.square.center[1]+int(vec_pl[1])),10)
                u = (np.dot(vec_pl,vec_norm)/np.dot(vec_norm,vec_norm)*vec_norm)
                w = vec_norm-u
                print (np.linalg.norm(vec_norm))
                new_vel = (w+u)*10
                pygame.draw.line(self.display, (0, 255, 255), self.player.square.center, (self.player.square.center[0]+int(new_vel[0]),self.player.square.center[1]+int(new_vel[1])),10)
                print(new_vel)
                if self.player.square.clipline(self.platform.plat_coords(self)) and self.player.jump==False:
                    pygame.draw.line(self.display, (255, 255, 0), self.player.square.center, (self.player.square.center[0]+int(vec_pl[0]),self.player.square.center[1]+int(vec_pl[1])),10)
                    self.player.velocity[0] = new_vel[0]
                    self.player.velocity[1] = new_vel[1]
                    self.player.jump = True
                else:
                    self.player.update((0,0))
            #print(self.line)
            
            
            
            #check for collision

            self.player.rect()
            
            self.player.render(self.display)
            self.screen.blit(self.display,(0,0))
            pygame.display.update() 
            self.clock.tick(60)
game().run()