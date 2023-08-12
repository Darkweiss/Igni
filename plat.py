import pygame
import numpy as np
class Platform:
    def __init__(self,coeff):
        self.coeff = coeff
    def draw(self,surf,start,ending):
        self.start = start
        self.ending = ending
        self.rect = pygame.draw.line(surf, (255, 0, 0), start, ending,10)

    def bounce(self,player,surf):        
        temp1x,temp1y = self.start
        temp2x,temp2y = self.ending
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
        
        if (pt2x-pt1x) == 0:
            slope = (pt2y-pt1y)/0.0001
        else:
            slope = (pt2y-pt1y)/(pt2x-pt1x)
        
        if slope==0:
            bnc_slope = 0
        else:                
            bnc_slope = -1/slope
        interc = midpointy - bnc_slope*midpointx
        #need to check if the player is contacting the line from one side or the other 
        #top = pygame.draw.line(game.display, (0, 255, 0), (midpointx,midpointy), (pt2x,pt2x*bnc_slope+interc),1)
        #bottom = pygame.draw.line(game.display, (0, 255, 0), (midpointx,midpointy), (pt2x,pt2x*bnc_slope+interc),1)
        vec_norm = [(pt2x-midpointx), ((pt2x*bnc_slope+interc)-midpointy)]
        vec_norm = vec_norm/np.linalg.norm(vec_norm)
        vec_pl =  (player.velocity/np.linalg.norm(player.velocity))
        pygame.draw.line(surf, (255, 255, 0), player.rect().center, (player.rect().center[0]+int(vec_pl[0]),player.rect().center[1]+int(vec_pl[1])),10)
        u = (np.dot(vec_pl,vec_norm)/np.dot(vec_norm,vec_norm)*vec_norm)
        if (np.dot(vec_pl,vec_norm))<=0:
            w = vec_norm-u
        else:
            w = -vec_norm-u
        
        print (np.linalg.norm(vec_norm))
        new_vel = (w+u)*self.coeff
        pygame.draw.line(surf, (255, 255, 0), player.rect().center, (player.rect().center[0]+int(vec_pl[0]),player.rect().center[1]+int(vec_pl[1])),10)
        player.velocity[0] = new_vel[0]
        player.velocity[1] = new_vel[1]
        player.bounces -= 1