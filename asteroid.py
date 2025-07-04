# Import required modules
import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    """
    Asteroid class representing asteroids in the Asteroids game.
    Inherits from CircleShape to get collision detection and basic position/velocity.
    """
    
    def __init__(self, x, y, radius):
        """
        Initialize an asteroid at the specified position with given radius.
        
        Args:
            x (float): Initial x-coordinate
            y (float): Initial y-coordinate
            radius (float): Radius of the asteroid
        """
        # Call parent constructor with position and radius
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        """
        Draw the asteroid as a white circle outline on the screen.
        
        Args:
            screen: Pygame surface to draw on
        """
        # Draw a white circle outline with line width of 2
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def update(self, dt):
        """
        Update the asteroid's position based on its velocity.
        
        Args:
            dt (float): Delta time (time since last frame) in seconds
        """
        # Move the asteroid by adding velocity scaled by delta time to position
        self.position += self.velocity * dt
    
    def split(self):
        """
        Split the asteroid into two smaller asteroids when destroyed.
        Large asteroids become two medium asteroids, medium asteroids become two small asteroids,
        and small asteroids are simply destroyed.
        """
        # Always destroy this asteroid first
        self.kill()
        
        # If this is the smallest asteroid size, just disappear
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        # Generate a random split angle between 20 and 50 degrees
        random_angle = random.uniform(20, 50)
        
        # Create two new velocity vectors by rotating the current velocity
        new_velocity_1 = self.velocity.rotate(random_angle)
        new_velocity_2 = self.velocity.rotate(-random_angle)
        
        # Calculate the new radius for the smaller asteroids
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        
        # Create two new asteroids at the current position with smaller radius
        asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
        
        # Set their velocities to the rotated vectors, scaled up by 1.2 for faster movement
        asteroid_1.velocity = new_velocity_1 * 1.2
        asteroid_2.velocity = new_velocity_2 * 1.2
