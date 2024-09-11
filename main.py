import pygame
pygame.init()

pygame.display.set_caption('My Game')

from src.Game import Game

game = Game()
game.start()

pygame.quit()
