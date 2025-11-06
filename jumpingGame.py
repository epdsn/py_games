"""
Simple Jumping Game with Rob
============================

A pygame where Rob can jump and move around with collision detection.
- Space bar: Jump
- Left/Right arrows: Move left/right
- Rob can jump on the obstacle block
- Rob cannot move past screen boundaries

TEACHING GUIDE FOR STUDENT DEVELOPMENT
======================================

This game teaches:
1. Object-oriented programming with classes
2. Game physics (gravity, jumping)
3. Collision detection
4. Event handling in pygame
5. Game loop structure

Follow the numbered steps to guide the student through development.
"""

import pygame
import sys
import traceback

# Initialize Pygame
pygame.init()

# Game constants
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Import the refactored classes from separate modules
from jumpingGame_Person import Person
from jumpingGame_Obstacle import Obstacle
from jumpingGame_Enemy import Enemy

# =============================================================================
# STEP 3: SET UP THE GAME
# =============================================================================
# Tell the student: "Now let's set up the main game. This includes creating the screen,
# setting up the game loop, and handling user input."

def main():
    """
    STEP 3A: Explain to student: "This is the main function that runs our game.
    It sets up everything and contains the main game loop."
    """
    # TEACHING POINT: "Create the game window"
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Rob's Jumping Game - Now with Enemies!")
    clock = pygame.time.Clock()
    
    # TEACHING POINT: "Create our game objects"
    rob = Person(50, SCREEN_HEIGHT - 80)  # Create Rob near the bottom left
    obstacle = Obstacle(SCREEN_WIDTH // 2 - 25, SCREEN_HEIGHT - 100, 50, 50)  # Obstacle in middle
    
    # TEACHING POINT: "Create enemies that patrol different areas"
    enemies = [
        Enemy(100, SCREEN_HEIGHT - 50, 80, 200),      # Ground patrol enemy
        Enemy(250, SCREEN_HEIGHT - 130, 200, 350),    # Obstacle area patrol
        Enemy(350, SCREEN_HEIGHT - 50, 300, 450),     # Right side patrol
    ]
    
    # Game state variables
    game_over = False
    font = pygame.font.Font(None, 74)
    small_font = pygame.font.Font(None, 36)
    
    # =============================================================================
    # STEP 4: MAIN GAME LOOP
    # =============================================================================
    # Tell the student: "The game loop runs forever until the player quits.
    # Each time through the loop, we: 1) Handle events, 2) Update game state, 3) Draw everything"
    
    running = True
    while running:
        # TEACHING POINT: "Handle events (keyboard input, window close, etc.)"
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if not game_over:
                        rob.jump()  # Jump when space is pressed
                    else:
                        # Reset game
                        rob.x = 50
                        rob.y = SCREEN_HEIGHT - 80
                        rob.velocity_y = 0
                        rob.on_ground = False
                        game_over = False
                elif event.key == pygame.K_r and game_over:
                    # Reset game with R key
                    rob.x = 50
                    rob.y = SCREEN_HEIGHT - 80
                    rob.velocity_y = 0
                    rob.on_ground = False
                    game_over = False
        
        if not game_over:
            # TEACHING POINT: "Check for continuous key presses (left/right movement)"
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                rob.move_left()
            if keys[pygame.K_RIGHT]:
                rob.move_right()
            
            # TEACHING POINT: "Update Rob's position (handle gravity and jumping)"
            rob.update()
            
            # TEACHING POINT: "Update all enemies"
            for enemy in enemies:
                enemy.update()
            
            # TEACHING POINT: "Check collision between Rob and the obstacle"
            if rob.rect.colliderect(obstacle.rect):
                # TEACHING POINT: "If Rob is above the obstacle, he can land on it"
                if rob.velocity_y > 0 and rob.y < obstacle.y:
                    rob.y = obstacle.y - rob.height
                    rob.velocity_y = 0
                    rob.on_ground = True
            
            # TEACHING POINT: "Check collision between Rob and enemies"
            for enemy in enemies:
                if rob.rect.colliderect(enemy.rect):
                    game_over = True
                    print("Game Over! Rob touched an enemy!")
        
        # TEACHING POINT: "Clear the screen and draw everything"
        screen.fill(WHITE)  # Fill with white background
        
        if not game_over:
            rob.draw(screen)  # Draw Rob
        else:
            # Draw Rob in a different color when game over
            pygame.draw.rect(screen, (100, 100, 100), (rob.x, rob.y, rob.width, rob.height))
        
        obstacle.draw(screen)  # Draw the obstacle
        
        # Draw all enemies
        for enemy in enemies:
            enemy.draw(screen)
        
        # Draw game over screen
        if game_over:
            game_over_text = font.render("GAME OVER!", True, RED)
            restart_text = small_font.render("Press SPACE or R to restart", True, BLACK)
            
            # Center the text
            game_over_rect = game_over_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 - 50))
            restart_rect = restart_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 + 20))
            
            screen.blit(game_over_text, game_over_rect)
            screen.blit(restart_text, restart_rect)
        
        # Draw instructions
        if not game_over:
            instructions = small_font.render("Arrows: Move, Space: Jump, Avoid red enemies!", True, BLACK)
            screen.blit(instructions, (10, 10))
        
        # TEACHING POINT: "Update the display and control frame rate"
        pygame.display.flip()
        clock.tick(FPS)  # Limit to 60 FPS
    
    # TEACHING POINT: "Clean up when the game ends"
    pygame.quit()
    sys.exit()

