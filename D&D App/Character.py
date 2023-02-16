import math

from Control import *

class Character:
    character = {}
    maxHealth = 0
    health = 0
    initiative = 0

    def getSpeed(self):
        raceFileName = "source/races/" + self.character["race"] + ".json"
        raceFileData = Control.getData(raceFileName)
        return raceFileData["speed"]
    
    def getProficiencyBonus(self):
        proficiencyBonusFileName = "source/proficiencyBonus.json"
        proficiencyBonusFileData = Control.getData(proficiencyBonusFileName)
        return proficiencyBonusFileData[self.character["level"]]
    
    def getStatModifier(self, statModifierName):
        statModifier = math.floor((self.character["stats"][statModifierName] - 10) / 2)
        return statModifier
    
    # def getSavingThrowModifier(self, savingThrowName):
    #     savingThrowModifier = 
    #     return savingThrowModifier
    
    def getSkillModifier(self, skillModifierName):
        skillModifier = self.getStatModifier(Control.getStatFromSkill(skillModifierName)) + (self.character["skills"][skillModifierName] * self.getProficiencyBonus())
        return skillModifier
    
    # def getPassivePerception():
    #     return passivePerception

    def getData(self, characterName):
        characterFileName = "characters/" + characterName + ".json"
        characterData = Control.getData(characterFileName)
        return characterData
    
    def __init__(self, characterName):
        self.character = self.getData(characterName)