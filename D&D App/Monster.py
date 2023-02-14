import json

class Monster:
    def getData(self, monster):
        try:
            monsterFile = "source/monsters/" + str(monster) + ".json"
            file = open(monsterFile, "r")
            monsterData = json.dumps(file.read())
            file.close()
            return monsterData
        except FileNotFoundError():
            return "{}"
    
    def __init__(self, monster):
        monsterData = self.getData(monster)