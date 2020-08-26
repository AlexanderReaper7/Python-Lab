import pygame
from pygame.locals import *
from array import *
from typing import TypeVar

BACKGROUND_COLOR = (240,240,240)  # White


class Square:
	def __init__(self):
		self.owner


class Grid:
	def __init__(self):
		self.squares = [Square().__init__() for i in range(3) for j in range(3)]


def main():
    # Initialise screen
    pygame.init()
    screen = pygame.display.set_mode((150, 50))
    pygame.display.set_caption('Tic Tac Toe, but it´s made in python!')

    # Fill background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill(BACKGROUND_COLOR)

    # Display some text
    font = pygame.font.Font(None, 36)
    text = font.render("Hello There", 1, (10, 10, 10))
    textpos = text.get_rect()
    textpos.centerx = background.get_rect().centerx
    background.blit(text, textpos)

    # Blit everything to the screen
    screen.blit(background, (0, 0))
    pygame.display.flip()

    # Event loop
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                return

        screen.blit(background, (0, 0))
        pygame.display.flip()

# Run game
if __name__ == '__main__': main()