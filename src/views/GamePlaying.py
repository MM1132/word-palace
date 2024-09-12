from src.components.Button import Button
from src.utils.Constants import OnClickType

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
    
    def set_level(self, level):
        self.level = level
        print("Level set to: {}".format(self.level))

    def update(self, mouse_pos):
        self.back_button.update(mouse_pos)

    def render(self):
        self.back_button.render()

    def click(self):
        click_behaviour = self.back_button.click()
        if type(click_behaviour) is list and len(click_behaviour) != 0:
            return click_behaviour
        return []