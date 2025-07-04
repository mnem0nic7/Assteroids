# Game constants for the Asteroids game
# All values are carefully balanced for optimal gameplay experience

# Screen/Window dimensions
SCREEN_WIDTH = 1280  # Width of the game window in pixels
SCREEN_HEIGHT = 720  # Height of the game window in pixels

# Asteroid properties
ASTEROID_MIN_RADIUS = 20  # Smallest possible asteroid radius in pixels
ASTEROID_KINDS = 3  # Number of different asteroid sizes (small, medium, large)
ASTEROID_SPAWN_RATE = 0.8  # Time in seconds between asteroid spawns
ASTEROID_MAX_RADIUS = ASTEROID_MIN_RADIUS * ASTEROID_KINDS  # Largest asteroid radius (60 pixels)

# Player spaceship properties
PLAYER_RADIUS = 20  # Collision radius of the player ship in pixels
PLAYER_TURN_SPEED = 300  # Player rotation speed in degrees per second
PLAYER_SPEED = 200  # Player movement speed in pixels per second
PLAYER_SHOOT_SPEED = 500  # Speed of bullets fired by the player in pixels per second
PLAYER_SHOOT_COOLDOWN = 0.3  # Time in seconds between shots

# Shot/Bullet properties
SHOT_RADIUS = 5  # Radius of player bullets in pixels
PLAYER_SPEED = 200  # Player movement speed in pixels per second