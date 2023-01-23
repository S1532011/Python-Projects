from Map import getMapData
from Player import *
from Functions import *
from Keybinds import *


def testTriggers(type):
    map = getMapData()
    returnCode = ""

    triggers = map["triggers"]

    for trigger in triggers:
        if(trigger["X"] == getPlayerX() and trigger["Y"] == getPlayerY()):
            if(len(trigger["conditions"]) == 0):
                returnCode = runTrigger(trigger,type)
            else:
                control = True
                for condition in trigger["conditions"]:
                    if(condition["conditionType"] == "key.Use1" and getUseState("key.Use1") == False):
                        control = False
                    if(condition["conditionType"] == "key.Use2" and getUseState("key.Use2") == False):
                        control = False
                    if(condition["conditionType"] == "key.Use3" and getUseState("key.Use3") == False):
                        control = False
                    if(condition["conditionType"] == "key.Use4" and getUseState("key.Use4") == False):
                        control = False
                    if(condition["conditionType"] == "item" and testForItem(condition) == False):
                        control = False

                if(control):
                    returnCode = runTrigger(trigger,type)

    if(type == "text"):
        setUseState(False, "key.Use1")
        setUseState(False, "key.Use2")
        setUseState(False, "key.Use3")
        setUseState(False, "key.Use4")
    
    return returnCode

def runTrigger(trigger, type):
    if(trigger["type"] == "text" and type == "text"):
        text = str(trigger["text"])
        if("{" in text):
            keyName = text[text.find("{")+1:text.find("}")]
            text = text.replace(str(keyName), str(getKey(keyName)))
        print(text)
    elif(trigger["type"] == "teleport" and type == "teleport"):
        setPlayerPos(trigger["X2"], trigger["Y2"])
        if(trigger["map"] != ""):
            setCurrentMap(trigger["map"])
    elif(trigger["type"] == "function" and type == "teleport"):
        return runFunction(trigger)
