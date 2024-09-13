from src.components.ViewSwitcher import ViewSwitcher
from src.components.Button import Button
from src.components.View import View
from src.utils.Constants import OnClickType, SCREEN_WIDTH
import glob

class MainMenu(ViewSwitcher):
    def __init__(self, screen, name, set_running, set_level, set_palace):
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
                            "Choose Palace", 
                            {
                                "onClick": [
                                    {
                                        "type": OnClickType.SWITCH_VIEW,
                                        "data": "choosePalace"
                                    }
                                ]
                            },
                            (SCREEN_WIDTH / 2, 200)
                        ),
                        Button(
                            screen, 
                            "Quit", 
                            {
                                "onClick": [
                                    {
                                        "type": OnClickType.FUNCTION,
                                        "data": set_running,
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
                        *([Button(
                            screen, 
                            filename, 
                            {
                                "onClick": [
                                    {
                                        "type": OnClickType.FUNCTION,
                                        "data": set_level,
                                        "props": [filename]
                                    },
                                    {
                                        "type": OnClickType.SWITCH_VIEW,
                                        "data": "game",
                                    }
                                ]
                            },
                            (SCREEN_WIDTH / 2, 100 + index * 80)
                        ) for index, filename in enumerate(glob.glob("wordlists/*.wl"))]),
                        Button(
                            screen, 
                            "Back", 
                            {
                                "onClick": [
                                    {
                                        "type": OnClickType.SWITCH_VIEW,
                                        "data": "main"
                                    }
                                ]
                            },
                            (SCREEN_WIDTH / 2, 700)
                        )
                    ]
                ),
                "choosePalace": View(
                    [
                        *([Button(
                            screen, 
                            filename, 
                            {
                                "onClick": [
                                    {
                                        "type": OnClickType.FUNCTION,
                                        "data": set_palace,
                                        "props": [filename]
                                    },
                                    {
                                        "type": OnClickType.SWITCH_VIEW,
                                        "data": "game",
                                    }
                                ]
                            },
                            (SCREEN_WIDTH / 2, 100 + index * 80)
                        ) for index, filename in enumerate(glob.glob("palaces/*.palace"))]),
                        Button(
                            screen, 
                            "Back", 
                            {
                                "onClick": [
                                    {
                                        "type": OnClickType.SWITCH_VIEW,
                                        "data": "main"
                                    }
                                ]
                            },
                            (SCREEN_WIDTH / 2, 700)
                        )
                    ]
                )
            },
            "main"
        )
