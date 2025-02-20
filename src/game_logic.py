import config
import random

class Snake:
    def __init__(self, x, y, length):
        self.body = [(x, y)]
        self.length = length
        self.direction = 'right'
    
    def move(self):
        head = self.body[0]
        x, y = head
        if self.direction == 'right':
            x += 1
        elif self.direction == 'left':
            x -= 1
        elif self.direction == 'up':
            y -= 1
        elif self.direction == 'down':
            y += 1
        self.body.insert(0, (x, y))

        # Aggiunge la nuova testa e rimuove l'ultimo segmento (se non ha mangiato)
        if len(self.body) > self.length:
            self.body.pop()

    def grow(self):
        self.length += 1

    def check_collision(self):
        head = self.body[0]
        x, y = head
        if x < 0 or x >= config.WIDTH // config.GRID_SIZE:
            return True
        if y < 0 or y >= config.HEIGHT // config.GRID_SIZE:
            return True
        if head in self.body[1:]:
            return True
        return False
    
class Food:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.position = [(x, y)]

    def respawn(self):
        self.x = random.randint(0, config.WIDTH // config.GRID_SIZE - 1)
        self.y = random.randint(0, config.HEIGHT // config.GRID_SIZE - 1)
        self.position = [(self.x, self.y)]