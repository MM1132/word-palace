from src.components.Word import Word
import random, pygame
from src.utils.Constants import *

class WordManager:
    BORDERS = [
        pygame.Rect(0, 0, SCREEN_WIDTH, 50),
        pygame.Rect(-10, 0, 10, SCREEN_HEIGHT),
        pygame.Rect(0, SCREEN_HEIGHT, SCREEN_WIDTH, 10),
        pygame.Rect(SCREEN_WIDTH, 0, 10, SCREEN_HEIGHT)
    ]

    def __init__(self, screen):
        self.screen = screen
        self.save_filename = None

        self.words = []
    
    def load_palace(self, palace_filename):
        with open(palace_filename, "r") as f:
            for line in f:
                self.words.append(Word())

    def set_level(self, level):
        self.words = []
        with open(level, "r", encoding="utf-8") as f:
            for line in f:
                tries_counter = 0
                while tries_counter < 100:
                    tries_counter += 1

                    new_word = Word(self.screen, *line.split(":"))
                    # Collisions
                    if new_word.text_rect.collidelist([word.text_rect for word in self.words]) != -1:
                        continue
                    if new_word.text_rect.collidelist(WordManager.BORDERS) != -1:
                        continue
                    self.words.append(new_word)
                    break
        
        self.save_filename = level.replace(".wl", ".palace").replace("wordlists/", "palaces/")
    
    def set_palace(self, palace_filename):
        with open(palace_filename, "r") as f:
            self.words = [Word.from_palace_data(self.screen, *(line.strip().split(","))) for line in f]

    def save_palace(self):
        with open(self.save_filename, "w") as f:
            for word in self.words:
                f.write(
                    "{},{},{},{},{},{},{},{}\n".format(
                        word.lang_1,
                        word.lang_2,
                        word.pos[0],
                        word.pos[1],
                        word.color[0],
                        word.color[1],
                        word.color[2],
                        word.box_size,
                    )
                )

    # Unless all the active words are guessed
    # Don't pick any new words
    def get_random_word(self):
        all_active_words = [word for word in self.words if word.active]
        have_all_active_words_been_guessed = all([word.guessed for word in all_active_words])
        if have_all_active_words_been_guessed:
            for word in self.words:
                word.set_guessed(False)
            not_active_words = [word for word in self.words if not word.active]
            if len(not_active_words) != 0:
                random_word = random.choice(not_active_words)
                random_word.activate()
                return random_word.lang_1
        random_word = random.choice([word for word in all_active_words if not word.guessed])
        return random_word.lang_1
    
    def update(self, mouse_pos):
        for word in self.words:
            if word.active:
                word.update(mouse_pos)
    
    def render(self):
        for word in self.words:
            if word.active:
                word.render()

    def click(self):
        for word in self.words:
            hovering = word.click()
            if hovering:
                return word
        return None
