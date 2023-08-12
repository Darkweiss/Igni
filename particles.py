import pygame
class Particle:
    def __init__(self,size):        
        self.size = size
    def render(self,game):
        smaller = 1
        for i in range(len(game.player.pos_history)):            
            pygame.draw.circle(game.display,(255,0,0),game.player.pos_history[i],smaller)
            smaller += 1