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

# =============================================================================
# STEP 1: CREATE THE PERSON CLASS
# =============================================================================
# Tell the student: "Let's create a class for our character Rob. 
# A class is like a blueprint that defines what Rob can do and what properties he has."

class Person:
    """
    STEP 1A: Explain to student: "This is our Person class for Rob.
    It defines all the properties Rob has (like position, size, speed) 
    and all the things Rob can do (like move, jump, draw himself)."
    """
    
    def __init__(self, x, y):
        """
        STEP 1B: Explain to student: "The __init__ method is like a constructor.
        It runs when we create a new Person object. It sets up Rob's starting properties."
        """
        # TEACHING POINT: "These are Rob's properties - his position, size, and abilities"
        self.x = x  # Rob's x position
        self.y = y  # Rob's y position
        self.width = 30  # Rob's width
        self.height = 30  # Rob's height
        self.speed = 5  # How fast Rob moves left/right
        self.jump_speed = 15  # How fast Rob jumps up
        self.velocity_y = 0  # Rob's current vertical speed
        self.on_ground = False  # Is Rob touching the ground?
        self.gravity = 0.8  # How fast Rob falls down
        
        # TEACHING POINT: "We create a rectangle to represent Rob for collision detection"
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
    
    def move_left(self):
        """
        STEP 1C: Explain to student: "This method makes Rob move left.
        We check if he's not at the left edge of the screen first."
        """
        # TEACHING POINT: "We check boundaries to prevent Rob from going off screen"
        if self.x > 0:  # If not at left edge
            self.x -= self.speed
            self.rect.x = self.x  # Update the collision rectangle
    
    def move_right(self):
        """
        STEP 1D: Explain to student: "This method makes Rob move right.
        We check if he's not at the right edge of the screen first."
        """
        # TEACHING POINT: "We check boundaries to prevent Rob from going off screen"
        if self.x < SCREEN_WIDTH - self.width:  # If not at right edge
            self.x += self.speed
            self.rect.x = self.x  # Update the collision rectangle
    
    def jump(self):
        """
        STEP 1E: Explain to student: "This method makes Rob jump.
        He can only jump when he's on the ground or on an obstacle."
        """
        # TEACHING POINT: "Rob can only jump when he's touching something solid"
        if self.on_ground:
            self.velocity_y = -self.jump_speed  # Negative velocity goes up
            self.on_ground = False  # He's no longer on the ground
    
    def update(self):
        """
        STEP 1F: Explain to student: "This method updates Rob's position every frame.
        It handles gravity and makes sure Rob falls down naturally."
        """
        # TEACHING POINT: "Gravity pulls Rob down every frame"
        self.velocity_y += self.gravity  # Gravity increases downward speed
        self.y += self.velocity_y  # Move Rob based on his velocity
        
        # TEACHING POINT: "Check if Rob hits the ground"
        if self.y >= SCREEN_HEIGHT - self.height:
            self.y = SCREEN_HEIGHT - self.height  # Keep him on screen
            self.velocity_y = 0  # Stop falling
            self.on_ground = True  # He's on the ground
        
        # TEACHING POINT: "Update the collision rectangle to match Rob's position"
        self.rect.y = self.y
    
    def draw(self, screen):
        """
        STEP 1G: Explain to student: "This method draws Rob on the screen.
        We use pygame.draw.rect to draw a blue rectangle for Rob."
        """
        # TEACHING POINT: "We draw Rob as a blue rectangle"
        pygame.draw.rect(screen, BLUE, (self.x, self.y, self.width, self.height))

# =============================================================================
# STEP 2: CREATE THE OBSTACLE CLASS
# =============================================================================
# Tell the student: "Now let's create a simple obstacle that Rob can jump on."

class Obstacle:
    """
    STEP 2A: Explain to student: "This class represents the obstacle block.
    It's simpler than Rob because it doesn't move or jump."
    """
    
    def __init__(self, x, y, width, height):
        """
        STEP 2B: Explain to student: "The obstacle just needs position and size.
        It will be a red rectangle that Rob can jump on."
        """
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pygame.Rect(x, y, width, height)
    
    def draw(self, screen):
        """
        STEP 2C: Explain to student: "This draws the obstacle as a red rectangle."
        """
        pygame.draw.rect(screen, RED, (self.x, self.y, self.width, self.height))

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
    pygame.display.set_caption("Rob's Jumping Game")
    clock = pygame.time.Clock()
    
    # TEACHING POINT: "Create our game objects"
    rob = Person(50, SCREEN_HEIGHT - 80)  # Create Rob near the bottom left
    obstacle = Obstacle(SCREEN_WIDTH // 2 - 25, SCREEN_HEIGHT - 100, 50, 50)  # Obstacle in middle
    
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
                    rob.jump()  # Jump when space is pressed
        
        # TEACHING POINT: "Check for continuous key presses (left/right movement)"
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            rob.move_left()
        if keys[pygame.K_RIGHT]:
            rob.move_right()
        
        # TEACHING POINT: "Update Rob's position (handle gravity and jumping)"
        rob.update()
        
        # TEACHING POINT: "Check collision between Rob and the obstacle"
        if rob.rect.colliderect(obstacle.rect):
            # TEACHING POINT: "If Rob is above the obstacle, he can land on it"
            if rob.velocity_y > 0 and rob.y < obstacle.y:
                rob.y = obstacle.y - rob.height
                rob.velocity_y = 0
                rob.on_ground = True
        
        # TEACHING POINT: "Clear the screen and draw everything"
        screen.fill(WHITE)  # Fill with white background
        rob.draw(screen)  # Draw Rob
        obstacle.draw(screen)  # Draw the obstacle
        
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
    main()

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
