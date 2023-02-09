import json

class Character:
    def getData(self, characterFile):
        file = open(characterFile, "r")
        character = json.dumps(file.read())
        file.close()
        return character
    
    def __init__(self):
        self.getData()