import pygame
import numpy as np
class Platform:
    def __init__(self,game):
        self.rect = pygame.draw.line(game.display, (255, 0, 0), game.line_star, game.line_end,10)
    def bounce(self,game):        
        temp1x,temp1y = game.line_star
        temp2x,temp2y = game.line_end
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
        midpointx = (pt1x + pt2x)/2
        midpointy = (pt1y + pt2y)/2
        slope = (pt2y-pt1y)/(pt2x-pt1x)
        
        if slope==0:
            bnc_slope = 0
        else:                
            bnc_slope = -1/slope
        interc = midpointy - bnc_slope*midpointx
        pygame.draw.line(game.display, (0, 255, 0), (midpointx,midpointy), (pt2x,pt2x*bnc_slope+interc),10)
        vec_norm = [pt2x-midpointx, (pt2x*bnc_slope+interc)-midpointy]
        vec_norm = vec_norm/np.linalg.norm(vec_norm)
        vec_pl = - (game.player.velocity/np.linalg.norm(game.player.velocity))
        pygame.draw.line(game.display, (255, 255, 0), game.player.rect().center, (game.player.rect().center[0]+int(vec_pl[0]),game.player.rect().center[1]+int(vec_pl[1])),10)
        u = (np.dot(vec_pl,vec_norm)/np.dot(vec_norm,vec_norm)*vec_norm)
        w = vec_norm-u
        print (np.linalg.norm(vec_norm))
        new_vel = (w+u)*10
        pygame.draw.line(game.display, (255, 255, 0), game.player.rect().center, (game.player.rect().center[0]+int(vec_pl[0]),game.player.rect().center[1]+int(vec_pl[1])),10)
        game.player.velocity[0] = new_vel[0]
        game.player.velocity[1] = new_vel[1]
        game.player.bounces -= 1