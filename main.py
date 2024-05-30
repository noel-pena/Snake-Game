import pygame, sys
from pygame.math import Vector2
from snake import SNAKE
from fruit import FRUIT

class MAIN:
    def __init__(self, cell_size, cell_number):
        self.cell_size = cell_size
        self.cell_number = cell_number
        self.snake = SNAKE()
        self.fruit = FRUIT(cell_size, cell_number)
        self.initial_speed = 150
        self.speed_increment = 2
        self.current_speed = self.initial_speed
        self.update_speed()

    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()
        self.adjust_speed()

    def draw_elements(self, screen):
        self.draw_grass(screen)
        self.fruit.draw_fruit(screen)
        self.snake.draw_snake(screen, self.cell_size)
        self.draw_score(screen)

    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.randomize()
            self.snake.add_block()
            self.snake.play_sound()

        for block in self.snake.body[1:]:
            if block == self.fruit.pos:
                self.fruit.randomize()

    def check_fail(self):
        if not 0 <= self.snake.body[0].x < self.cell_number or not 0 <= self.snake.body[0].y < self.cell_number:
            self.game_over()

        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()

    def game_over(self):
        self.snake.reset()
        self.current_speed = self.initial_speed
        self.update_speed()

    def draw_grass(self, screen):
        grass_color = (167, 209, 61)
        for row in range(self.cell_number):
            for col in range(row % 2, self.cell_number, 2):
                grass_rect = pygame.Rect(col * self.cell_size, row * self.cell_size, self.cell_size, self.cell_size)
                pygame.draw.rect(screen, grass_color, grass_rect)

    def draw_score(self, screen):
        score_text = str(len(self.snake.body) - 3)
        score_surface = game_font.render(score_text, True, (56, 74, 12))
        score_x = int(self.cell_size * self.cell_number - 60)
        score_y = int(self.cell_size * self.cell_number - 40)
        score_rect = score_surface.get_rect(center=(score_x, score_y))
        apple_rect = self.fruit.image.get_rect(midright=(score_rect.left, score_rect.centery))
        bg_rect = pygame.Rect(apple_rect.left, apple_rect.top, apple_rect.width + score_rect.width + 6, apple_rect.height)

        pygame.draw.rect(screen, (167, 209, 61), bg_rect)
        screen.blit(score_surface, score_rect)
        screen.blit(self.fruit.image, apple_rect)
        pygame.draw.rect(screen, (56, 74, 12), bg_rect, 2)
        
    def adjust_speed(self):
        score = len(self.snake.body) - 3
        if score != 0:
            new_speed = self.initial_speed - (score * self.speed_increment)
            if new_speed != self.initial_speed:
                self.current_speed = new_speed
                self.update_speed()
    
    def update_speed(self):
        pygame.time.set_timer(SCREEN_UPDATE, self.current_speed)

pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
clock = pygame.time.Clock()
game_font = pygame.font.Font('font/PoetsenOne-Regular.ttf', 25)

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

main_game = MAIN(cell_size, cell_number)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            main_game.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and main_game.snake.direction.y != 1:
                main_game.snake.direction = Vector2(0, -1)
            if event.key == pygame.K_DOWN and main_game.snake.direction.y != -1:
                main_game.snake.direction = Vector2(0, 1)
            if event.key == pygame.K_LEFT and main_game.snake.direction.x != 1:
                main_game.snake.direction = Vector2(-1, 0)
            if event.key == pygame.K_RIGHT and main_game.snake.direction.x != -1:
                main_game.snake.direction = Vector2(1, 0)
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

    screen.fill((175, 215, 70))
    main_game.draw_elements(screen)
    pygame.display.update()
    clock.tick(60)
