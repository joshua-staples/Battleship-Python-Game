from ship import Ship
import arcade
import constants
from player import Player
from enemy import Enemy
from pathlib import Path
from score import Score
import math

class Board(arcade.Window):
    """Handles the output of the board. Along with the key inputs of the ship
    
    Code Based on:
        # https://arcade.academy/examples/sprite_collect_coins_background.html?highlight=background%20images

    Stereotype:
        Controller/ Coordinator

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
        super().__init__(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.SCREEN_TITLE)

        # Path declaration for images to be loaded from.
        self.cur_dir = Path(__file__).parent
        self.assets_dir = self.cur_dir/"assets"

        # varables that will hold future spriteLists
        self.ship_list = None
        self.explosion_list = None
        self.enemy_list = None
        self.bullet_list = None
        # self.wave_background = None

        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)
        
        self.output_Score = Score()
                
    
    def setup(self):
        """Set up of the board.

        Args:
            self.ship = instance of ship class
        """
        # Sprite Lists
        self.ship_list = arcade.SpriteList() 
        self.explosion_list = arcade.SpriteList() 
        self.enemy_list = arcade.SpriteList() 
        self.bullet_list = arcade.SpriteList() 

        # self.enemy = Enemy(":resources:images/alien/alienBlue_front.png", SPRITE_SCALING )
        # self.enemy.center_x = 100
        # self.enemy.center_y = 100
        # self.enemy_list.append(self.Enemy)
        # :resources:assets/motor-boat_1f6e5-fe0f.png

        self.player_ship = Ship(self.assets_dir / "motor-boat_1f6e5-fe0f.png", constants.SPRITE_SCALING)
        self.player_ship.center_x = constants.SCREEN_WIDTH/2
        self.player_ship.center_y = constants.SCREEN_HEIGHT/2
        self.ship_list.append(self.player_ship)
        # self.wave_background = arcade.load_texture(":resources:assets/water-wave_1f30a.png")

    def on_draw(self):
        """Draws the board

        Args:
            None.
        """
        arcade.start_render()

        # Draw all the Sprites 
        self.ship_list.draw()
        self.explosion_list.draw() 
        self.bullet_list.draw()
        
        self.output_Score.on_draw()
        # arcade.draw_lrwh_rectangle_textured(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, self.wave_background)

    def on_update(self, delta_time):
        """updates the board

        Args:
            delta_time Archad: [description]
        """
        self.bullet_list.update()
        self.player_ship.update()

        # Loop through each bullet
        for bullet in self.bullet_list:

            # # Check this bullet to see if it hit a coin
            # hit_list = arcade.check_for_collision_with_list(bullet, self.coin_list)

            # # If it did, get rid of the bullet
            # if len(hit_list) > 0:
            #     bullet.remove_from_sprite_lists()

            # # For every coin we hit, add to the score and remove the coin
            # for coin in hit_list:
            #     coin.remove_from_sprite_lists()
            #     self.score += 1

            # If the bullet flies off-screen, remove it.
            if bullet.bottom > constants.SCREEN_WIDTH or bullet.top < 0 or bullet.right < 0 or bullet.left > constants.SCREEN_WIDTH:
                bullet.remove_from_sprite_lists()

    def on_key_press(self, key, modifiers):
        """Handles the key press and movement
        called whenever a key is pressed. 

        Args:
            key = What the key is
        """

        # If the player presses a key, update the speed
        if key == arcade.key.W:
            self.player_ship.change_y = constants.MOVEMENT_SPEED
        elif key == arcade.key.S:
            self.player_ship.change_y = -constants.MOVEMENT_SPEED
        elif key == arcade.key.A:
            self.player_ship.change_x = -constants.MOVEMENT_SPEED
        elif key == arcade.key.D:
            self.player_ship.change_x = constants.MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key.
        
        Args:
            key = What the key is
        """

        # If a player releases a key, zero out the speed.
        # This doesn't work well if multiple keys are pressed.
        # Use 'better move by keyboard' example if you need to
        # handle this.
        if key == arcade.key.W or key == arcade.key.S:
            self.player_ship.change_y = 0
        elif key == arcade.key.A or key == arcade.key.D:
            self.player_ship.change_x = 0       

    def on_mouse_press(self, x, y, button, modifiers):
        """ Called whenever the mouse button is clicked. 
        
        Taken from: https://arcade.academy/examples/sprite_bullets_aimed.html#sprite-bullets-aimed
        with slight modification of Sprite names.
        """

        # Create a bullet
        bullet = arcade.Sprite(":resources:images/space_shooter/laserBlue01.png", constants.SPRITE_SCALING_LASER)

        # Position the bullet at the player's current location
        start_x = self.player_ship.center_x
        start_y = self.player_ship.center_y
        bullet.center_x = start_x
        bullet.center_y = start_y

        # Get from the mouse the destination location for the bullet
        # IMPORTANT! If you have a scrolling screen, you will also need
        # to add in self.view_bottom and self.view_left.
        dest_x = x
        dest_y = y

        # Do math to calculate how to get the bullet to the destination.
        # Calculation the angle in radians between the start points
        # and end points. This is the angle the bullet will travel.
        x_diff = dest_x - start_x
        y_diff = dest_y - start_y
        angle = math.atan2(y_diff, x_diff)

        # Angle the bullet sprite so it doesn't look like it is flying
        # sideways.
        bullet.angle = math.degrees(angle)
        print(f"Bullet angle: {bullet.angle:.2f}")

        # Taking into account the angle, calculate our change_x
        # and change_y. Velocity is how fast the bullet travels.
        bullet.change_x = math.cos(angle) * constants.BULLET_SPEED
        bullet.change_y = math.sin(angle) * constants.BULLET_SPEED

        # Add the bullet to the appropriate lists
        self.bullet_list.append(bullet)

    
       
       
    

