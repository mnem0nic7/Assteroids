# Import required modules
import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS

class Shot(CircleShape):
    """
    Shot class representing bullets fired by the player in the Asteroids game.
    Inherits from CircleShape to get collision detection and basic position/velocity.
    """
    
    def __init__(self, x, y):
        """
        Initialize a shot at the specified position.
        
        Args:
            x (float): Initial x-coordinate
            y (float): Initial y-coordinate
        """
        # Call parent constructor with position and shot radius
        super().__init__(x, y, SHOT_RADIUS)
    
    def draw(self, screen):
        """
        Draw the shot as a small white circle on the screen.
        
        Args:
            screen: Pygame surface to draw on
        """
        # Draw a white filled circle for the bullet
        pygame.draw.circle(screen, "white", self.position, self.radius)
    
    def update(self, dt):
        """
        Update the shot's position based on its velocity.
        
        Args:
            dt (float): Delta time (time since last frame) in seconds
        """
        # Move the shot by adding velocity scaled by delta time to position
        self.position += self.velocity * dt
