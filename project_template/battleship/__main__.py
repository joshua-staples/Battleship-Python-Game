import arcade
import screen
import constants

def main():
    arcade.open_window(constants.LENGTH, constants.WIDTH, constants.SCREENNAME)
    arcade.set_background_color(arcade.csscolor.AQUA)
    
    arcade.start_render()

    arcade.finish_render()
    
    arcade.run()

main()