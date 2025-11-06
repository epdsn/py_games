import pygame
import random
import sys
import time

# ============================================================
#                 🔧 CUSTOMIZABLE SETTINGS
# ============================================================

# Game window
WINDOW_WIDTH = 16 * 80
WINDOW_HEIGHT = 9 * 80
FPS = 10                      # Base speed (frames per second)

# Grid settings
GRID_SIZE = 15
GRID_WIDTH = WINDOW_WIDTH // GRID_SIZE
GRID_HEIGHT = WINDOW_HEIGHT // GRID_SIZE

# Game mechanics
FOOD_COUNT = 3                # Number of foods on screen
FOOD_EFFECT_DURATION = 5      # Duration (in seconds) of speed effects
FOOD_SCORE_VALUE = 10         # Base score for normal food
SPEED_SCORE_MULTIPLIER = 5    # Multiplier for score when fast

# Food types and colors
FOOD_TYPES = {
    "normal": {"color": (255, 80, 80), "effect": "normal"},
    "speed":  {"color": (255, 255, 0), "effect": "speed"},
    "slow":   {"color": (80, 150, 255), "effect": "slow"},
    "mega":   {"color": (200, 80, 255), "effect": "grow"},
}

# Colors
COLOR_BACKGROUND = (15, 15, 25)
COLOR_GRID = (25, 25, 35)
COLOR_SNAKE = (0, 255, 100)
COLOR_SNAKE_HEAD = (0, 200, 255)
COLOR_TEXT = (240, 240, 240)
COLOR_GLOW = (50, 255, 150)

# Font and UI
FONT_NAME = "arial"
FONT_SIZE = 32
TITLE_FONT_SIZE = 56
myvar = 100
# ============================================================
#                  🎮 INITIALIZATION
# ============================================================

pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("🐍 Snake is cool")
clock = pygame.time.Clock()
font = pygame.font.SysFont(FONT_NAME, FONT_SIZE)
title_font = pygame.font.SysFont(FONT_NAME, TITLE_FONT_SIZE, bold=True)

# ============================================================
#                  🧩 HELPER FUNCTIONS
# ============================================================

def draw_text(text, font, color, surface, x, y, center=False):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    if center:
        text_rect.center = (x, y)
    else:
        text_rect.topleft = (x, y)
    surface.blit(text_obj, text_rect)

def draw_grid():
    for x in range(0, WINDOW_WIDTH, GRID_SIZE):
        pygame.draw.line(screen, COLOR_GRID, (x, 0), (x, WINDOW_HEIGHT))
    for y in range(0, WINDOW_HEIGHT, GRID_SIZE):
        pygame.draw.line(screen, COLOR_GRID, (0, y), (WINDOW_WIDTH, y))

# ============================================================
#                  🐍 SNAKE CLASS
# ============================================================

class Snake:
    def __init__(self):
        self.positions = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        self.direction = random.choice(["UP", "DOWN", "LEFT", "RIGHT"])
        self.grow_amount = 0

    def move(self):
        x, y = self.positions[0]
        if self.direction == "UP": y -= 1
        elif self.direction == "DOWN": y += 1
        elif self.direction == "LEFT": x -= 1
        elif self.direction == "RIGHT": x += 1

        # ❌ Die if hitting wall
        if x < 0 or y < 0 or x >= GRID_WIDTH or y >= GRID_HEIGHT:
            return False

        new_head = (x, y)
        if new_head in self.positions[1:]:
            return False  # Collision with self

        self.positions.insert(0, new_head)
        if self.grow_amount > 0:
            self.grow_amount -= 1
        else:
            self.positions.pop()
        return True

    def draw(self, surface):
        for i, pos in enumerate(self.positions):
            x, y = pos
            rect = pygame.Rect(x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE)
            color = COLOR_SNAKE_HEAD if i == 0 else COLOR_SNAKE
            pygame.draw.rect(surface, color, rect)
            if i == 0:
                glow_rect = rect.inflate(10, 10)
                pygame.draw.ellipse(surface, COLOR_GLOW, glow_rect, 2)

    def change_direction(self, dir):
        opposite = {"UP": "DOWN", "DOWN": "UP", "LEFT": "RIGHT", "RIGHT": "LEFT"}
        if dir != opposite.get(self.direction):
            self.direction = dir

