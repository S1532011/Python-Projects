import msvcrt

from Map import *
from Player import *
from Keybinds import *


def getInput():
    keyInput = str(msvcrt.getwch()).upper()
    mapFile = Map.getMapData()
    map = mapFile["map"]

    if (keyInput == Keybinds.getKey("key.Up")):
        if(Map.wallExistsPlayer(Player.getPlayerY() - 1, Player.getPlayerX(), map) == False or Player.getEditorMode()):
            Player.setPlayerY(Player.getPlayerY() - 1)
    elif (keyInput == Keybinds.getKey("key.Down")):
        if(Map.wallExistsPlayer(Player.getPlayerY() + 1, Player.getPlayerX(), map) == False or Player.getEditorMode()):
            Player.setPlayerY(Player.getPlayerY() + 1)
    elif (keyInput == Keybinds.getKey("key.Left")):
        if(Map.wallExistsPlayer(Player.getPlayerY(), Player.getPlayerX() - 1, map) == False or Player.getEditorMode()):
            Player.setPlayerX(Player.getPlayerX() - 1)
    elif (keyInput == Keybinds.getKey("key.Right")):
        if(Map.wallExistsPlayer(Player.getPlayerY(), Player.getPlayerX() + 1, map) == False or Player.getEditorMode()):
            Player.setPlayerX(Player.getPlayerX() + 1)
    elif (keyInput == Keybinds.getKey("key.Use1")):
        Player.setUseState(True, "key.Use1")
    elif (keyInput == Keybinds.getKey("key.Use2")):
        Player.setUseState(True, "key.Use2")
    elif (keyInput == Keybinds.getKey("key.Use3")):
        Player.setUseState(True, "key.Use3")
    elif (keyInput == Keybinds.getKey("key.Use4")):
        Player.setUseState(True, "key.Use4")
    elif (keyInput == Keybinds.getKey("key.Menu")):
        Keybinds.toggleMenu()