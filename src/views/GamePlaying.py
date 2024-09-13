from src.components.Button import Button
from src.utils.Constants import OnClickType
from src.components.WordManager import WordManager
from src.components.Text import Text
from src.utils.Constants import *
import pygame

class GamePlaying:
    def __init__(self, screen):
        self.screen = screen
        self.level = None

        self.back_button = Button(
            self.screen,
            "Back to menu",
            {
                "onClick": [
                    {
                        "type": OnClickType.SWITCH_VIEW,
                        "data": "main-menu"
                    }
                ]
            },
            (50, 25)
        )

        self.word_manager = WordManager(self.screen)
        self.current_word = ""
        self.current_word_text = Text(self.screen, self.current_word, (SCREEN_WIDTH / 2, 20), 36)

        self.score = 0
        self.score_text = Text(self.screen, "Score: {}".format(self.score), (SCREEN_WIDTH - 100, 20), 36)
    
    def increase_score(self):
        self.score += 1
        self.score_text.set_text("Score: {}".format(self.score))

    def get_new_random_word(self):
        self.current_word = self.word_manager.get_random_word()
        self.current_word_text.set_text(self.current_word)

    def set_level(self, level):
        self.level = level
        self.word_manager.set_level(self.level)

        self.get_new_random_word()

    def update(self, mouse_pos):
        self.back_button.update(mouse_pos)
        self.word_manager.update(mouse_pos)
        self.current_word_text.update(mouse_pos)
        self.score_text.update(mouse_pos)

    def render(self):
        self.back_button.render()
        self.word_manager.render()
        self.current_word_text.render()
        self.score_text.render()

        pygame.draw.line(self.screen, (255, 255, 255), (0, 55), (SCREEN_WIDTH, 55))

    def click(self):
        click_behaviour = self.back_button.click()
        if type(click_behaviour) is list and len(click_behaviour) != 0:
            return click_behaviour
        
        clicked_word = self.word_manager.click()
        if clicked_word is not None:
            if clicked_word == self.current_word:
                self.increase_score()
                self.get_new_random_word()

        return []