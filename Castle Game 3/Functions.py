import os
import msvcrt

from Player import *
from Keybinds import *

def startGame():
    Player.setPlayerPos(1,1)

    Player.setUseState(False, "key.Use1")
    Player.setUseState(False, "key.Use2")
    Player.setUseState(False, "key.Use3")
    Player.setUseState(False, "key.Use4")
    Player.setUseState(True, "key.Menu")

    Player.setCurrentMap("startMenu.json")

    checkSavedMap()

def checkSavedMap():
    if(Player.getSavedMap() == ""):
        Player.setSavedMap("save/startMap.json")
        Player.setSavedPos(1,2)

def runFunction(trigger):
    if(trigger["function"] == "deleteSave"):
        deleteSave()
    if(trigger["function"] == "levelEditor"):
        levelEditor()
    if(trigger["function"] == "quitGame"):
        return "quit"
    if(trigger["function"] == "startGame"):
        Keybinds.toggleMenu()
    if(trigger["function"] == "giveItem"):
        giveItem(trigger)
    if(trigger["function"] == "removeItem"):
        removeItem(trigger)
    if(trigger["function"] == "setKey"):
        print("Press a Key to Change Keybind:")
        Keybinds.setKey(trigger["key"], str(msvcrt.getwch()).upper())
#if(trigger["function"] == ""):

def getItem(itemFile):
    file = open(itemFile, "r")
    item = json.loads(file.read())
    file.close()
    return item

def deleteSave():
    os.system("del /Q save\\*")
    Player.setSavedMap("save/startMap.json")
    Player.setSavedPos(1,2)

def levelEditor():
    os.system("copy maps/template.json save")

def giveItem(trigger):
    item = getItem(trigger["item"])
    Player.giveItem(item)

def removeItem(trigger):
    item = getItem(trigger["item"])
    Player.removeItem(item)