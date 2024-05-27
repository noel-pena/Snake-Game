import pygame, sys, random
from pygame.math import Vector2

class SNAKE:
    def __init__(self):
        self.body = [Vector2(5,10), Vector2(6,10), Vector2(7,10)]
        self.direction = Vector2(1,0)
        # Right: (1, 0)
        # Left: (-1, 0)
        # Up: (0, -1)
        # Down: (0, 1)
        
    def draw_snake(self):
        for block in self.body:
            # Create rectangle
            x_pos = block.x * cell_size
            y_pos = block.y * cell_size
            snake_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)
            pygame.draw.rect(screen, (5,15,10), snake_rect)

    def move_snake(self):
        body_copy = self.body[:-1] # Removes the last item of the list
        body_copy.insert(0,body_copy[0] + self.direction) # Add 1 element of the front this moves forward
        self.body = body_copy[:]

class FRUIT:
    def __init__(self):
        # create a reusable x and y position using vectors
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x,self.y)
        
    def draw_fruit(self):
        # create a rectangle
        fruit_rect = pygame.Rect(self.pos.x * cell_size, self.pos.y * cell_size, cell_size,cell_size) # w, y, w, h
        pygame.draw.rect(screen, (126,166,114), fruit_rect) # Surface, color, rect

pygame.init()
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
clock = pygame.time.Clock() 

fruit = FRUIT() # Call FRUIT class
snake = SNAKE() # Call SNAKE class

SCREEN_UPDATE = pygame.USEREVENT # The event for the time
pygame.time.set_timer(SCREEN_UPDATE, 150) # Event gets triggered every 150ms

# Main game loop
while True:
    for event in pygame.event.get():
        # Quit game
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # Moves snake
        if event.type == SCREEN_UPDATE:
            snake.move_snake()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.direction= Vector2(0,-1)
            if event.key == pygame.K_DOWN:
                snake.direction= Vector2(0, 1) 
            if event.key == pygame.K_LEFT:
                snake.direction= Vector2(-1, 0)
            if event.key == pygame.K_RIGHT:
                snake.direction= Vector2(1, 0)

    screen.fill((175,215,70))
    fruit.draw_fruit()
    snake.draw_snake()
    pygame.display.update()
    clock.tick(60) # Locks the framerate for all systems to 60 fps