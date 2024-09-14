import random
from src.utils.Constants import *
import pygame

class Word:
    def __init__(self, screen, lang_1, lang_2):
        self.screen = screen
        self.lang_1 = lang_1.strip()
        self.lang_2 = lang_2.strip()

        self.color = (random.randint(45, 220), random.randint(45, 220), random.randint(45, 220))
        self.hover = False
        self.active = True
        self.guessed = False

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
    
    @classmethod
    def from_palace_data(cls, screen, lang_1, lang_2, pos_1, pos_2, red, green, blue, box_size):
        word = cls(screen, lang_1, lang_2)
        word.pos = [int(pos_1), int(pos_2)]
        word.color = (int(red), int(green), int(blue))
        word.box_size = int(box_size)

        FONT = pygame.font.SysFont(pygame.font.get_fonts()[0], word.box_size)
        word.text_surface = FONT.render(word.lang_2, True, (255, 255, 255), word.color)
        word.text_rect = word.text_surface.get_rect()
        word.text_rect.x = word.pos[0] - word.text_rect.center[0]
        word.text_rect.y = word.pos[1] - word.text_rect.center[1]

        word.rect = pygame.Rect(
            word.pos[0] - word.box_size / 2, 
            word.pos[1] - word.box_size / 2, 
            word.box_size, 
            word.box_size
        )

        return word
    
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
