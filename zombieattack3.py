# file used to run the game

#import statements for all the modules

#import the other files

import gamesetup #gets the map put together
import za3gui #displays the graphics and splashpage
import za3brain #uses these functions to get things done, aka algorithms & etc
#import webspread #controls web interface

#loads gui

gamesetup.go();
#display choice of maps for player
choice = raw_input('choose a map');
#if maps(choice) does not exist, berate the player and have them choose again
za3brain.openMap(choice);
za3brain.loadInfo();
za3gui.loadMap();
za3gui.go();
