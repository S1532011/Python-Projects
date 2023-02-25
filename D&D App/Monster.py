import math

from Control import *
from Window import *

class Monster:
    monster = {}
    monsterFileName = ""

    def showInfo(self):
        print(self.monsterFileName)

    def getHitPoints(self, battleFilePath):
        battleFileData = Control.getData(battleFilePath)
        return battleFileData["monsterFileName"]["hit_points"]
    
    def setHitPoints(self, battleFilePath, hitPoints):
        battleFileData = Control.getData(battleFilePath)
        battleFileData["hit_points"] = hitPoints
        Control.setData(battleFilePath, battleFileData)
    
    def getInitiative(self, battleFilePath):
        battleFileData = Control.getData(battleFilePath)
        return battleFileData["monsterFileName"]["initiative"]

    def setInitiative(self, battleFilePath, initiative):
        battleFileData = Control.getData(battleFilePath)
        battleFileData["initiative"] = initiative
        Control.setData(battleFilePath, battleFileData)  

    def rollInitiative(self):
        return Control.roll("1d20+" + str(self.getStatModifier("dexterity")))      

    def getSpeed(self):
        return self.monster["speed"]
    
    def getHitPoints(self, battleFilePath, id):
        battleFileData = Control.getData(battleFilePath)
        return battleFileData[id]["hit_points"]
    
    def rollHitPoints(self):
        hitPoints = Control.roll(self.monster["hit_points"])
        return hitPoints
    
    def getStatModifier(self, statModifierName):
        statModifier = math.floor((self.monster["stats"][statModifierName] - 10) / 2)
        return statModifier

    def getData(self, monsterName):
        monsterFileName = "source/monsters/" + monsterName + ".json"
        monsterData = Control.getData(monsterFileName)
        return monsterData
    
    def __init__(self, monsterName):
        self.monster = self.getData(monsterName)
        self.monsterFileName = monsterName