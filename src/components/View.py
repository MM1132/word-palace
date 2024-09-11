class View:
    def __init__(self, elements):
        self.elements = elements
    
    def update(self, mouse_pos):
        for element in self.elements:
            element.update(mouse_pos)
    
    def render(self):
        for element in self.elements:
            element.render()

    def click(self):
        for element in self.elements:
            click_behaviour_list = element.click()
            if type(click_behaviour_list) is list and len(click_behaviour_list) != 0:
                return click_behaviour_list
        return []