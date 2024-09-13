import random
from src.utils.Constants import *
import pygame

class Word:
    BORDERS = [
        pygame.Rect(0, 0, SCREEN_WIDTH, 50),
        pygame.Rect(-10, 0, 10, SCREEN_HEIGHT),
        pygame.Rect(0, SCREEN_HEIGHT, SCREEN_WIDTH, 10),
        pygame.Rect(SCREEN_WIDTH, 0, 10, SCREEN_HEIGHT)
    ]

    def __init__(self, screen, lang_1, lang_2, words):
        self.screen = screen
        self.lang_1 = lang_1.strip()
        self.lang_2 = lang_2.strip()

        self.color = self.color = (random.randint(45, 230), random.randint(45, 230), random.randint(45, 230))
        self.hover = False

        tries = 1
        while tries < 100:
            tries += 1

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

            # Collisions
            if self.text_rect.collidelist([word.text_rect for word in words]) != -1:
                continue

            if self.text_rect.collidelist(Word.BORDERS) != -1:
                continue

            break

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

    def click(self):
        return self.hover
