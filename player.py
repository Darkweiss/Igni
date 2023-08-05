import pygame

class player:
    def __init__(self,game,pos,size):
        self.game = game
        self.pos = list(pos)
        self.size = size
    def rect(self):
        self.square =  pygame.Rect(self.pos[0],self.pos[1],self.size[0],self.size[1])
    def render(self,surf):
        pygame.draw.rect(surf,(0,255,0),self.square)