import pygame
class Particle:
    def __init__(self,size,particle_offset):        
        self.size = size
        self.particle_offset = particle_offset
    def render(self,game,offset,):
        smaller = 1
        for i in range(len(game.player.pos_history)):            
            pygame.draw.circle(game.display,(255,0,0),[game.player.pos_history[i][0] +  self.particle_offset[0],game.player.pos_history[i][1]-offset +  self.particle_offset[1]],smaller)
            smaller += 1