SCREEN_WIDTH = 1280  # the screen width will be 1280 pixels
SCREEN_HEIGHT = 720  # the screen height will be 720 pixels

ASTEROID_MIN_RADIUS = 20  # the minimum radius of an asteroid will be 20 pixels long
ASTEROID_KINDS = 3  # there will be 3 kinds of asteroids
ASTEROID_SPAWN_RATE = 0.8  # asteroids will spawn every 0.8 seconds
ASTEROID_MAX_RADIUS = ASTEROID_MIN_RADIUS * ASTEROID_KINDS

# the maximum radius of an asteroid is set to the minimum radius of the asteroid times the number of asteroids
# there are 3 kinds of asteroids in the base game, leading to the max radius equating to three times the asteroid minimum radius
# the asteroids max radius is measured in pixels

PLAYER_RADIUS = 20  #  the player hitbox will be 20 pixels long
PLAYER_TURN_SPEED = 300  #  the player will turn 300 (Insert units here), pixels per ???
PLAYER_SPEED = 200  #  the player will move 200 (Insert units here), pixels per ???
SHOT_RADIUS = 5  # the radius of each shot will be 5 pixels
PLAYER_SHOOT_SPEED = 500  # each shot will move 500 (Insert units here), pixels per ???
