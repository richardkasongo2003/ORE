import pygame
import sys
import random
from diver import Diver
from asteroid import Asteroid
from enemy import Enemy

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("ORE")
        self.clock = pygame.time.Clock()
        self.is_running = True
        self.diver = Diver(400, 300)
        self.diver_image = pygame.image.load("image/player_walk_2.webp").convert_alpha()
        self.asteroids = []
        self.astero = None
        self.enemies = []
        self.last_asteroid_spawn_time = pygame.time.get_ticks()  # Time of last asteroid spawn
        self.last_enemy_spawn_time = pygame.time.get_ticks()
       
        # Load ocean water image
        original_ocean_image = pygame.image.load("image/ocean.png").convert_alpha()
        # Scale it to fit the screen
        self.ocean_image = pygame.transform.scale(original_ocean_image, (800, 600))

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
    def update(self):
        self.diver.update_shots()

        current_time = pygame.time.get_ticks()

        # Spawn enemies every 0.5 seconds at 5 positions alternating
        if current_time - self.last_enemy_spawn_time > 500:
            # Alternate between 1 position
            positions = [200]
            for pos in positions:
                enemy = Enemy(800, pos)  # Initialize enemy with screen width and position
                self.enemies.append(enemy)
            self.last_enemy_spawn_time = current_time  # Update last spawn time

        # Move and update enemies
        for enemy in self.enemies:
            enemy.move()

            # Check if the enemy collides with the diver's shots
            for shot in self.diver.shots:
                shot_rect = pygame.Rect(shot.x, shot.y, 0, 0)
                if enemy.check_collision(shot_rect):
                    self.enemies.remove(enemy)
                    self.diver.shots.remove(shot)
                    # Increase score when enemy is hit
                    self.score += 1
                    break  # Break out of the inner loop once collision is detected

            # Remove enemy if it goes below the screen
            if enemy.y > 600:
                self.enemies.remove(enemy)

            # Move and update asteroids
            for asteroid in self.asteroids:
                asteroid.move()
                for shot in self.diver.shots:
                    if asteroid.check_collision(shot):
                        self.asteroids.remove(asteroid)
                        self.diver.shots.remove(shot)
                        break  # Break out of the inner loop once collision is detected

    def draw(self):
        self.screen.blit(self.ocean_image, (0, 0))
        self.diver.draw_shots(self.screen)
        self.screen.blit(self.diver_image, (self.diver.x - self.diver_image.get_width() / 2, self.diver.y - self.diver_image.get_height() / 2))

        # Draw asteroids
        # for asteroid in self.asteroids:
        #     asteroid.draw(self.screen)

        self.astero = Asteroid(200,300)
        self.astero.draw(self.screen)
        
        # Draw enemies
        for enemy in self.enemies:
            enemy.draw(self.screen)

        pygame.display.flip()

    def start(self):
        while self.is_running:
            self.handle_events()
            self.draw()
            self.update()
            self.clock.tick(60)

        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = Game()
    game.start()

