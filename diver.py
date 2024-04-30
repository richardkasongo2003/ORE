import pygame

class Diver:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 5
        self.shots = []
        self.directions = {'up': False, 'down': False, 'left': False, 'right': False}

    def move_up(self):
        self.directions['up'] = True

    def move_down(self):
        self.directions['down'] = True

    def move_left(self):
        self.directions['left'] = True

    def move_right(self):
        self.directions['right'] = True

    def stop_up(self):
        self.directions['up'] = False

    def stop_down(self):
        self.directions['down'] = False

    def stop_left(self):
        self.directions['left'] = False

    def stop_right(self):
        self.directions['right'] = False

    def move(self):
        if self.directions['up']:
            self.y -= self.speed
        if self.directions['down']:
            self.y += self.speed
        if self.directions['left']:
            self.x -= self.speed
        if self.directions['right']:
            self.x += self.speed

    def shoot(self):
        shot = Shot(self.x, self.y)
        self.shots.append(shot)

    def update_shots(self):
        for shot in self.shots:
            shot.move()
            if shot.y < 0:
                self.shots.remove(shot)

    def draw_shots(self, screen):
        for shot in self.shots:
            shot.draw(screen)

    def reset(self, x, y):
        self.x = x
        self.y = y
        self.shots.clear()

class Shot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        self.y -= 10

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (self.x, self.y), 5)


        
