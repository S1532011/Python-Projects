import json

class Character:
    character = {}

    def getData(self, character):
        characterFile = "players/" + character + ".json"
        file = open(characterFile, "r")
        character = json.dumps(file.read())
        file.close()
        return character
    
    def __init__(self, character):
        self.character = self.getData(character)