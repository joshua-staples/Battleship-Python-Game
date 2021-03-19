import constants
import arcade
from board import Board
class Instructions(arcade.View):
    """ This handles showing the instructions after the main menu when the 
    game starts up.

    Code gotten from the "view instruction and game over" example on 
    the arcade website.

    https://arcade.academy/examples/view_instructions_and_game_over.html#view-instructions-and-game-over

    Editor: Logan Huston
    """

    def on_show(self):
        """
        """
        # self.screen.clear(self.background_color)
        arcade.set_background_color(arcade.color.AIR_SUPERIORITY_BLUE)

    # def __init__(self):
    #     # super().__init__(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)
    #     arcade.set_background_color(arcade.color.AIR_SUPERIORITY_BLUE)
    

    def on_draw(self):
        """ Draw the Instructions screen.
        """
        # arcade.draw_text("Instructions", 2*constants.SCREEN_WIDTH/3, constants.SCREEN_HEIGHT/2, arcade.color.WHITE, font_size=50, anchor_x="center")
        arcade.draw_text("Move with WASD", constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2+30, arcade.color.WHITE, font_size=30, anchor_x="center")
        arcade.draw_text("Aim by moving the mouse", constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2, arcade.color.WHITE, font_size=30, anchor_x="center")
        arcade.draw_text("Left-click to shoot", constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2-35, arcade.color.WHITE, font_size=30, anchor_x="center")
        arcade.draw_text("Click to advance", constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2-75, arcade.color.WHITE, font_size=30, anchor_x="center")


    def on_mouse_press(self, _x, _y, _button, _modifiers):
        """
        """
        # Probably need to modify __main__ so that I can let this start the game loop.
        # window = Board()
        # window.setup()
        # self.window.show_view(window)
