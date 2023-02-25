from Character import *
from Monster import *

class Game:
    characters = {}
    monsters = {}
    turnOrder = []
    gameName = ""
    gameFolder = ""
    battleName = ""
    battleFilePath = ""
    battleSaveFilePath = ""
    
    def getBattleSave(self):
        try:
            return Control.getData(self.battleSaveFilePath)
        except FileNotFoundError:
            battleSaveData = {}
            for characterName in self.characters:
                character = self.characters[characterName]
                hitPoints = character.character["hit_point_maximum"]
                battleSaveData[character.characterFileName] = {"hit_points": hitPoints, "initiative": character.rollInitiative()}
            for monsterName in self.monsters:
                monster = self.monsters[monsterName]
                hitPoints = monster.rollHitPoints()
                battleSaveData[monsterName] = {"hit_point_maximum": hitPoints, "hit_points": hitPoints, "initiative": monster.rollInitiative()}

            Control.setData(self.battleSaveFilePath, battleSaveData)
            return battleSaveData
    
    def setTurnOrder(self):
        battleSave = self.getBattleSave()

        for creature in battleSave.keys():
                self.turnOrder.append(creature)
        
        for i in range(0, len(self.turnOrder)):
            for j in range(i + 1, len(self.turnOrder)):
                if(battleSave[self.turnOrder[i]]["initiative"] < battleSave[self.turnOrder[j]]["initiative"]):
                    temp = self.turnOrder[i]
                    self.turnOrder[i] = self.turnOrder[j]
                    self.turnOrder[j] = temp
                
    def showInfo(self, creatureID):
        if creatureID in self.characters.keys():
            self.characters[creatureID].showInfo()
        else:
            self.monsters[creatureID].showInfo()

    def getCharacters(self):
        partyFileData = Control.getData(self.gameFolder + "party.json")
        party = partyFileData["party"]
        for character in party:
            tempCharacter = Character(str(character))
            self.characters[character] = (tempCharacter)
            
        print(self.characters)

    
    def getMonsters(self):
        battleFileData = Control.getData(self.battleFilePath)
        for monster in battleFileData["monsters"]:
            for monsterNum in range(monster["count"]):
                self.monsters[monster["monster"] + str(monsterNum)] = Monster(monster["monster"])

    def __init__(self, gameName, battleName):
        self.gameName = str(gameName)
        self.gameFolder = "games/" + self.gameName + "/"
        self.battleName = str(battleName)
        self.battleFilePath = self.gameFolder + "battles/" + self.battleName + ".json"
        self.battleSaveFilePath = self.gameFolder + "battle_saves/" + self.battleName + ".json"
        self.getCharacters()
        self.getMonsters()