"""
CircleShape - Base Class Module

Provides a base class for all circular game objects in the Asteroids game.
This includes the player ship, asteroids, and bullets - all of which use
circular collision detection for simplicity and performance.

This class inherits from pygame.sprite.Sprite to provide sprite group
functionality for efficient collision detection and batch operations.
"""

import pygame

# Base class for all circular game objects (player, asteroids, bullets)
class CircleShape(pygame.sprite.Sprite):
    """
    Base class for game objects that use circular collision detection.
    
    Provides common functionality like position, velocity, radius, and
    collision detection that all circular game objects need.
    
    Inherits from pygame.sprite.Sprite for sprite group functionality.
    """
    
    def __init__(self, x, y, radius):
        """
        Initialize a circular game object.
        
        Args:
            x (float): Initial x-coordinate
            y (float): Initial y-coordinate  
            radius (float): Collision radius in pixels
        """
        # Check if this object should be added to sprite containers
        # This allows for automatic sprite group management
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        # Position as a 2D vector for easy mathematical operations
        self.position = pygame.Vector2(x, y)
        
        # Velocity vector - how fast and in what direction the object moves
        self.velocity = pygame.Vector2(0, 0)
        
        # Collision radius - used for circular collision detection
        self.radius = radius

    def draw(self, screen):
        """
        Draw the object on the screen.
        
        This is an abstract method that must be overridden by subclasses
        to define how each specific object type should be rendered.
        
        Args:
            screen: Pygame surface to draw on
        """
        # Sub-classes must override this method to implement their own drawing
        pass

    def update(self, dt):
        """
        Update the object's state for one frame.
        
        This is an abstract method that must be overridden by subclasses
        to define how each object type should update (movement, animation, etc.).
        
        Args:
            dt (float): Delta time (time since last frame) in seconds
        """
        # Sub-classes must override this method to implement their own update logic
        pass