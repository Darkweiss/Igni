import pygame

class player:
    def __init__(self,game,pos,size):
        self.game = game
        self.pos = list(pos)
        self.size = size
        self.velocity = [0,0]
        #self.square =  pygame.Rect(self.pos[0],self.pos[1],self.size[0],self.size[1])
        self.jump = False
        self.air_time = 0
        self.resolution = game.resolution
        self.bounces = 100
        self.charges = 1
    def render(self,surf):
        pygame.draw.rect(surf,(0,255,0),self.rect())
    def update(self,tilemap,movement=(0,0)):        
        self.collisions = {'up': False, 'down': False,'right': False,'left': False}
        self.frame_movement = (movement[0] + self.velocity[0],movement[1] + self.velocity[1])       
        self.pos[0] += self.frame_movement[0]
        
        entity_rect = self.rect()
        for rect in tilemap.physics_rects_around(self.pos):
            if entity_rect.colliderect(rect):
                if self.frame_movement[0] > 0:
                    entity_rect.right = rect.left
                    self.collisions['right'] = True
                    self.velocity[0] = 0
                if self.frame_movement[0] < 0:
                    entity_rect.left = rect.right
                    self.collisions['left'] = True
                    self.velocity[0] = 0
                self.pos[0] = entity_rect.x
        
        self.pos[1] += self.frame_movement[1]
        entity_rect = self.rect()
        for rect in tilemap.physics_rects_around(self.pos):
            if entity_rect.colliderect(rect):
                if self.frame_movement[1] > 0:
                    entity_rect.bottom = rect.top
                    self.collisions['down'] = True
                    print('here')
                if self.frame_movement[1] < 0:
                    entity_rect.top = rect.bottom
                    self.collisions['up'] = True
                self.pos[1] = entity_rect.y
        if self.pos[0]<=0:
            self.velocity[0] = -self.velocity[0]
        if self.pos[0] + self.size[0]>self.resolution[0]:
            self.velocity[0] = -self.velocity[0]
        
        self.velocity[1] = min(5,self.velocity[1] + 0.1)
                
        if self.collisions['down'] or self.collisions['up']:
            self.velocity[1] = 0
        if self.collisions['down']:
            self.air_time = 0
            self.jumps = 1
        if self.collisions['down']:
            if self.velocity[0] >0:
                self.velocity[0] = max(self.velocity[0] - 0.5,0)
            else:
                self.velocity[0] = min(self.velocity[0] + 0.5,0)
    def rect(self):
        return  pygame.Rect(self.pos[0],self.pos[1],self.size[0],self.size[1])
    def jump_up(self):
        self.velocity[1] =-5
        self.charges = max(0,self.charges-1)