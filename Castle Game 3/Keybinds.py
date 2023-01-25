import json

from Player import *

class Keybinds:
    def getControls():
        file = open("keybinds.json", "r")
        return json.loads(file.read())

    def getKey(keyName):
        controls = Keybinds.getControls()
        return controls[keyName]

    def setControls(controls):
        file = open("keybinds.json", "w")
        file.write(json.dumps(controls))
        file.close()

    def setKey(keyName, key):
        controls = Keybinds.getControls()
        controls[keyName] = key
        Keybinds.setControls(controls)

    def toggleMenu():
        if(Player.getCurrentMap() == "startMenu.json" or Player.getCurrentMap() == "settings.json" or Player.getCurrentMap() == "deleteSave.json" or Player.getCurrentMap() == "controls.json"):
            Player.setUseState(True, "key.Menu")
        else:
            Player.setUseState(False, "key.Menu")

        if(Player.getUseState("key.Menu")):
            Player.setPlayerPos(Player.getSavedX(),Player.getSavedY())
            Player.setCurrentMap(Player.getSavedMap())
        else:
            Player.setSavedPos(Player.getPlayerX(),Player.getPlayerY())
            Player.setPlayerPos(1,1)
            Player.setSavedMap(Player.getCurrentMap())
            Player.setCurrentMap("startMenu.json")