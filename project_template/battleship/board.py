from ship import Ship
import arcade
import constants
from player import Player
from enemy import Enemy_icon
from pathlib import Path
from score import Score
import math
import random

#for collisions
from typing import cast

class Board(arcade.Window):
    """Handles the output of the board. Along with the key inputs of the ship
    
    Code Based on:
        # https://arcade.academy/examples/sprite_collect_coins_background.html?highlight=background%20images
        # enemy behavior and functionality was based on https://github.com/daviddelsol1998/Slime_Space_invaders 
        which is in essence an over customized version of the above tutorials with other code from additional sources
        please see detailed informmation in the description within the enemy class.

    Stereotype:
        Controller/ Coordinator

    Authors:
        Spencer Wigren
        Logan Huston
        Josh Staples
        David Del Sol

    """



    #SPRITE_SCALING
    SPRITE_SCALING = 0.5

    SCALE = 0.5

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
        self.enemy_ship_list = arcade.SpriteList()
        self.bullet_list = None
        # self.wave_background = None

        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)
        
        self.output_Score = Score()

        #Sounds
        #you can use this one for the bullet 
        #self.laser_sound = arcade.load_sound(":resources:sounds/hit5.wav")

        #this ones are triggered when coallision happens
        self.hit_sound1 = arcade.load_sound(":resources:sounds/coin1.wav")
        self.hit_sound2 = arcade.load_sound(":resources:sounds/coin2.wav")
        self.hit_sound3 = arcade.load_sound(":resources:sounds/coin3.wav")
        self.hit_sound4 = arcade.load_sound(":resources:sounds/coin4.wav")

                
    
    def setup(self):
        """Set up of the board.

        Args:
            self.ship = instance of ship class
        """
        
        #GLOBAL VARIABLES
        SCREEN_WIDTH = 800
        SCREEN_HEIGHT = 600

        STARTING_ENEMY_SHIP_COUNT = 10
        SCALE = 0.5
        OFFSCREEN_SPACE = 300
        MUSIC_VOLUME = 0.5

        SCREEN_TITLE = "Battle Ships beta team 6"
        LEFT_LIMIT = -OFFSCREEN_SPACE
        RIGHT_LIMIT = SCREEN_WIDTH + OFFSCREEN_SPACE
        BOTTOM_LIMIT = -OFFSCREEN_SPACE
        TOP_LIMIT = SCREEN_HEIGHT + OFFSCREEN_SPACE

        #score
        self.score = 0

        # Sprite Lists
        self.ship_list = arcade.SpriteList() 
        self.explosion_list = arcade.SpriteList() 
        self.enemy_list = arcade.SpriteList() 
        self.bullet_list = arcade.SpriteList() 

        # self.enemy = Enemy(self.assets_dir / "F5S4.png", constants.SPRITE_SCALING)
        # self.enemy.center_x = 100
        # self.enemy.center_y = 100
        # self.enemy_list.append(self.Enemy)
        # :resources:assets/motor-boat_1f6e5-fe0f.png

        self.player_ship = Ship(self.assets_dir / "motor-boat_1f6e5-fe0f.png", constants.SPRITE_SCALING)
        self.player_ship.center_x = constants.SCREEN_WIDTH/2
        self.player_ship.center_y = constants.SCREEN_HEIGHT/2
        self.ship_list.append(self.player_ship)
        # self.wave_background = arcade.load_texture(":resources:assets/water-wave_1f30a.png")

         # used frogs and other weird animals because I thought it would be fun
         # this will later be changed to something else if you guys want
        image_list = (self.assets_dir / "fishGreen.png",
                      self.assets_dir / "frog_move.png",
                      self.assets_dir / "frog.png",
                      self.assets_dir / "slimeGreen.png")
        for i in range(constants.STARTING_ENEMY_COUNT):
            image_no = random.randrange(4)
            enemy_sprite = Enemy_icon(image_list[image_no], SCALE)
            enemy_sprite.guid = "Enemy"

            enemy_sprite.center_y = random.randrange(BOTTOM_LIMIT, TOP_LIMIT)
            enemy_sprite.center_x = random.randrange(LEFT_LIMIT, RIGHT_LIMIT)

            enemy_sprite.change_x = random.random() * 3 - 1
            enemy_sprite.change_y = random.random() * 3 - 1

            enemy_sprite.change_angle = (random.random() - 0.5) * 2
            enemy_sprite.size = 4
            self.enemy_ship_list.append(enemy_sprite)

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
        #self.enemy_list.draw()
        self.enemy_ship_list.draw()
        
        self.output_Score.on_draw()
        # arcade.draw_lrwh_rectangle_textured(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, self.wave_background)

    def on_update(self, delta_time):
        """updates the board

        Args:
            delta_time Archad: [description]
        """
        self.enemy_ship_list.update()
        self.bullet_list.update()
        self.player_ship.update()

        # Loop through each bullet
        for bullet in self.bullet_list:
            enemies = arcade.check_for_collision_with_list(bullet, self.enemy_ship_list)
            # # Check this bullet to see if it hit a coin
            # hit_list = arcade.check_for_collision_with_list(bullet, self.coin_list)

            # # If it did, get rid of the bullet
            # if len(hit_list) > 0:
            #     bullet.remove_from_sprite_lists()

            # # For every coin (enemy) we hit, add to the score and remove the coin
            for enemy in enemies:
                self.split_enemy(cast(Enemy_icon, enemy))  # expected Enemy_icon, got Sprite instead
                enemy.remove_from_sprite_lists()
                bullet.remove_from_sprite_lists()

            # If the bullet flies off-screen, remove it.
            if bullet.bottom > constants.SCREEN_WIDTH or bullet.top < 0 or bullet.right < 0 or bullet.left > constants.SCREEN_WIDTH:
                bullet.remove_from_sprite_lists()

        if arcade.check_for_collision_with_list(self.player_ship, self.enemy_ship_list):
            arcade.close_window()

    def split_enemy(self, enemy: Enemy_icon):
        """ Split an enemy into smaller versions. """
        x = enemy.center_x
        y = enemy.center_y
        self.score += 1
        SCALE = 0.5

        if enemy.size == 4:
            for i in range(3):
                image_no = random.randrange(2)
                image_list = [self.assets_dir / "wormGreen.png",
                              self.assets_dir / "wormGreen_dead.png"]

                enemy_sprite = Enemy_icon(image_list[image_no],
                                              SCALE * 1.5)

                enemy_sprite.center_y = y
                enemy_sprite.center_x = x

                enemy_sprite.change_x = random.random() * 2.5 - 1.25
                enemy_sprite.change_y = random.random() * 2.5 - 1.25

                enemy_sprite.change_angle = (random.random() - 0.5) * 2
                enemy_sprite.size = 3

                self.enemy_ship_list.append(enemy_sprite)
                self.hit_sound1.play()

            # Will update the score
            self.output_Score.update_basic()

        elif enemy.size == 3:
            for i in range(3):
                image_no = random.randrange(2)
                image_list = [self.assets_dir / "wormGreen.png",
                              self.assets_dir / "wormGreen_dead.png"]

                enemy_sprite = Enemy_icon(image_list[image_no],
                                              SCALE * 1.5)

                enemy_sprite.center_y = y
                enemy_sprite.center_x = x

                enemy_sprite.change_x = random.random() * 3 - 1.5
                enemy_sprite.change_y = random.random() * 3 - 1.5

                enemy_sprite.change_angle = (random.random() - 0.5) * 2
                enemy_sprite.size = 2

                self.enemy_ship_list.append(enemy_sprite)
                self.hit_sound2.play()

            # Will update the score
            self.output_Score.update_basic()

        elif enemy.size == 2:
            for i in range(3):
                image_no = random.randrange(2)
                image_list = [self.assets_dir / "wormGreen.png",
                              self.assets_dir / "wormGreen_dead.png"]

                enemy_sprite = Enemy_icon(image_list[image_no],
                                              SCALE * 1.5)

                enemy_sprite.center_y = y
                enemy_sprite.center_x = x

                enemy_sprite.change_x = random.random() * 3.5 - 1.75
                enemy_sprite.change_y = random.random() * 3.5 - 1.75

                enemy_sprite.change_angle = (random.random() - 0.5) * 2
                enemy_sprite.size = 1

                self.enemy_ship_list.append(enemy_sprite)
                self.hit_sound3.play()

            # Will update the score
            self.output_Score.update_basic()

        elif enemy.size == 1:
            self.hit_sound4.play()

            # Will update the score
            self.output_Score.update_final()
            
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
        bullet = arcade.Sprite(self.assets_dir / "laserRed01.png", constants.SPRITE_SCALING_LASER)

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

    
       
       
    

