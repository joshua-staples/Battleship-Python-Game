import arcade
import constants
from board import Board
from menu import Menu

def main():
    """ Main method 
    
    Args:
        window = will set the window
        start_view = instance of Menu
    """
    
    window = arcade.Window(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.SCREEN_TITLE)
    start_view = Menu()
    window.show_view(start_view)
    arcade.run()

if __name__ == "__main__":
    main()  

