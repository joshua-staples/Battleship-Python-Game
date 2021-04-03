"""Will show the menue screen when programs is loaded up.
    Menu is a subclass of view and window.
    on_show will set the back ground and viewport window.
    on_draw will draw the text to the screen
    on_mouse_press will start the game when pressed and load the new window.
"""

import constants
import arcade
from board import Board

class Menu(arcade.View, arcade.Window):
    """ This handles showing the main menu when the game starts up.

    Code gotten from the "view instruction and game over" example on 
    the arcade website.

    https://arcade.academy/examples/view_instructions_and_game_over.html#view-instructions-and-game-over

    Sterotype:
        Coordinator

    Author: Logan Huston
    Editor: Spencer Wigren
    """

    def on_show(self):
        """Will set the back ground screen and size

        Args:
            None
        """

        arcade.set_background_color(arcade.color.DARK_SPRING_GREEN)
        arcade.set_viewport(0, constants.SCREEN_WIDTH - 1, 0, constants.SCREEN_HEIGHT - 1)


    def on_draw(self):
        """Will draw the text on the screen

        Args:
            None
        """

        arcade.start_render()

        # Draw the main text on the screen
        arcade.draw_text("Battleship Shooter", constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2 + 200, arcade.color.WHITE, font_size=50, anchor_x="center")
        arcade.draw_text("Move with WASD", constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2+35, arcade.color.WHITE, font_size=30, anchor_x="center")
        arcade.draw_text("Aim by moving the mouse", constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2, arcade.color.WHITE, font_size=30, anchor_x="center")
        arcade.draw_text("Left-click to shoot", constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2-35, arcade.color.WHITE, font_size=30, anchor_x="center")
        arcade.draw_text("Click to advance", constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2-100, arcade.color.WHITE, font_size=30, anchor_x="center")

        #Authors Names
        arcade.draw_text('Authors:', constants.SCREEN_WIDTH/2-700, constants.SCREEN_HEIGHT/2+300, arcade.color.WHITE, font_size=30, anchor_x="left")
        arcade.draw_text('Josh Staples', constants.SCREEN_WIDTH/2-650, constants.SCREEN_HEIGHT/2+250, arcade.color.WHITE, font_size=20, anchor_x="left")
        arcade.draw_text('Logan Huston', constants.SCREEN_WIDTH/2-650, constants.SCREEN_HEIGHT/2+200, arcade.color.WHITE, font_size=20, anchor_x="left")
        arcade.draw_text('David Del Sol', constants.SCREEN_WIDTH/2-650, constants.SCREEN_HEIGHT/2+150, arcade.color.WHITE, font_size=20, anchor_x="left")
        arcade.draw_text('Spencer Wigren', constants.SCREEN_WIDTH/2-650, constants.SCREEN_HEIGHT/2+100, arcade.color.WHITE, font_size=20, anchor_x="left")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        """Will start the game and clears the menu screen.
        
        Args:
            None
        """

        board_view = Board()
        self.window.show_view(board_view)

