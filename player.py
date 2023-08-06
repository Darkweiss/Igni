import pygame

class player:
    def __init__(self,game,pos,size):
        self.game = game
        self.pos = list(pos)
        self.size = size
        self.velocity = [0,0]
    def render(self,surf):
        pygame.draw.rect(surf,(0,255,0),self.square)
    def update(self,movement=(0,0)):
        self.collisions = {'up': False, 'down': False,'right': False,'left': False}
        frame_movement = (movement[0] + self.velocity[0],movement[1] + self.velocity[1])
        self.velocity[1] = min(5,self.velocity[1] + 0.1)
        self.pos[0] += frame_movement[0]
        self.pos[1] += frame_movement[1]
    def rect(self):
        self.square =  pygame.Rect(self.pos[0],self.pos[1],self.size[0],self.size[1])