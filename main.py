"""
Asteroids Game - Main Module

A classic arcade-style space shooter game built with Pygame.
The player controls a triangular spaceship that can rotate and must avoid asteroids.

Controls:
- A: Rotate left
- D: Rotate right
- Close window or Ctrl+C to quit

Author: Boot.dev Asteroids Project
"""

# Import required modules
import pygame
from constants import *  # Import all game constants
from player import Player  # Import the Player class

def main():
    """
    Main game function that initializes pygame and runs the game loop.
    Handles all game logic including initialization, event processing, 
    updating game objects, and rendering.
    """
    print("Starting Asteroids!")
    
    # Initialize all pygame modules (graphics, sound, input, etc.)
    pygame.init()
    
    # Create a clock object to control the game's frame rate
    # This ensures the game runs at a consistent speed across different hardware
    clock = pygame.time.Clock()
    
    # Create the game window with dimensions defined in constants
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids")  # Set the window title
    
    # Initialize the player spaceship in the center of the screen
    x = SCREEN_WIDTH / 2   # Horizontal center
    y = SCREEN_HEIGHT / 2  # Vertical center
    player = Player(x, y)
    
    # Main game loop - runs continuously until the game is closed
    # This is the heart of the game where all updates and rendering happen
    while True:
        # Control frame rate at 60 FPS and calculate delta time
        # Delta time is the time elapsed since the last frame (in seconds)
        # This makes movement frame-rate independent
        dt = clock.tick(60) / 1000.0  # Convert milliseconds to seconds
        
        # Event handling - process all user input events in the event queue
        for event in pygame.event.get():
            # Check if user clicked the window's close button (X)
            if event.type == pygame.QUIT:
                return  # Exit the function and end the game
                
        # Clear the screen by filling it with black color
        # This erases everything from the previous frame
        screen.fill("black")
        
        # Update game objects
        # Update player position/rotation based on input and delta time
        player.update(dt)
        
        # Render all game objects
        # Draw the player spaceship on the screen
        player.draw(screen)
        
        # Update the display to show all rendered changes
        # This swaps the back buffer with the front buffer (double buffering)
        pygame.display.flip()

# Entry point - only run main() if this script is executed directly
# This prevents main() from running if this file is imported as a module
if __name__ == "__main__":
    main()
