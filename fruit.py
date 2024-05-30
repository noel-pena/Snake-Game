import pygame
import random
from pygame.math import Vector2

class FRUIT:
    def __init__(self, cell_size, cell_number):
        self.cell_size = cell_size
        self.cell_number = cell_number
        self.randomize()
        self.original_image = pygame.image.load('pics/apple.png').convert_alpha()
        self.image = pygame.transform.smoothscale(self.original_image, (cell_size, cell_size))

    def draw_fruit(self, screen):
        fruit_rect = pygame.Rect(self.pos.x * self.cell_size, self.pos.y * self.cell_size, self.cell_size, self.cell_size)
        screen.blit(self.image, fruit_rect)

    def randomize(self):
        self.pos = Vector2(random.randint(0, self.cell_number - 1), random.randint(0, self.cell_number - 1))
