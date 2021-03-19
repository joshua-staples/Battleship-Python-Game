import arcade
import constants 
from enemy import Enemy
from player import Player

class Score(arcade.Sprite):
    """handles the score output. Along with increaseing the score.

    Code Based on: 
        https://arcade.academy/examples/platform_tutorial/step_07.html?highlight=score

    Sterotype:
        Coordinator

    Authors:
        Spencer Wigren
    """

    def __init__(self):
        """The sut up of the score
        
        Args:
            score = init the score
            enemy = class of Enemy()
            player = class of Player()

        """
        # init the score
        self.score = 0
        # self.enemy = Enemy()
        # self.player = Player()
    

    def update_basic(self):
        """Will up date the score

        Args:
            None

        """
        self.score += 10
        return self.score


    def update_final(self):
        """Will up date the score

        Args:
            None
        
        """
        self.score += 50
        return self.score
        
        

    def on_draw(self):
        """Will draw the score
            
        Args:
            score_output = text for the score

        """
        self.score_output = f"Score: {self.score}"
        arcade.draw_text(self.score_output, 0, constants.SCREEN_HEIGHT - 20,
                         arcade.csscolor.WHITE, 18)