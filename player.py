import pygame
import math



class player:
    def __init__(self,game,pos,size):
        
        pygame.font.init()
        self.my_font = pygame.font.SysFont('Comic Sans MS', 20)
        self.game = game
        self.pos = list(pos)
        self.size = size
        self.velocity = [0,0]
        self.jump = False
        self.air_time = 0
        self.resolution = game.resolution
        self.bounces = 100
        self.charges = 1
        self.pos_history = []
        self.lv_height = game.lv_height
        self.camera = 0
        self.action = ''
        self.type = 'Igni'
    def render(self,surf,offset):
        pygame.draw.rect(surf,(0,255,0),self.rect_draw(offset))
        text_surface = self.my_font.render(str(self.charges), False, (255, 0, 0))
        surf.blit(text_surface, (1,100))
        #surf.blit(self.animation.img(), (self.pos[0],self.pos[1] - offset))
    def update(self,tilemap,offset,movement=(0,0)):
        self.set_action('idle')  
        self.collisions = {'up': False, 'down': False,'right': False,'left': False}
        self.frame_movement = (movement[0] + self.velocity[0],movement[1] + self.velocity[1])  
             
        self.pos[0] += self.frame_movement[0]
        entity_rect = self.rect_real_coord()
        for rect in tilemap.physics_rects_around(self.pos):
            if entity_rect.colliderect(rect):
                if self.frame_movement[0] > 0:
                    entity_rect.right = rect.left
                    self.collisions['right'] = True
                    self.velocity[0] = -self.velocity[0]*0.5
                if self.frame_movement[0] < 0:
                    entity_rect.left = rect.right
                    self.collisions['left'] = True
                    self.velocity[0] = -self.velocity[0]*0.5
                self.pos[0] = entity_rect.x
        
        self.pos[1] += self.frame_movement[1]
        entity_rect = self.rect_real_coord()
        #print(entity_rect.bottom)
        
        for rect in tilemap.physics_rects_around(self.pos):
            if entity_rect.colliderect(rect):
                if self.frame_movement[1] > 0:
                    entity_rect.bottom = rect.top# + (self.size[1] - rect.size[1])
                    self.collisions['down'] = True
                if self.frame_movement[1] < 0:
                    entity_rect.top = rect.bottom
                    self.collisions['up'] = True
                self.pos[1] = entity_rect.y
        if self.pos[0]<=0 or self.pos[0] + self.size[0]>self.resolution[0]:
            self.velocity[0] = -self.velocity[0]
        self.camera = (self.pos[1])//self.lv_height
        self.pos_history.append(self.rect_real_coord().center)
        if len(self.pos_history)>10:
            self.pos_history.pop(0)
        
        self.velocity[1] = min(5,self.velocity[1] + 0.1)
                
        if self.collisions['down'] or self.collisions['up']:
            self.velocity[1] = 0
        if self.collisions['down']:
            self.air_time = 0
            self.charges = 1
        if self.collisions['down']:
            if self.velocity[0] >0:
                self.velocity[0] = max(self.velocity[0] * 0.5,0)
            else:
                self.velocity[0] = min(self.velocity[0] * 0.5,0)
            self.game.platform_bounce.charges = 1
        else :
            self.air_time += 1
        self.animation.update()
    def rect_draw(self,offset):
        return  pygame.Rect(self.pos[0],int(self.pos[1] - offset),self.size[0],self.size[1])
    def rect_real_coord(self):
        return pygame.Rect(self.pos[0],self.pos[1],self.size[0],self.size[1])
    def jump_up(self):
        self.velocity[1] =-5
        self.charges = max(0,self.charges-1)
    def move(self,vel):
        self.velocity[0] =vel
    def set_action(self,action):
        if action != self.action:
            self.action = action
            self.animation = self.game.assets[self.type + '/' + self.action].copy()