# =============================================================================
# STEP 5: RUN THE GAME
# =============================================================================
# Tell the student: "This is where we start our game. The if __name__ == '__main__'
# check makes sure the game only runs when we run this file directly."

if __name__ == "__main__":
    try:
        main()
    except Exception:
        # Print traceback to console so we can see why the game quits
        traceback.print_exc()
        try:
            input("An error occurred. Press Enter to exit...")
        except Exception:
            pass

# =============================================================================
# TEACHING GUIDE: NEXT STEPS FOR STUDENT DEVELOPMENT
# =============================================================================
"""
INSTRUCTOR NOTES: Use these steps to guide your student through improvements

PHASE 1: UNDERSTANDING THE BASICS
==================================
Tell the student: "Let's understand how this game works!"

Step 1: Run the Game
- "First, let's run the game and see what happens"
- Have them test the controls: left/right arrows and space bar
- Ask them to explain what they see

Step 2: Explain the Game Loop
- "Every game has a loop that runs forever"
- "Each time through the loop: 1) Check for input, 2) Update game state, 3) Draw everything"
- Point out the while running loop

Step 3: Understand Classes
- "Rob is an object with properties (x, y, speed) and methods (move, jump)"
- "The obstacle is a simpler object that just sits there"
- Ask them to identify Rob's properties and methods

PHASE 2: BASIC IMPROVEMENTS
============================
Tell the student: "Now let's make the game better!"

Step 4: Add More Obstacles
- "Let's add more blocks for Rob to jump on"
- Create a list of obstacles
- Add collision detection for all obstacles

Step 5: Improve Rob's Appearance
- "Let's make Rob look more like a person"
- Draw a simple face or use a sprite
- Add different colors for different states (jumping, standing)

Step 6: Add Sound Effects
- "Let's add sounds when Rob jumps or lands"
- Use pygame.mixer for sound effects
- Add background music

PHASE 3: INTERMEDIATE FEATURES
===============================
Tell the student: "Ready for some advanced features?"

Step 7: Add Animation
- "Let's make Rob's movement smoother"
- Add sprite animation for walking
- Add a jumping animation

Step 8: Add Game Mechanics
- "Let's add a goal or objective"
- Add collectible items
- Add a score system

Step 9: Improve Physics
- "Let's make the jumping feel more realistic"
- Adjust gravity and jump strength
- Add momentum and friction

PHASE 4: ADVANCED FEATURES
===========================
Tell the student: "Now let's make it really cool!"

Step 10: Add Multiple Levels
- "Let's create different levels with different obstacles"
- Design level layouts
- Add level progression

Step 11: Add Enemies or Challenges
- "Let's add moving obstacles or enemies"
- Create enemy classes
- Add collision detection for enemies

Step 12: Add Power-ups
- "Let's add special abilities for Rob"
- Create power-up classes
- Add temporary abilities (double jump, speed boost)

BONUS CHALLENGES FOR ADVANCED STUDENTS
======================================
- Add a level editor
- Create a multiplayer mode
- Add particle effects
- Create a story mode with cutscenes
- Add save/load functionality
- Create a mobile version

TEACHING TIPS:
- Let the student run the game after each change
- Ask them to explain what each part does
- Encourage them to experiment with values (speed, gravity, etc.)
- Have them test edge cases (jumping off screen, etc.)
- Ask them to think of new features they'd like to add
- Let them break things and then fix them together
"""
