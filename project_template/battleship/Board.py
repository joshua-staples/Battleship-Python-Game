# import constants
import arcade

#SPRITE_SCALING = 0.5

# SCREEN_HEIGHT = 600
# SCREEN_WIDTH =  600
# SCREEN_TITLE = "Battleship"
# FPS = 60

class Board(arcade.Sprite):
    

    def __init__(self):

        # super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        self.ship_list = None
        self.wave_background = None
        self.explosion_list = None
        
        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)

    def setup(self):
        self.ship_list = arcade.SpriteList()
        
        self.explosion_list = arcade.SpriteList()
        
        self.wave_background = arcade.load_texture(":resources:assets/water-wave_1f30a.png")
        
        
        # self.wave_list = arcade.load_texture(":resources:assets/water-wave_1f30a.png")
        # Will need to take this out for final project
    # def on_draw(self):

    #     arcade.start_render()
    #     self.ship_list.draw()
    #     # self.wave_list.draw()
    #     self.explosion_list.draw()
    #     arcade.draw_lrwh_rectangle_textured(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, self.wave_background)

# def main():
#     """ Main method """
#     window = Board()
#     window.setup()
#     arcade.run()


# if __name__ == "__main__":
#     main()