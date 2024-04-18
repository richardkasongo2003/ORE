import pygame
import random

class Asteroid:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 20
        self.speed = 3
        self.direction = random.choice(["up", "down", "left", "right"])

    def move(self):
        if self.direction == "up":
            self.y -= self.speed
        elif self.direction == "down":
            self.y += self.speed
        elif self.direction == "left":
            self.x -= self.speed
        elif self.direction == "right":
            self.x += self.speed

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 0, 0), (self.x, self.y), self.radius)

    def check_collision(self, bullet):
        distance = ((self.x - bullet.x) ** 2 + (self.y - bullet.y) ** 2) ** 0.5
        if distance < self.radius:
            return True
        else:
            return False

