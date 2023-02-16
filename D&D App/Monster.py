import math

from Control import *

class Monster:
    monster = {}
    maxHealth = 0
    health = 0
    initiative = 0

    def getSpeed(self):
        return self.monster["speed"]
    
    def getHealth(self):
        health = Control.roll(self.monster["hit_points"])
        return health
    
    def getStatModifier(self, statModifierName):
        statModifier = math.floor((self.monster["stats"][statModifierName] - 10) / 2)
        return statModifier

    def getData(self, monsterName):
        monsterFileName = "source/monsters/" + monsterName + ".json"
        monsterData = Control.getData(monsterFileName)
        return monsterData
    
    def __init__(self, monsterName):
        self.monster = self.getData(monsterName)