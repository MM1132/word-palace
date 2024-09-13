import pygame

class Text:
    def __init__(self, screen, text, pos, font_size):
        self.screen = screen
        self.pos = pos
        self.font = pygame.font.SysFont(pygame.font.get_fonts()[0], font_size)
        self.hover = False
        
        self.set_text(text)
    
    def set_text(self, text):
        self.text_surface = self.font.render(text, True, (255, 255, 255))

        self.rect = self.text_surface.get_rect()
        self.rect.x = self.pos[0] - self.rect.center[0]
        self.rect.y = self.pos[1] - self.rect.center[1]
    
    def update(self, mouse_pos):
        self.hover = self.rect.collidepoint(mouse_pos)

    def render(self):
        self.screen.blit(self.text_surface, self.rect)
    
    def click(self):
        return self.hover
