import os
import msvcrt

from Player import *
from Keybinds import *

def startGame():
    setPlayerPos(1,1)

    setUseState(False, "key.Use1")
    setUseState(False, "key.Use2")
    setUseState(False, "key.Use3")
    setUseState(False, "key.Use4")
    setUseState(True, "key.Menu")

    setCurrentMap("startMenu.json")

    checkSavedMap()

def checkSavedMap():
    if(getSavedMap() == ""):
        setSavedMap("save/startMap.json")
        setSavedPos(1,2)

def runFunction(trigger):
    if(trigger["function"] == "deleteSave"):
        os.system("del /Q save\\*")
        setSavedMap("save/startMap.json")
        setSavedPos(1,2)
    if(trigger["function"] == "levelEditor"):
        os.system("copy maps/template.json save")
    if(trigger["function"] == "quitGame"):
        return "quit"
    if(trigger["function"] == "startGame"):
        toggleMenu()
    if(trigger["function"] == "giveItem"):
        item = getItem(trigger["item"])
        addItem(item)
    if(trigger["function"] == "removeItem"):
        item = getItem(trigger["item"])
        removeItem(item)
    if(trigger["function"] == "setKey"):
        print("Press a Key to Change Keybind:")
        setKey(trigger["key"], str(msvcrt.getwch()).upper())
#if(trigger["function"] == ""):

def getItem(itemFile):
    file = open(itemFile, "r")
    item = json.loads(file.read())
    file.close()
    return item