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
            enemy = class of Enemy()
            player = class of Player()
        """
        # init the score
        self.score = 0
        

    def update_basic(self):
        """Will up date the score

        Args:
            None
        """
        self.score += 10
        return self.score


    def update_final(self):
        """Will up date the score for final enemy

        Args:
            None
        """
        self.score += 50
        return self.score
        
    
    def get_score(self):
        return self.score
        
        
    def on_draw(self):
        """Will draw and keep track the score
            
        Args:
            score_output = text for the score
        """
        self.score_output = f"Score: {self.score}"
        arcade.draw_text(self.score_output, 0, constants.SCREEN_HEIGHT - 56,
                         arcade.color.GOLDENROD, 50)

        # Tried colors
        # Had to use .color, or .csscolor
            # Liked:
                # AQUAMARINE, RED, GOLD, GOLDEN_POPPY
            
            # Maybe:
                # ROMAN_SILVER,

            # Didn't Liked:
                # SEA_GREEN, GRAY_BLUE

            # GOLD_FUSION		 
            # GOLDEN_BROWN		 
            # GOLDEN_POPPY		 
            # GOLDEN_YELLOW		 
            # GOLDENROD