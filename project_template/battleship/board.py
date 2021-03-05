from ship import Ship
import arcade
import constants

# https://arcade.academy/examples/sprite_collect_coins_background.html?highlight=background%20images

SPRITE_SCALING = 0.5
SCREEN_HEIGHT = 600
SCREEN_WIDTH =  600
SCREEN_TITLE = "Battleship"
FPS = 60

class Board(arcade.Window):
    

    def __init__(self):

        super().__init__(constants.WIDTH, constants.HEIGHT, constants.SCREEN_TITLE)

        self.ship_list = None
        # self.wave_background = None
        self.explosion_list = None
        
        
        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)
        self.ship_list = arcade.SpriteList()
                
        self.explosion_list = arcade.SpriteList()

        # Need to find the correct path for the assets        
        # self.wave_background = arcade.load_texture(":resources:assets/water-wave_1f30a.png")
        # self.wave_background = arcade.load_texture(":battleship:assets/water-wave_1f30a.png")
        
    
    def setup(self):
        self.ship = Ship(":resources:assets/motor-boat_1f6e5-fe0f.png", constants.SPRITE_SCALING)
        self.ship.center_x = 300
        self.ship.center_y = 300
        self.ship_list.append(self.ship)
        # self.wave_background = arcade.load_texture(":resources:assets/water-wave_1f30a.png")


    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        # If the player presses a key, update the speed
        if key == arcade.key.UP:
            self.ship.change_y = constants.MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.ship.change_y = -constants.MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.ship.change_x = -constants.MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.ship.change_x = constants.MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        # If a player releases a key, zero out the speed.
        # This doesn't work well if multiple keys are pressed.
        # Use 'better move by keyboard' example if you need to
        # handle this.
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.ship.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.ship.change_x = 0       

    def on_update(self, delta_time):
            self.ship.update()
       
    def on_draw(self):

        arcade.start_render()
        self.ship_list.draw()
        self.explosion_list.draw()
        # arcade.draw_lrwh_rectangle_textured(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, self.wave_background)

