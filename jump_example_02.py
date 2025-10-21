# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_jump.md
#
# How to make a character jump in Pygame?
# https://stackoverflow.com/questions/70591591/how-to-make-a-character-jump-in-pygame/70591592#70591592
#
# How to make a character jump in Pygame?
# https://stackoverflow.com/questions/67667103/how-can-i-do-a-double-jump-in-pygame/67667585#67667585

# JUMPING BALL GAME - Like having a pet bouncy ball! 🏀

import pygame

# Start up pygame (like turning on the game console)
pygame.init()
# Make a window that's 300x300 pixels (like a square TV screen)
window = pygame.display.set_mode((300, 300))
# Make a clock to control how fast the game runs
clock = pygame.time.Clock()

# CREATE THE RED BALL (our bouncy character!)
player = pygame.sprite.Sprite()  # Make a new sprite (game character)
player.image = pygame.Surface((30, 30), pygame.SRCALPHA)  # Make a 30x30 invisible square
pygame.draw.circle(player.image, (255, 0, 0), (15, 15), 15)  # Draw a red circle on it
player.rect = player.image.get_rect(center = (150, 235))  # Put the ball near the bottom center
all_sprites = pygame.sprite.Group([player])  # Put the ball in a group so we can draw it

# IMPORTANT VARIABLES (the magic numbers that control everything!)
y, vel_y = player.rect.bottom, 0  # y = where ball is up/down, vel_y = how fast ball moves up/down (0 = sitting still)
vel = 5  # How fast the ball moves left/right when you press arrow keys (5 tiny steps)
ground_y = 250  # Where the floor is (250 pixels from the top of the screen)
acceleration = 10  # How much OOMPH we give the ball when jumping (bigger = higher jumps!)
gravity = 0.5  # Invisible force that pulls everything down (like real gravity but gentler)

# MAIN GAME LOOP (this runs over and over, like a heartbeat!)
run = True  # Keep the game running
while run:  # Do this forever until we quit
    clock.tick(100)  # Run the game 100 times per second (makes it smooth!)
    acc_y = gravity  # Always pull the ball down with gravity (unless we're jumping!)
    # CHECK FOR BUTTON PRESSES AND EVENTS
    for event in pygame.event.get():  # Look for things the player did
        if event.type == pygame.QUIT:  # Did they try to close the window?
            run = False  # Stop the game
        if event.type == pygame.KEYDOWN:  # Did they press a key?
            # JUMPING: Only jump if ball is on ground (vel_y = 0) AND they pressed SPACE
            if vel_y == 0 and event.key == pygame.K_SPACE:
                acc_y = -acceleration  # Give big upward push! (negative = up, positive = down)

    # MOVING LEFT AND RIGHT (like rolling a ball)
    keys = pygame.key.get_pressed()  # Check which keys are being held down right now
    # Move left/right: RIGHT key = +1, LEFT key = +1, both = 0, neither = 0
    # % 300 makes ball wrap around screen (go off right side = appear on left side!)
    player.rect.centerx = (player.rect.centerx + (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * vel) % 300
    
    # THE PHYSICS MAGIC! (How jumping and falling works)
    vel_y += acc_y  # Change how fast we're moving up/down (gravity makes us fall faster)
    y += vel_y  # Actually move the ball up or down based on vel_y
    
    # Did the ball hit the ground? (went too low?)
    if y > ground_y:
        y = ground_y  # Put ball back on the ground
        vel_y = 0  # Stop moving up/down (no more bouncing)
        acc_y = 0  # Stop accelerating (until next jump)
    
    player.rect.bottom = round(y)  # Update the ball's position on screen

    # DRAW EVERYTHING ON THE SCREEN (like painting a picture!)
    window.fill((0, 0, 64))  # Fill screen with dark blue color (like night sky)
    pygame.draw.rect(window, (64, 64, 64), (0, 250, 300, 100))  # Draw gray ground/floor
    all_sprites.draw(window)  # Draw the red ball on top of everything
    pygame.display.flip()  # Show the finished picture to the player

# GAME OVER - Clean up and close everything
pygame.quit()  # Turn off pygame
exit()  # Close the program completely