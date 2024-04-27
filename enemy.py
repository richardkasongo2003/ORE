import pygame
import random

class Enemy:
    def __init__(self, screen_width, x):
        self.image = pygame.image.load("image/enemy.png").convert_alpha()
        self.width, self.height = self.image.get_size()
        self.x = x  # Use the provided x position
        self.y = -self.height  # Start above the screen
        self.speed_x = random.choice([-1, 1])  # Random speed for variation in x direction
        self.speed_y = random.randint(1, 2)  # Random speed for variation in y direction

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def check_collision(self, other_object):
        enemy_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        return enemy_rect.colliderect(other_object)

    def reset(self, screen_width):
        self.x = random.randint(0, screen_width - self.width)
        self.y = -self.height
        self.speed_x = random.choice([-1, 1])
        self.speed_y = random.randint(1, 2)
