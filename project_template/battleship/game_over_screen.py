import constants
import arcade

class Game_Over_Screen(arcade.View):
    """ This handles showing the Game Over screen when the player loses or ends the game.

    Code gotten from the "view instruction and game over" example on 
    the arcade website.
    Editor: Logan Huston
    """

    def on_show(self):
        """
        """
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        """ Draw the Game Over screen.
        """
        arcade.draw_text("Game Over", constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2, arcade.color.WHITE, font_size=50, anchor_x="center")
        # Need to change this and the next method to the escape key.
        arcade.draw_text("Click to end", constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2-75, arcade.color.WHITE, font_size=30, anchor_x="center")

    def on_key_press(self, key, _modifiers):
        """ Use a key press to end the game.
        """
        if arcade.key.ESCAPE:
            arcade.close_window()
