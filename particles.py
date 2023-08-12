import pygame
class Particle:
    def __init__(self,size):        
        self.size = size
    def render(self,game,offset):
        smaller = 1
        for i in range(len(game.player.pos_history)):            
            pygame.draw.circle(game.display,(255,0,0),[game.player.pos_history[i][0],game.player.pos_history[i][1]-offset],smaller)
            smaller += 1