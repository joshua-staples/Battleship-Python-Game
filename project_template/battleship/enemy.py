import arcade

'''
    author: David Del Sol
    disclaimer: some of the functionality in this class
    has been inspired by previous games that I built using the arcade library
    both for pleasure
    
    the main behavior of the enemies was inspired from a modified version of the space invaders game
    an original project designed by Brother Burton for CS241 which is designed to be completed by the students
    this project was later modified over christmas break just for fun to include original code designed by myself
    as well as a combination of code taking from the following tutorials and websites in order to find the desired
    design and functionality.

    the youtube playlist on the
    arcade library https://www.youtube.com/watch?v=2qP1M1Nf__w&list=PL1P11yPQAo7pPlDlFEaL3IUbcWnnPcALI
    The arcade library's official documentation site https://arcade.academy/get_started.html
    resources from https://arcade.academy/resources.html
    as well as other online resources such as stackoverflow


    For more information please see: https://github.com/daviddelsol1998/Slime_Space_invaders
    '''


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

STARTING_ENEMY_COUNT = 10
SCALE = 0.5
OFFSCREEN_SPACE = 300
MUSIC_VOLUME = 0.5


LEFT_LIMIT = -OFFSCREEN_SPACE
RIGHT_LIMIT = SCREEN_WIDTH + OFFSCREEN_SPACE
BOTTOM_LIMIT = -OFFSCREEN_SPACE
TOP_LIMIT = SCREEN_HEIGHT + OFFSCREEN_SPACE


class Enemy_icon(arcade.Sprite):
    #uses sprite from arcade library resources

    def __init__(self, image_file_name, scale):
        super().__init__(image_file_name, scale=scale)
        self.size = 0

    def update(self):
        #updates the position of the Enemy_icon sprite
        super().update()
        if self.center_x < LEFT_LIMIT:
            self.center_x = RIGHT_LIMIT
        if self.center_x > RIGHT_LIMIT:
            self.center_x = LEFT_LIMIT
        if self.center_y > TOP_LIMIT:
            self.center_y = BOTTOM_LIMIT
        if self.center_y < BOTTOM_LIMIT:
            self.center_y = TOP_LIMIT

class Enemy(arcade.Sprite):
    #uses sprite from arcade library resources

    def __init__(self, image_file_name, scale):
        super().__init__(image_file_name, scale=scale)
        self.size = 0

    def update(self):
        #updates the position of the enemy sprite
        super().update()
        if self.center_x < LEFT_LIMIT:
            self.center_x = RIGHT_LIMIT
        if self.center_x > RIGHT_LIMIT:
            self.center_x = LEFT_LIMIT
        if self.center_y > TOP_LIMIT:
            self.center_y = BOTTOM_LIMIT
        if self.center_y < BOTTOM_LIMIT:
            self.center_y = TOP_LIMIT