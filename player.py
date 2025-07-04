# Import required modules
import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN
from shot import Shot

class Player(CircleShape):
    """
    Player class representing the player's spaceship in the Asteroids game.
    Inherits from CircleShape to get collision detection and basic position/velocity.
    """
    
    def __init__(self, x, y):
        """
        Initialize the player at the specified position.
        
        Args:
            x (int): Initial x-coordinate
            y (int): Initial y-coordinate
        """
        # Call parent constructor with player radius
        super().__init__(x, y, PLAYER_RADIUS)
        # Initialize rotation angle (in degrees)
        self.rotation = 0
        # Initialize shooting cooldown timer
        self.shoot_timer = 0

    def triangle(self):
        """
        Calculate the three points of the triangular spaceship based on current position and rotation.
        
        Returns:
            list: List of three pygame.Vector2 points representing the triangle vertices
        """
        # Calculate forward direction vector based on current rotation
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        # Calculate right direction vector (perpendicular to forward)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        
        # Calculate the three triangle points
        a = self.position + forward * self.radius  # Front tip of the ship
        b = self.position - forward * self.radius - right  # Bottom left
        c = self.position - forward * self.radius + right  # Bottom right
        return [a, b, c]
    
    def draw(self, screen):
        """
        Draw the player as a white triangle on the screen.
        
        Args:
            screen: Pygame surface to draw on
        """
        # Draw a white triangle outline with line width of 2
        pygame.draw.polygon(screen, "white", self.triangle(), 2)
    
    def rotate(self, dt):
        """
        Rotate the player by the turn speed multiplied by delta time.
        
        Args:
            dt (float): Delta time (time since last frame) in seconds
        """
        # Update rotation based on turn speed and delta time
        self.rotation += PLAYER_TURN_SPEED * dt
    
    def move(self, dt):
        """
        Move the player forward in the direction they are facing.
        
        Args:
            dt (float): Delta time (time since last frame) in seconds
        """
        # Create a unit vector pointing up (0, 1)
        # Rotate it by the player's current rotation to get forward direction
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        # Move the player by adding the scaled forward vector to position
        self.position += forward * PLAYER_SPEED * dt
    
    def shoot(self):
        """
        Create a new shot at the player's position moving in the direction they are facing.
        Only shoots if the cooldown timer has expired.
        """
        # Check if enough time has passed since the last shot
        if self.shoot_timer > 0:
            return  # Still on cooldown, don't shoot
        
        # Create a new shot at the player's current position
        shot = Shot(self.position.x, self.position.y)
        
        # Calculate the direction the player is facing
        # Start with a unit vector pointing up (0, 1)
        direction = pygame.Vector2(0, 1).rotate(self.rotation)
        
        # Set the shot's velocity by scaling the direction vector
        shot.velocity = direction * PLAYER_SHOOT_SPEED
        
        # Set the cooldown timer to prevent rapid firing
        self.shoot_timer = PLAYER_SHOOT_COOLDOWN
    
    def update(self, dt):
        """
        Update the player based on keyboard input.
        
        Args:
            dt (float): Delta time (time since last frame) in seconds
        """
        # Decrease the shooting cooldown timer
        if self.shoot_timer > 0:
            self.shoot_timer -= dt
        
        # Get the current state of all keyboard keys
        keys = pygame.key.get_pressed()

        # Rotate left when 'A' key is pressed (negative dt for counter-clockwise)
        if keys[pygame.K_a]:
            self.rotate(-dt)
        # Rotate right when 'D' key is pressed (positive dt for clockwise)
        if keys[pygame.K_d]:
            self.rotate(dt)
        # Move forward when 'W' key is pressed
        if keys[pygame.K_w]:
            self.move(dt)
        # Move backward when 'S' key is pressed (negative dt for reverse)
        if keys[pygame.K_s]:
            self.move(-dt)
        # Shoot when spacebar is pressed (respects cooldown timer)
        if keys[pygame.K_SPACE]:
            self.shoot()
