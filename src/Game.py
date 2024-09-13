import pygame
from src.components.Button import Button
from src.components.ViewSwitcher import ViewSwitcher
from src.utils.Constants import *
from src.components.View import View
from src.views.MainMenu import MainMenu
from src.views.GamePlaying import GamePlaying

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.mouse_pos = pygame.mouse.get_pos()
        self.game_running = True
        self.clock = pygame.time.Clock()

        self.game_playing = GamePlaying(self.screen)

        self.view_switcher = ViewSwitcher(
            self.screen,
            "controller",
            {
                "main-menu": MainMenu(
                    self.screen,
                    "main-menu",
                    self.set_running,
                    self.game_playing.set_level,
                    self.game_playing.set_palace
                ),
                "game": ViewSwitcher(
                    self.screen,
                    "game",
                    {
                        "game-playing": View(
                            [
                                self.game_playing
                            ]
                        ),
                    },
                    "game-playing"
                )
            }, 
            "main-menu"
        )
    
    def set_running(self, state):
        self.game_running = state

    def update(self):
        self.view_switcher.update(self.mouse_pos)

    def render(self):
        self.view_switcher.render()

    def start(self):
        while self.game_running:
            for event in pygame.event.get():
                self.handle_pygame_event(event)

            self.update()

            self.screen.fill((10, 15, 10))
            self.render()

            pygame.display.flip()

            self.clock.tick(60)
    
    def mouse_clicked(self):
        self.view_switcher.click()

    def handle_pygame_event(self, event):
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            self.game_running = False
        elif event.type == pygame.MOUSEMOTION:
            self.set_mouse_position(pygame.mouse.get_pos())
        elif event.type == pygame.MOUSEBUTTONDOWN:
            self.mouse_clicked()
    
    def set_mouse_position(self, mouse_pos):
        self.mouse_pos = mouse_pos
