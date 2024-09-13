import random
from src.utils.Constants import *
import pygame

class Word:
    def __init__(self, screen, lang_1, lang_2):
        self.screen = screen
        self.lang_1 = lang_1.strip()
        self.lang_2 = lang_2.strip()

        self.color = self.color = (random.randint(45, 230), random.randint(45, 230), random.randint(45, 230))
        self.hover = False

        ### 
        self.pos = [random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT)]

        self.box_size = random.randint(30, 60)
        FONT = pygame.font.SysFont(pygame.font.get_fonts()[0], self.box_size)

        self.text_surface = FONT.render(self.lang_2, True, (255, 255, 255), self.color)
        self.text_rect = self.text_surface.get_rect()
        self.text_rect.x = self.pos[0] - self.text_rect.center[0]
        self.text_rect.y = self.pos[1] - self.text_rect.center[1]

        self.rect = pygame.Rect(
            self.pos[0] - self.box_size / 2, 
            self.pos[1] - self.box_size / 2, 
            self.box_size, 
            self.box_size
        )

        self.active = False
        self.guessed = False
    
    def activate(self):
        self.active = True
    
    def set_guessed(self, state):
        self.guessed = state

    def update(self, mouse_pos):
        self.hover = self.rect.collidepoint(mouse_pos)

    def render(self):
        pygame.draw.rect(
            self.screen, 
            self.color, 
            self.rect
        )
        if self.guessed:
            pygame.draw.rect(
                self.screen, 
                (255, 255, 255), 
                self.rect,
                2
            )
        
        if self.hover:
            self.screen.blit(self.text_surface, self.text_rect)
            if self.guessed:
                pygame.draw.rect(
                    self.screen, 
                    (255, 255, 255), 
                    self.text_rect,
                    4
                )

    def click(self):
        return self.hover
