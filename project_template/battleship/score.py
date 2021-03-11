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
    

    def update(self):
        """Will up date the score

        Args:
            None

        """
        # Will need to figure out how to fix this code with the team.
        # I don't know how we are going to consired when the socre increases
        # I think that it will be when the players bullets locations hits the enemy location

        # Will need to find a way to know where the player hits the enemy
        # if self.player == self.enemy:
        #     # Do we need to change the score increase?
        #     score += 10
        

    def on_draw(self):
        """Will draw the score
            
        Args:
            score_output = text for the score

        """
        score_output = f"Score: {self.score}"
        arcade.draw_text(score_output, 0, constants.HEIGHT - 20,
                         arcade.csscolor.WHITE, 18)