# ============================================================
#                  🍎 FOOD CLASS
# ============================================================

class Food:
    def __init__(self, snake_positions):
        self.type = random.choice(list(FOOD_TYPES.keys()))
        self.color = FOOD_TYPES[self.type]["color"]
        self.effect = FOOD_TYPES[self.type]["effect"]
        self.position = self.random_position(snake_positions)

    def random_position(self, snake_positions):
        pos = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
        while pos in snake_positions:
            pos = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
        return pos

    def draw(self, surface):
        x, y = self.position
        rect = pygame.Rect(x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE)
        pygame.draw.rect(surface, self.color, rect)
        glow_rect = rect.inflate(6, 6)
        pygame.draw.ellipse(surface, self.color, glow_rect, 2)

# ============================================================
#                  ⚙️ GAME LOOP
# ============================================================

def main():
    snake = Snake()
    foods = [Food(snake.positions) for _ in range(FOOD_COUNT)]
    score = 0
    base_fps = FPS
    speed_mod = 0.0  # cumulative speed modifier (positive = faster, negative = slower)
    active_effects = []  # list of tuples (type, end_time)

    running = True

    while running:
        # Compute FPS from current effects
        current_time = time.time()
        active_effects = [(typ, end) for (typ, end) in active_effects if current_time < end]
        speed_mod = sum(0.6 if t == "speed" else -0.4 for (t, _) in active_effects)
        current_fps = max(4, base_fps * (1 + speed_mod))

        clock.tick(current_fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w: snake.change_direction("UP")
                elif event.key == pygame.K_s: snake.change_direction("DOWN")
                elif event.key == pygame.K_a: snake.change_direction("LEFT")
                elif event.key == pygame.K_d: snake.change_direction("RIGHT")

        # Move
        alive = snake.move()
        if not alive:
            game_over(score)
            return

        # Handle food collisions
        for food in foods[:]:
            if snake.positions[0] == food.position:
                foods.remove(food)
                foods.append(Food(snake.positions))

                multiplier = 1
                if any(t == "speed" for (t, _) in active_effects):
                    multiplier = SPEED_SCORE_MULTIPLIER

                if food.effect == "normal":
                    snake.grow_amount += myvar
                    score += FOOD_SCORE_VALUE * multiplier

                elif food.effect == "speed":
                    snake.grow_amount += myvar
                    active_effects.append(("speed", current_time + FOOD_EFFECT_DURATION))
                    score += FOOD_SCORE_VALUE * 2 * multiplier

                elif food.effect == "slow":
                    snake.grow_amount += myvar
                    active_effects.append(("slow", current_time + FOOD_EFFECT_DURATION))
                    score += FOOD_SCORE_VALUE * multiplier

                elif food.effect == "grow":
                    snake.grow_amount += myvar
                    score += FOOD_SCORE_VALUE * 3 * multiplier

        # Drawing
        screen.fill(COLOR_BACKGROUND)
        draw_grid()
        snake.draw(screen)
        for food in foods:
            food.draw(screen)

        # UI info
        draw_text(f"Score: {score}", font, COLOR_TEXT, screen, 10, 10)
        if any(t == "speed" for (t, _) in active_effects):
            draw_text("⚡ SPEED BOOST!", font, (255, 255, 100), screen, 10, 50)
        if any(t == "slow" for (t, _) in active_effects):
            draw_text("🐢 SLOW!", font, (100, 150, 255), screen, 10, 90)

        pygame.display.flip()

# ============================================================
#                  💀 GAME OVER
# ============================================================

def game_over(score):
    while True:
        screen.fill((10, 10, 20))
        draw_text("GAME OVER", title_font, (255, 50, 50), screen, WINDOW_WIDTH // 2, WINDOW_HEIGHT // 3, center=True)
        draw_text(f"Score: {score}", font, COLOR_TEXT, screen, WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2, center=True)
        draw_text("Press [R] to Restart or [Q] to Quit", font, (200, 200, 200),
                  screen, WINDOW_WIDTH // 2, WINDOW_HEIGHT * 0.65, center=True)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    main()
                    return
                elif event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

# ============================================================
#                  🚀 START GAME
# ============================================================

if __name__ == "__main__":
    main()
