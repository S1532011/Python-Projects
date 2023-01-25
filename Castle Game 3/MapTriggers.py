from Map import getMapData
from Player import *
from Functions import *
from Keybinds import *

class MapTriggers:
    def testTriggers(type):
        map = getMapData()
        returnCode = ""

        triggers = map["triggers"]

        for trigger in triggers:
            if(trigger["X"] == Player.getPlayerX() and trigger["Y"] == Player.getPlayerY()):
                if(len(trigger["conditions"]) == 0):
                    returnCode = MapTriggers.runTrigger(trigger,type)
                else:
                    control = True
                    for condition in trigger["conditions"]:
                        if(condition["conditionType"] == "key.Use1" and Player.getUseState("key.Use1") == False):
                            control = False
                        if(condition["conditionType"] == "key.Use2" and Player.getUseState("key.Use2") == False):
                            control = False
                        if(condition["conditionType"] == "key.Use3" and Player.getUseState("key.Use3") == False):
                            control = False
                        if(condition["conditionType"] == "key.Use4" and Player.getUseState("key.Use4") == False):
                            control = False
                        if(condition["conditionType"] == "item" and Player.testForItem(condition) == False):
                            control = False

                    if(control):
                        returnCode = MapTriggers.runTrigger(trigger,type)

        if(type == "text"):
            Player.setUseState(False, "key.Use1")
            Player.setUseState(False, "key.Use2")
            Player.setUseState(False, "key.Use3")
            Player.setUseState(False, "key.Use4")
        
        return returnCode

    def runTrigger(trigger, type):
        if(trigger["type"] == "text" and type == "text"):
            text = str(trigger["text"])
            if("{" in text):
                keyName = text[text.find("{")+1:text.find("}")]
                text = text.replace(str(keyName), str(Keybinds.getKey(keyName)))
            print(text)
        elif(trigger["type"] == "teleport" and type == "teleport"):
            Player.setPlayerPos(trigger["X2"], trigger["Y2"])
            if(trigger["map"] != ""):
                Player.setCurrentMap(trigger["map"])
        elif(trigger["type"] == "function" and type == "teleport"):
            return runFunction(trigger)
