import constants
import math
import arcade

class Player(arcade.Sprite):
    """
    loads a sprite from the arcade library
    """
    def __init__(self, filename, scale):
        super().__init__(filename, scale)

        # cordenates and angle from the parent class
        self.thrust = 0
        self.speed = 0
        self.max_speed = 4
        self.drag = 0.05
        self.respawning = 0

        # Mark that we are respawning.
        self.respawn()

    def respawn(self):
        #method called when user is killed
        self.respawning = 1
        self.center_x = constants.WIDTH / 2
        self.center_y = constants.HEIGHT / 2
        self.center_x = SCREEN_WIDTH / 2
        self.center_y = SCREEN_HEIGHT / 2
        self.angle = 0

    def update(self):
        #update frames
        if self.respawning:
            self.respawning += 1
            self.alpha = self.respawning
            if self.respawning > 250:
                self.respawning = 0
                self.alpha = 255
        if self.speed > 0:
            self.speed -= self.drag
            if self.speed < 0:
                self.speed = 0

        if self.speed < 0:
            self.speed += self.drag
            if self.speed > 0:
                self.speed = 0

        self.speed += self.thrust
        if self.speed > self.max_speed:
            self.speed = self.max_speed
        if self.speed < -self.max_speed:
            self.speed = -self.max_speed

        self.change_x = -math.sin(math.radians(self.angle)) * self.speed
        self.change_y = math.cos(math.radians(self.angle)) * self.speed

        self.center_x += self.change_x
        self.center_y += self.change_y

        # If the player goes off-screen, move it to the other side of the window
        if self.right < 0:
            self.left = constants.WIDTH

        if self.left > constants.WIDTH:
            self.right = 0

        if self.bottom < 0:
            self.top = constants.HEIGHT

        if self.top > constants.HEIGHT:
            self.bottom = 0

        #call update method from parent class
        super().update()
            self.left = SCREEN_WIDTH

        if self.left > SCREEN_WIDTH:
            self.right = 0

        if self.bottom < 0:
            self.top = SCREEN_HEIGHT

        if self.top > SCREEN_HEIGHT:
            self.bottom = 0

        #call update method from parent class
        super().update()
