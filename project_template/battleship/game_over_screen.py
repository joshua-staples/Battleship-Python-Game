from arcade.key import ESCAPE
import constants
import arcade

class Game_Over_Screen(arcade.View):
    """ This handles showing the Game Over screen when the player loses or ends the game.

    Code gotten from the "view instruction and game over" example on 
    the arcade website.
    Editor: Logan Huston and Joshua Staples
    """
    
    def __init__(self):
        super().__init__()
        arcade.set_viewport(0, constants.SCREEN_WIDTH - 1, 0, constants.SCREEN_HEIGHT - 1)
        self.final_score = 0
        
    def on_show(self):
        """Change the back ground color.

            This def may not work. Check for finaly release.
        """
        arcade.set_background_color(arcade.csscolor.BLACK)

    def on_draw(self):
        """ Draw the Game Over screen.
        """
        arcade.start_render()
        arcade.draw_text(f"High Score: {self.final_score}", constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2 + 100,
                         arcade.color.WHITE, font_size=100, anchor_x="center")
        arcade.draw_text("Game Over", constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2,
                         arcade.color.WHITE, font_size=50, anchor_x="center")
        # Need to change this and the next method to the escape key.
        arcade.draw_text("Press ESC to Exit", constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2-75,
                         arcade.color.WHITE, font_size=30, anchor_x="center")
        # arcade.draw_text("Click Left Mouse to Play Again", constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2-150,
        #                  arcade.color.WHITE, font_size=30, anchor_x="center")

    def on_key_press(self, key, _modifiers):
        """ Use a key press to end the game.
        """
        if key == arcade.key.ESCAPE:
            arcade.close_window()


