#from battleship import constants
import arcade
import random
from PIL import Image

#SPRITE_SCALING = 0.5

SCREEN_HEIGHT = 600
SCREEN_WIDTH =  600
SCREEN_TITLE = "Battleship"
FPS = 60

class Board(arcade.Window):
    

    def __init__(self):

        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        self.ship_list = None
        self.wave_list = None
        self.explosion_list = None
        
        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)

    def setup(self):
        self.ship_list = arcade.SpriteList()
        self.wave_list = arcade.SpriteList()
        self.explosion_list = arcade.SpriteList()
        
        # Will need to change path to images later
        # Will create list for waves horizontal rows
        for x in range(0, SCREEN_WIDTH, 92):
            wave = arcade.Sprite("resources:images/tiles/water-wave_1f30a.png")
            wave.center_x = x
            wave.center_y = 32
            self.wave_list.append(wave)

            wave = arcade.Sprite("resources:images/assets/water-wave_1f30a.png")
            wave.center_x = x
            wave.center_y = SCREEN_HEIGHT - 32
            self.wave_list.append(wave)

        # Will create list for waves vertical columns
        for y in range(128, SCREEN_HEIGHT, 196):
            wave = arcade.Sprite("resources:images/assets/water-wave_1f30a.png")
            wave.center_x = 32
            wave.center_y = y
            self.wave_list.append(wave)

            wave = arcade.Sprite("resources:images/assets/water-wave_1f30a.png")
            wave.center_x = y
            wave.center_y = SCREEN_WIDTH - 32
            self.wave_list.append(wave)

        
        

        # Will need to take this out for final project
    def on_draw(self):
        arcade.start_render()
        self.ship_list.draw()
        self.wave_list.draw()
        self.explosion_list.draw()


def main():
    """ Main method """
    window = Board()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()