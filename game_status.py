import pygame
class GameStatus:
    def __init__(self):
        self.win_score = 100
        self.game_duration = 60  # in seconds
        self.game_over = False  # Track game over state

    def check_game_over(self, score, elapsed_time):
        if score >= self.win_score or elapsed_time >= self.game_duration:
            self.game_over = True
            if score >= self.win_score:
                return True, "You win!"
            else:
                return True, "Time's up! You lose!"
        else:
            return False, None

    def get_elapsed_time(self, start_time):
        return (pygame.time.get_ticks() - start_time) / 1000  # Convert milliseconds to seconds
