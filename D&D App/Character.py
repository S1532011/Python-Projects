import math

from Control import *

class Character:
    character = {}
    characterFileName = ""

    def getHitPoints(self, battleFilePath):
        battleFileData = Control.getData(battleFilePath)
        return battleFileData["characterFileName"]["hit_points"]
    
    def setHitPoints(self, battleFilePath, hitPoints):
        battleFileData = Control.getData(battleFilePath)
        battleFileData["hit_points"] = hitPoints
        Control.setData(battleFilePath, battleFileData)
    
    def getInitiative(self, battleFilePath):
        battleFileData = Control.getData(battleFilePath)
        return battleFileData["characterFileName"]["initiative"]
    
    def setInitiative(self, battleFilePath, initiative):
        battleFileData = Control.getData(battleFilePath)
        battleFileData["initiative"] = initiative
        Control.setData(battleFilePath, battleFileData)
    
    def rollInitiative(self):
        return Control.roll("1d20+" + str(self.getStatModifier("dexterity")))

    def getRaceData(self):
        raceFileName = "source/races/" + self.character["race"] + ".json"
        return Control.getData(raceFileName)
    
    def getRaceLink(self):
        racesFileData = Control.getData("source/race.json")
        raceName = racesFileData["link"]
        return raceName
        
    def getRaceName(self):
        racesFileData = Control.getData("source/race.json")
        raceName = racesFileData["name"]
        return raceName
    
    def getRaceBook(self):
        racesFileData = Control.getData("source/race.json")
        raceName = racesFileData["book"]
        return raceName

    def getSpeed(self):
        raceFileData = self.getRaceData()
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
        self.characterFileName = characterName