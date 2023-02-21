from Character import *
from Monster import *


class Game:
    characters = []
    monsters = []
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
            for character in self.characters:
                hitPoints = character.character["hit_point_maximum"]
                battleSaveData[character.characterFileName] = {"hit_point_maximum": hitPoints, "hit_points": hitPoints, "initiative": character.rollInitiative()}
            for monster in self.monsters:
                hitPoints = monster["data"].rollHitPoints()
                battleSaveData[monster["id"]] = {"hit_point_maximum": hitPoints, "hit_points": hitPoints, "initiative": monster["data"].rollInitiative()}

            Control.setData(self.battleSaveFilePath, battleSaveData)

    def getCharacters(self):
        partyFileData = Control.getData(self.gameFolder + "party.json")
        party = partyFileData["party"]
        for character in party:
            tempCharacter = Character(str(character))
            self.characters.append(tempCharacter)
    
    def getMonsters(self):
        battleFileData = Control.getData(self.battleFilePath)
        for monster in battleFileData["monsters"]:
            for monsterNum in range(monster["count"]):
                self.monsters.append({"id": monster["monster"] + str(monsterNum), "data": Monster(monster["monster"])})

    def __init__(self, gameName, battleName):
        self.gameName = str(gameName)
        self.gameFolder = "games/" + self.gameName + "/"
        self.battleName = str(battleName)
        self.battleFilePath = self.gameFolder + "battles/" + self.battleName + ".json"
        self.battleSaveFilePath = self.gameFolder + "battle_saves/" + self.battleName + ".json"
        self.getCharacters()
        self.getMonsters()