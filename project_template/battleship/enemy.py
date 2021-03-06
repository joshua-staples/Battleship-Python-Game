import constants
import arcade


class Enemy(arcade.Sprite):
    scale = 0.5

    #uses sprite from arcade library resources
    def __init__(self, image_file_name, scale):
        super().__init__(image_file_name, scale=scale)
        self.size = 0
    def update(self):
        #updates the position of the enemy sprite
        super().update()
        if self.center_x < constants.LEFT_LIMIT:
            self.center_x = constants.RIGHT_LIMIT
        if self.center_x > constants.RIGHT_LIMIT:
            self.center_x = constants.LEFT_LIMIT
        if self.center_y > constants.TOP_LIMIT:
            self.center_y = constants.BOTTOM_LIMIT
        if self.center_y < constants.BOTTOM_LIMIT:
            self.center_y = constants.TOP_LIMIT