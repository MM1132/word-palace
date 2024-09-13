from src.components.Word import Word
import random, pygame

class WordManager:
    def __init__(self, screen):
        self.screen = screen

        self.words = []

    def set_level(self, level):
        self.words = []
        with open(level, "r", encoding="utf-8") as f:
            for line in f:
                self.words.append(Word(self.screen, *line.split(":"), self.words))
    
    def get_random_word(self):
        return random.choice([word.lang_1 for word in self.words])
    
    def update(self, mouse_pos):
        for word in self.words:
            word.update(mouse_pos)
    
    def render(self):
        for word in self.words:
            word.render()

    def click(self):
        for word in self.words:
            hovering = word.click()
            if hovering:
                return word.lang_1
        return None
