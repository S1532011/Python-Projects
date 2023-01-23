import msvcrt

from Map import *
from Player import *
from Keybinds import *


def getInput():
    keyInput = str(msvcrt.getwch()).upper()
    mapFile = getMapData()
    map = mapFile["map"]

    if (keyInput == getKey("key.Up")):
        if(wallExistsPlayer(getPlayerY() - 1, getPlayerX(), map) == False or getEditorMode()):
            setPlayerY(getPlayerY() - 1)
    elif (keyInput == getKey("key.Down")):
        if(wallExistsPlayer(getPlayerY() + 1, getPlayerX(), map) == False or getEditorMode()):
            setPlayerY(getPlayerY() + 1)
    elif (keyInput == getKey("key.Left")):
        if(wallExistsPlayer(getPlayerY(), getPlayerX() - 1, map) == False or getEditorMode()):
            setPlayerX(getPlayerX() - 1)
    elif (keyInput == getKey("key.Right")):
        if(wallExistsPlayer(getPlayerY(), getPlayerX() + 1, map) == False or getEditorMode()):
            setPlayerX(getPlayerX() + 1)
    elif (keyInput == getKey("key.Use1")):
        setUseState(True, "key.Use1")
    elif (keyInput == getKey("key.Use2")):
        setUseState(True, "key.Use2")
    elif (keyInput == getKey("key.Use3")):
        setUseState(True, "key.Use3")
    elif (keyInput == getKey("key.Use4")):
        setUseState(True, "key.Use4")
    elif (keyInput == getKey("key.Menu")):
        toggleMenu()