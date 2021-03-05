import arcade
import constants
from board import Board

def main():
    """ Main method """
    window = Board()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()  

