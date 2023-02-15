import json
import random

class Control:
    def roll(rollValue):
        numDice = int(rollValue[0:rollValue.find("d")])
        diceValue = int(rollValue[rollValue.find("d") + 1:rollValue.find("+")])
        rollResult = int(rollValue[rollValue.find("+") + 1:])
        for i in range(numDice):
            rollResult += random.randint(0, diceValue)

        return rollResult
    def getStatFromSkill(skillName):
        skillsFileData = Control.getData("source/skills.json")
        statName = skillsFileData[skillName]
        return statName
    
    def getData(fileName):
        file = open(fileName, "r")
        fileData = json.loads(file.read())
        file.close()
        return fileData