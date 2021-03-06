from ship import Ship
import arcade
import constants
from player import Player
from enemy import Enemy


SPRITE_SCALING = 0.5
SCREEN_HEIGHT = 600
SCREEN_WIDTH =  600
SCREEN_TITLE = "Battleship"
FPS = 60

class Board(arcade.Window):
    """Handles the output of the board. Along with the key inputs of the ship
    
    Code Based on:
        # https://arcade.academy/examples/sprite_collect_coins_background.html?highlight=background%20images

    Stereotype:
        COntroller/ Coordinator

    Authors:
        Spencer Wigren
        Logan Huston
        Josh Staples

    """

    def __init__(self):
        """The set up of the board.

        Args:
            ship_list = list of ships
            explosion_list = list of explosions

        """
        super().__init__(constants.WIDTH, constants.HEIGHT, constants.SCREEN_TITLE)

        self.ship_list = None
        self.explosion_list = None
        # self.wave_background = None

        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)
        
        self.ship_list = arcade.SpriteList()        
        self.explosion_list = arcade.SpriteList()

        self.enemy_list = None

        # Need to find the correct path for the assets        
        # self.wave_background = arcade.load_texture(":resources:assets/water-wave_1f30a.png")
        # self.wave_background = arcade.load_texture(":battleship:assets/water-wave_1f30a.png")
        
    
    def setup(self):
        """Set up of the board.

        Args:
            self.ship = instance of ship class
        """
        self.enemy = Enemy(":resources:images/alien/alienBlue_front.png", SPRITE_SCALING )
        self.enemy.center_x = 100
        self.enemy.center_y = 100
        self.enemy_list.append(self.Enemy)


        self.ship = Ship(":resources:assets/motor-boat_1f6e5-fe0f.png", constants.SPRITE_SCALING)
        self.ship.center_x = 300
        self.ship.center_y = 300
        self.ship_list.append(self.ship)
        # self.wave_background = arcade.load_texture(":resources:assets/water-wave_1f30a.png")


    def on_key_press(self, key, modifiers):
        """Handles the key press and movement
        called whenever a key is pressed. 

        Args:
            key = What the key is
        """

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
        """Called when the user releases a key.
        
        Args:
            key = What the key is
        """

        # If a player releases a key, zero out the speed.
        # This doesn't work well if multiple keys are pressed.
        # Use 'better move by keyboard' example if you need to
        # handle this.
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.ship.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.ship.change_x = 0       

    def on_update(self, delta_time):
        """updates the board

        Args:
            delta_time Archad: [description]
        """
        self.ship.update()
       
    def on_draw(self):
        """Draws the board

        Args:
            None.
        """
        arcade.start_render()
        self.ship_list.draw()
        self.explosion_list.draw()
        # arcade.draw_lrwh_rectangle_textured(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, self.wave_background)

