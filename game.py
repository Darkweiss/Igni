import sys
import pygame
import random
from player import player
class game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Igni')
        self.screen = pygame.display.set_mode((640,480))
        self.display = pygame.Surface((640,480))
        self.display.fill((0,0,0))
        self.clock = pygame.time.Clock()
        self.line = False
        self.player = player(self,[50,50],[50,50])
    def run(self):
        while True:
            test = self.player.rect()
            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                        
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            if self.line == False:
                                self.line_star = mpos = pygame.mouse.get_pos()
                                print('selected')
                    if event.type == pygame.MOUSEBUTTONUP:
                        if self.line == False:
                            if event.button == 1:
                                self.line_end = mpos = pygame.mouse.get_pos()
                                self.line = True
                                print('drawn')
                        if event.button == 3:
                            print('set to false')
                            self.line = False
                            print(self.line)
            self.display.fill((0,0,0))             
            #print(self.line)
            if self.line == True:
                pygame.draw.line(self.display, (255, 0, 0), self.line_star, self.line_end,10)
                #print('here')
            #print(self.line)
            self.player.update((0,0))
            self.player.render(self.display)
            self.screen.blit(self.display,(0,0))
            pygame.display.update() 
            self.clock.tick(60)
game().run()