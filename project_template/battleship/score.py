import arcade
import constants 

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
        """The set up of the score
        
        Args:
            score = init the score
        """
        # init the score
        self.score = 0
        

    def update_basic(self):
        """Will up date the score

        Args:
            score = main score counter
        """
        self.score += 10
        return self.score


    def update_final(self):
        """Will up date the score for final enemy

        Args:
            score = finaly score counter
        """
        self.score += 50
        return self.score
        
    
    def get_score(self):
        """Will show the score

        Args:
            score = score
        """
        return self.score
        
        
    def on_draw(self):
        """Will draw and keep track the score
            
        Args:
            score_output = text for the score
        """
        self.score_output = f"Score: {self.score}"
        arcade.draw_text(self.score_output, 0, constants.SCREEN_HEIGHT - 56,
                         arcade.color.GOLDENROD, 50)