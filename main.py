import pygame
from constants import *

def main():
    print("Starting Asteroids!")
    
    # Initialize all pygame modules (graphics, sound, etc.)
    pygame.init()
    
    # Create the game window with specified dimensions from constants
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids")
    
    # Main game loop - runs continuously until the game is closed
    while True:
        
        # Event handling - process all user input events
        for event in pygame.event.get():
            # Check if user clicked the window's close button (X)
            if event.type == pygame.QUIT:
                return  # Exit the function and end the game
                
        # Clear the screen by filling it with black color
        screen.fill("black")
        
        # Update the display to show all rendered changes
        pygame.display.flip()

# Entry point - only run main() if this script is executed directly
if __name__ == "__main__":
    main()
