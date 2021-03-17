import constants
import arcade

class Instructions(arcade.View):
    """ This handles showing the instructions after the main menu when the 
    game starts up.

    Code gotten from the "view instruction and game over" example on 
    the arcade website.
    Editor: Logan Huston
    """

    def on_show(self):
        """
        """
        arcade.set_background_color(arcade.color.AIR_SUPERIORITY_BLUE)

    def on_draw(self):
        """ Draw the Instructions screen.
        """
        arcade.draw_text("Instructions", 2*constants.SCREEN_WIDTH/3, constants.SCREEN_HEIGHT/2, arcade.color.WHITE, font_size=50, anchor_x="center")
        arcade.draw_text("Move with WASD", constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2+25, arcade.color.WHITE, font_size=30, anchor_x="center")
        arcade.draw_text("Aim by moving the mouse", constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2, arcade.color.WHITE, font_size=30, anchor_x="center")
        arcade.draw_text("Left-click to shoot", constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2-25, arcade.color.WHITE, font_size=30, anchor_x="center")
        arcade.draw_text("Click to advance", constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2-75, arcade.color.WHITE, font_size=30, anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        """
        """
        # Probably need to modify __main__ so that I can let this start the game loop.
        pass
