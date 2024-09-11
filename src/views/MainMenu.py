from src.components.ViewSwitcher import ViewSwitcher
from src.components.Button import Button
from src.components.View import View
from src.utils.Constants import OnClickType, SCREEN_WIDTH

class MainMenu(ViewSwitcher):
    def __init__(self, screen, name, stop_running, select_level):
        super().__init__(
            screen,
            name,
            {
                "main": View(
                    [
                        Button(
                            screen, 
                            "Choose Wordlist", 
                            {
                                "onClick": [
                                    {
                                        "type": OnClickType.SWITCH_VIEW,
                                        "data": "chooseWordlist"
                                    }
                                ]
                            },
                            (SCREEN_WIDTH / 2, 120)
                        ),
                        Button(
                            screen, 
                            "Quit", 
                            {
                                "onClick": [
                                    {
                                        "type": OnClickType.FUNCTION,
                                        "data": stop_running,
                                        "props": [False]
                                    }
                                ]
                            },
                            (SCREEN_WIDTH / 2, 650)
                        )
                    ]
                ),
                "chooseWordlist": View(
                    [
                        Button(
                            screen, 
                            "Select test level", 
                            {
                                "onClick": [
                                    {
                                        "type": OnClickType.FUNCTION,
                                        "data": select_level,
                                        "props": ["wordlists/foods_general.wl"]
                                    },
                                    {
                                        "type": OnClickType.SWITCH_VIEW,
                                        "data": "game",
                                    }
                                ]
                            },
                            (SCREEN_WIDTH / 2, 250)
                        ),
                        Button(
                            screen, 
                            "Backkkk", 
                            {
                                "onClick": [
                                    {
                                        "type": OnClickType.SWITCH_VIEW,
                                        "data": "main"
                                    }
                                ]
                            },
                            (SCREEN_WIDTH / 2, 500)
                        )
                    ]
                )
            },
            "main"
        )
