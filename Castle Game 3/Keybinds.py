import json

from Player import *

def getControls():
    file = open("keybinds.json", "r")
    return json.loads(file.read())

def getKey(keyName):
    controls = getControls()
    return controls[keyName]

def setControls(controls):
    file = open("keybinds.json", "w")
    file.write(json.dumps(controls))
    file.close()

def setKey(keyName, key):
    controls = getControls()
    controls[keyName] = key
    setControls(controls)

def toggleMenu():
    if(getCurrentMap() == "startMenu.json" or getCurrentMap() == "settings.json" or getCurrentMap() == "deleteSave.json" or getCurrentMap() == "controls.json"):
        setUseState(True, "key.Menu")
    else:
        setUseState(False, "key.Menu")

    if(getUseState("key.Menu")):
        setPlayerPos(getSavedX(),getSavedY())
        setCurrentMap(getSavedMap())
    else:
        setSavedPos(getPlayerX(),getPlayerY())
        setPlayerPos(1,1)
        setSavedMap(getCurrentMap())
        setCurrentMap("startMenu.json")