import json
import random

class Control:
    def roll(rollValue):
        numDice = int(rollValue[0:rollValue.find("d")])
        diceValue = int(rollValue[rollValue.find("d") + 1:rollValue.find("+")])
        rollResult = int(rollValue[rollValue.find("+") + 1:])
        for i in range(numDice):
            rollResult += random.randint(1, diceValue)

        return rollResult
    
    def getInfo(fileName, data):
        fileData = Control.getData("source/" + str(fileName) + ".json")
        return fileData[data]

    def getStatFromSkill(skillName):
        skillsFileData = Control.getData("source/skills.json")
        statName = skillsFileData[skillName]
        return statName
    
    def getData(fileName):
        file = open(fileName, "r")
        fileData = json.loads(file.read())
        file.close()
        return fileData
    
    def setData(fileName, fileData):
        file = open(fileName, "w")
        file.write(json.dumps(fileData))
        file.close()
        