import pygame

class player:
    def __init__(self,game,pos,size):
        self.game = game
        self.pos = list(pos)
        self.size = size
        self.velocity = [0,0]
        self.square =  pygame.Rect(self.pos[0],self.pos[1],self.size[0],self.size[1])
        self.jump = False
        self.air_time = 0
    def render(self,surf):
        pygame.draw.rect(surf,(0,255,0),self.square)
    def update(self,movement=(0,0)):
        self.collisions = {'up': False, 'down': False,'right': False,'left': False}
        self.frame_movement = (movement[0] + self.velocity[0],movement[1] + self.velocity[1])
        self.velocity[1] = min(5,self.velocity[1] + 0.1)
        
        #if 
        #if abs(self.dashing)==51:
        #    self.velocity[0] *=0.1
        
            
        #if self.velocity[0] >0:
        #    self.velocity[0] = max(self.velocity[0] - 0.1,0)
        #else:
        #    self.velocity[0] = min(self.velocity[0] + 0.1,0)
        
        
        #if abs(self.velocity[0])>0:
        #    self.velocity[0] += (self.velocity[0]/(-self.velocity[0]))*1
        
        self.pos[0] += self.frame_movement[0]
        self.pos[1] += self.frame_movement[1]
    def rect(self):
        self.square =  pygame.Rect(self.pos[0],self.pos[1],self.size[0],self.size[1])