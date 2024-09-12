from src.components.Word import Word

class WordManager:
    def __init__(self, screen):
        self.screen = screen

        self.words = []

    def set_level(self, level):
        self.words = []
        with open(level, "r", encoding="utf-8") as f:
            for line in f:
                self.words.append(Word(self.screen, *line.split(":"), self.words))
    
    def update(self, mouse_pos):
        for word in self.words:
            word.update(mouse_pos)
    
    def render(self):
        for word in self.words:
            word.render()