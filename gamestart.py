import pygame
import random
from diver import Diver
from asteroid import Asteroid
from score import Score
from game_status import GameStatus

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("ORE")
        self.clock = pygame.time.Clock()
        self.is_running = True
        self.diver = Diver(400, 300)
        self.diver_image = pygame.image.load("image/player_walk_2.png").convert_alpha()
        self.asteroids = []
        self.last_asteroid_spawn_time = pygame.time.get_ticks()  # Time of last asteroid spawn
        self.asteroid_spawn_delay = 3000  # Initial delay before the first asteroid spawn
        self.score = Score()  # Initialize Score object
        self.game_status = GameStatus()  # Initialize GameStatus object
        self.start_time = pygame.time.get_ticks()  # Time when the game started
        self.message_font = pygame.font.Font(None, 36)

        # Load ocean water image
        original_ocean_image = pygame.image.load("image/ocean.png").convert_alpha()
        # Scale it to fit the screen
        self.ocean_image = pygame.transform.scale(original_ocean_image, (800, 600))

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False
            elif event.type == pygame.KEYDOWN:
                if not self.game_status.game_over:
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
                else:
                    self.__init__()  # Restart the game if any key is pressed after game over
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    self.diver.stop_up()
                elif event.key == pygame.K_DOWN:
                    self.diver.stop_down()
                elif event.key == pygame.K_LEFT:
                    self.diver.stop_left()
                elif event.key == pygame.K_RIGHT:
                    self.diver.stop_right()

    def update(self):
        if not self.game_status.game_over:
            self.diver.move()

            self.diver.update_shots()

            # Spawn asteroids randomly
            current_time = pygame.time.get_ticks()
            if current_time - self.last_asteroid_spawn_time > self.asteroid_spawn_delay:
                # Choose a random position at the top to spawn the asteroid
                x_positions = [0, 200, 400, 600]  # Four different x positions
                x = random.choice(x_positions)
                asteroid = Asteroid(x, 0)  # Spawn asteroid at the top of the screen
                self.asteroids.append(asteroid)

                # Update last spawn time and set a new random spawn delay
                self.last_asteroid_spawn_time = current_time
                self.asteroid_spawn_delay = random.randint(2000, 4000)  # Random delay between 2 to 4 seconds

            # Move and update asteroids
            for asteroid in self.asteroids:
                asteroid.move()

                # Check collision with shots
                for shot in self.diver.shots:
                    if asteroid.check_collision(shot):
                        self.asteroids.remove(asteroid)
                        self.diver.shots.remove(shot)
                        self.score.increment_score()  # Increase score when an asteroid is destroyed
                        break  # Break out of the inner loop once collision is detected

            # Check game status
            game_over, message = self.game_status.check_game_over(self.score.score, self.game_status.get_elapsed_time(self.start_time))
            if game_over:
                self.game_status.game_over = True
                self.game_over_message = message

    def draw(self):
        self.screen.blit(self.ocean_image, (0, 0))
        self.diver.draw_shots(self.screen)
        self.screen.blit(self.diver_image, (self.diver.x - self.diver_image.get_width() / 2, self.diver.y - self.diver_image.get_height() / 2))

        # Draw asteroids
        for asteroid in self.asteroids:
            asteroid.draw(self.screen)

        # Draw score
        self.score.draw(self.screen)

        # Draw time
        elapsed_time = self.game_status.get_elapsed_time(self.start_time)
        remaining_time = max(0, self.game_status.game_duration - elapsed_time)
        time_text = self.score.font.render(f"Time: {int(remaining_time)}", True, (255, 255, 255))
        self.screen.blit(time_text, (10, 50))

        # Draw game over message and restart option
        if self.game_status.game_over:
            message_surface = self.message_font.render(self.game_over_message, True, (255, 255, 255))
            restart_surface = self.message_font.render("Click anywhere to restart", True, (255, 255, 255))
            message_rect = message_surface.get_rect(center=(400, 300))
            restart_rect = restart_surface.get_rect(center=(400, 350))
            self.screen.blit(message_surface, message_rect)
            self.screen.blit(restart_surface, restart_rect)

        pygame.display.flip()

    def start(self):
        while self.is_running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(60)

if __name__ == "__main__":
    game = Game()
    game.start()
