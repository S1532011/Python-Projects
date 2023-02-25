import math
from tkinter import *

from Control import *
from Window import *

class Character:
    character = {}
    characterFileName = ""

    def getItemText(self, key, characterNode):
        print("<!----- Key:", key, "----->")
        
        if(key.find("stat_modifier") != -1):
            return self.getStatModifier(key[key.rfind(".") + 1:])
        if(key.find("skill_modifier") != -1):
            return self.getSkillModifier(key[key.rfind(".") + 1:])

        if(key.find(".") != -1):
            return self.getItemText(key[key.find(".") + 1:], characterNode[key[:key.find(".")]])
        else:
            return characterNode[key]

    def showInfo(self):
        imageSource = PhotoImage(file="source/img/character_sheet.png")
        image = Label(Window.window, image=imageSource)
        image.place(x=200, y=0)

        characterSheet = Control.getData("source/sheets/character_sheet.json")

        for item in characterSheet:
            itemText = ""
            for key in item["keys"]:
                itemText += str(self.getItemText(key, self.character)) + " "

            sheetItem = Label(Window.window, text=itemText, anchor="w", bg="#ab23ff")
            sheetItem.place(x=item["x"], y=item["y"])

        Window.window.mainloop()

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
        proficiencyBonusFileName = "source/proficiency_bonus.json"
        proficiencyBonusFileData = Control.getData(proficiencyBonusFileName)
        return proficiencyBonusFileData["proficiency_bonus"][self.character["level"]]
    
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