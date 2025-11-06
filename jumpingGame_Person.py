import pygame


class Person:
    """
    Person class for Rob extracted from jumpingGame.py.
    Accepts screen dimensions so it can be used standalone.
    """

    def __init__(self, x, y, screen_width=500, screen_height=500):
        # Store screen bounds locally instead of importing from the main file
        self.screen_width = screen_width
        self.screen_height = screen_height

        # Position and size
        self.x = x
        self.y = y
        self.width = 30
        self.height = 30

        # Movement parameters
        self.speed = 5
        self.jump_speed = 15
        self.velocity_y = 0
        self.on_ground = False
        self.gravity = 0.8

        # Collision rect
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

        # Image (optional)
        self.image = None
        self.load_image()

    def load_image(self):
        try:
            self.image = pygame.image.load("assets/pixel_hero.jpg")
            self.image = pygame.transform.scale(self.image, (self.width, self.height))
            print("Successfully loaded pixel_hero.jpg image for Rob")
        except Exception as e:
            # Catch broad exception to avoid crashing if file missing
            print(f"Could not load pixel_hero.jpg: {e}")
            self.image = None

    def move_left(self):
        if self.x > 0:
            self.x -= self.speed
            self.rect.x = self.x

    def move_right(self):
        if self.x < self.screen_width - self.width:
            self.x += self.speed
            self.rect.x = self.x

    def jump(self):
        if self.on_ground:
            self.velocity_y = -self.jump_speed
            self.on_ground = False

    def update(self):
        self.velocity_y += self.gravity
        self.y += self.velocity_y

        if self.y >= self.screen_height - self.height:
            self.y = self.screen_height - self.height
            self.velocity_y = 0
            self.on_ground = True

        self.rect.y = self.y

    def draw(self, screen):
        if hasattr(self, 'image') and self.image:
            screen.blit(self.image, (self.x, self.y))
        else:
            pygame.draw.rect(screen, (0, 0, 255), (self.x, self.y, self.width, self.height))
