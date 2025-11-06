import pygame


class Enemy:
    """
    Patrolling enemy extracted from jumpingGame.py
    """

    def __init__(self, x, y, patrol_start, patrol_end):
        self.x = x
        self.y = y
        self.width = 25
        self.height = 25
        self.speed = 2
        self.patrol_start = patrol_start
        self.patrol_end = patrol_end
        self.direction = 1
        self.rect = pygame.Rect(x, y, self.width, self.height)
        self.image = None
        self.load_image()

    def load_image(self):
        try:
            self.image = pygame.image.load("assets/pixel_enemy.jpg")
            self.image = pygame.transform.scale(self.image, (self.width, self.height))
            print("Successfully loaded pixel_enemy.jpg image")
        except Exception:
            print("Could not load pixel_enemy.jpg, using circle shape")
            self.image = None

    def update(self):
        self.x += self.speed * self.direction
        if self.x <= self.patrol_start:
            self.x = self.patrol_start
            self.direction = 1
        elif self.x >= self.patrol_end - self.width:
            self.x = self.patrol_end - self.width
            self.direction = -1
        self.rect.x = self.x

    def draw(self, screen):
        if hasattr(self, 'image') and self.image:
            screen.blit(self.image, (self.x, self.y))
        else:
            center_x = self.x + self.width // 2
            center_y = self.y + self.height // 2
            pygame.draw.circle(screen, (255, 0, 0), (center_x, center_y), self.width // 2)
            pygame.draw.circle(screen, (255, 255, 255), (center_x - 5, center_y - 3), 3)
            pygame.draw.circle(screen, (255, 255, 255), (center_x + 5, center_y - 3), 3)
            pygame.draw.circle(screen, (0, 0, 0), (center_x - 5, center_y - 3), 1)
            pygame.draw.circle(screen, (0, 0, 0), (center_x + 5, center_y - 3), 1)
