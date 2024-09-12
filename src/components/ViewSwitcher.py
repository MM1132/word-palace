from src.utils.Constants import *

class ViewSwitcher:
    def __init__(self, screen, name, views, initial_view):
        self.screen = screen
        self.name = name
        self.views = views

        self.view = self.views[initial_view]
    
    def update(self, mouse_pos):
        self.view.update(mouse_pos)
    
    def render(self):
        self.view.render()

    def click(self):
        click_behaviour_list = self.view.click()
        for i in reversed(range(len(click_behaviour_list))):
            if "executed" in click_behaviour_list[i] and click_behaviour_list[i]["executed"] == True:
                continue
            if (click_behaviour_list[i]["type"] == OnClickType.SWITCH_VIEW) \
            and (click_behaviour_list[i]["data"] in self.views):
                self.view = self.views[click_behaviour_list[i]["data"]]
                click_behaviour_list[i]["executed"] = True
            elif (click_behaviour_list[i]["type"] == OnClickType.FUNCTION):
                click_behaviour_list[i]["data"](*(click_behaviour_list[i]["props"]))
                click_behaviour_list[i]["executed"] = True
        if len([v["executed"] for v in click_behaviour_list if "executed" in v and v["executed"] == True]) == len(click_behaviour_list):
            for v in click_behaviour_list:
                v["executed"] = False
            return []
        return click_behaviour_list