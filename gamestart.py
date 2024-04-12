import pygame
import sys
from diver import Diver

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("ORE")
        self.clock = pygame.time.Clock()
        self.is_running = True
        self.diver = Diver(400, 300)
        
        self.diver_image = pygame.image.load("image/player_walk_2.png").convert_alpha()
        # self.gun_image = pygame.image.load("gun.png").convert_alpha()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.diver.move_up()
                elif event.key == pygame.K_DOWN:
                    self.diver.move_down()
                elif event.key == pygame.K_LEFT:
                    self.diver.move_left()
                elif event.key == pygame.K_RIGHT:
                    self.diver.move_right()
                elif event.key == pygame.K_SPACE:
                    self.diver.shoot()

    def draw(self):
        self.screen.fill((0, 0, 255))
        self.diver.draw_shots(self.screen)
        self.screen.blit(self.diver_image, (self.diver.x - self.diver_image.get_width() / 2, self.diver.y - self.diver_image.get_height() / 2))
        pygame.display.flip()

    def update(self):
        self.diver.update_shots()

    def start(self):
        while self.is_running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(60)

        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = Game()
    game.start()

