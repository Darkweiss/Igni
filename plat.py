import pygame
class Platform:
    def __init__(self,game):
        self.rect = pygame.draw.line(game.display, (255, 0, 0), game.line_star, game.line_end,10)
    
    def plat_coords(self,game):
        return (game.line_star,game.line_end)