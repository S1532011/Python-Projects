from Character import *
from Monster import *


class Game:
    characters = []
    monsters = []
    gameName = ""
    gameFolder = ""

    def getCharacters(self):
        partyFileData = Control.getData(self.gameFolder + "party.json")
        party = partyFileData["party"]
        for character in party:
            tempCharacter = Character(str(character))
            self.characters.append(tempCharacter)

    def __init__(self, gameName):
        self.gameName = str(gameName)
        self.gameFolder = "games/" + self.gameName + "/"
        self.getCharacters()