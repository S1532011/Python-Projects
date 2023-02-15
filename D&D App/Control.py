import json

class Control:
    def getStatFromSkill(skillName):
        skillsFileData = Control.getData("source/skills.json")
        statName = skillsFileData[skillName]
        return statName
    
    def getData(fileName):
        file = open(fileName, "r")
        fileData = json.loads(file.read())
        file.close()
        return fileData