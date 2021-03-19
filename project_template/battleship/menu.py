import constants
import arcade
from instructions import Instructions

class Menu(arcade.View):
    """ This handles showing the main menu when the game starts up.

    Code gotten from the "view instruction and game over" example on 
    the arcade website.
    Editor: Logan Huston
    """

    def on_show(self):
        """
        """
        arcade.set_background_color(arcade.color.AIR_SUPERIORITY_BLUE)

    def on_draw(self):
        """
        """
        arcade.start_render() #This start render only needs to be called once. If this is called here, remove from the board class and vice versa.
        arcade.draw_text("Battleship Shooter", constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2, arcade.color.WHITE, font_size=50, anchor_x="center")
        arcade.draw_text("Click to advance", constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2-75, arcade.color.WHITE, font_size=30, anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        """
        """
        instructions = Instructions()
        self.window.show_view(instructions)
