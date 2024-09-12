from src.components.Button import Button
from src.utils.Constants import OnClickType
from src.components.Word import Word
from src.components.WordManager import WordManager

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
            (50, 50)
        )

        self.word_manager = WordManager(self.screen)
    
    def set_level(self, level):
        self.level = level
        self.word_manager.set_level(self.level)

    def update(self, mouse_pos):
        self.back_button.update(mouse_pos)
        self.word_manager.update(mouse_pos)

    def render(self):
        self.back_button.render()
        self.word_manager.render()

    def click(self):
        click_behaviour = self.back_button.click()
        if type(click_behaviour) is list and len(click_behaviour) != 0:
            return click_behaviour
        return []