# Battleship AI
PLay as a battleship against incoming hoards of pirate boats.
Kill a pirate and they muliply like the head of a hydra.
Crash into a pirate ship and the game is over. 
How many pirates can you slay, and how long can you survive against the onslaught. 

## Getting Started
---
Download all files and run main. 

## Project Structure
---
The project files and folders are organized as follows:
```
root                    (project root folder)
+-- docs                (project documentation)
+-- rename              [src code files - rename for project]
  +-- assets            (program asset files)
  +-- data              (program data files)
  +-- __init__.py       (python package file)
  +-- __main__.py       (entry point for program)
  +-- board.py          (place for all characters and updates to happen)
  +-- enemy.py          (handles all of the updating for the enemy ships)
  +-- ship.py           (handles all of the updating for the players ship)
  +-- menu.py           (opens a view for the instructions to be displayed)
  +-- game_over_screen.py (opens a view for the game over screen to be displayed when a player dies)
  +-- score.py          (holds all of the scoring information for the player)
  +-- constants.py      (holds all constant values that will not change during gameplay)
+-- LICENSE             (license file)
+-- README.md           (general info)
```

## Required Technologies
---
Python 3.6 or newer
Arcade library
random library

## Authors
---
Joshua Staples - sta16016@byui.edu
Logan Huston - hus18004@byui.edu
Spencer Wigren - wig20002@byui.edu
David Del Sol- del17005@byui.edu
