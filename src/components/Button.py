import pygame

class Button:
    FONT = pygame.font.SysFont(pygame.font.get_fonts()[0], 48)

    def __init__(self, screen, text, click_behaviour, pos):
        self.screen = screen
        self.text = text
        self.click_behaviour = click_behaviour["onClick"]

        self.hover = False
        self.text_surface = Button.FONT.render(self.text, True, (0, 0, 0))

        self.rect = self.text_surface.get_rect()
        self.rect.x, self.rect.y = -self.rect.center[0], -self.rect.center[1]
        self.rect.x += pos[0]
        self.rect.y += pos[1]
    
    def click(self):
        if not self.hover:
            return []
        return self.click_behaviour

    def render(self):
        pygame.draw.rect(
            self.screen,
            (0, 0, 255) if self.hover else (255, 0, 0),
            self.rect
        )
        self.screen.blit(self.text_surface, self.rect)
    
    def update(self, mouse_pos):
        self.hover = self.rect.collidepoint(mouse_pos)