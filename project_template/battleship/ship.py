"""The Ship class is in charge of overrding the update method for the player.
    Ship is a subclass of sprite so a ship will still have access to all of the sprite methods. 
    The update method in the ship class has been changed to move the player to a new x/y location.
"""
import arcade
import constants

class Ship(arcade.Sprite):
    """Handles the creation and movement of a player sprite known as the ship. 
    
    Code Based on:
        # https://arcade.academy/examples/sprite_move_keyboard.html#sprite-move-keyboard

    Stereotype:
        Information Holder

    Authors:
        Josh Staples
    """
    
    def update(self):
        """ 
        Move the player 
        
        Args:
            center_x = x location of player
            center_y = y location of player
            change_x = x next location of player
            change_y = y next location of player
        """
        # Move player.
        # Remove these lines if physics engine is moving player.
        self.center_x += self.change_x
        self.center_y += self.change_y

        # Check for out-of-bounds
        if self.left < 0:
            self.left = 0
        elif self.right > constants.SCREEN_WIDTH - 1:
            self.right = constants.SCREEN_WIDTH - 1

        if self.bottom < 0:
            self.bottom = 0
        elif self.top > constants.SCREEN_HEIGHT - 1:
            self.top = constants.SCREEN_HEIGHT - 1