import random
from src.utils.Constants import *
import pygame

class Word:
    FONT = pygame.font.SysFont(pygame.font.get_fonts()[0], 50)

    def __init__(self, screen, lang_1, lang_2, words):
        self.screen = screen
        self.lang_1 = lang_1.strip()
        self.lang_2 = lang_2.strip()

        self.color = self.color = (random.randint(40, 255), random.randint(40, 255), random.randint(40, 255))
        self.hover = False

        tries = 1
        while tries < 100:
            self.pos = [random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT)]

            self.text_surface = Word.FONT.render(self.lang_2, True, (0, 0, 0))
            self.text_rect = self.text_surface.get_rect()
            self.text_rect.x = self.pos[0] - self.text_rect.center[0]
            self.text_rect.y = self.pos[1] - self.text_rect.center[1]

            self.box_size = 60
            self.rect = pygame.Rect(
                self.pos[0] - self.box_size / 2, 
                self.pos[1] - self.box_size / 2, 
                self.box_size, 
                self.box_size
            )

            if self.rect.collidelist([word.rect for word in words]) == -1 and \
                self.text_rect.collidelist([word.text_rect for word in words]) == -1:
                break

            tries += 1

    def update(self, mouse_pos):
        self.hover = self.rect.collidepoint(mouse_pos)

    def render(self):
        pygame.draw.rect(
            self.screen, 
            self.color, 
            self.rect
        )
        if (self.hover):
            self.screen.blit(self.text_surface, self.text_rect)