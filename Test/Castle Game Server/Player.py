import uuid
import json
import time

class Player:
    def getPlayerDataFile(this, playerId):
        file = open(playerId + ".json", "r")
        playerData = json.dumps(file.read())
        return playerData
    
    def getPlayerDataFileOld(this, playerId):
        file = open(playerId + ".json.old", "r")
        playerDataOld = json.dumps(file.read())
        return playerDataOld

    def getPlayerDataValue(this, playerId, valueName):
        playerData = this.getPlayerDataFile(playerId)
        return playerData["valueName"]
    
    def getPlayerDataValueOld(this, playerId, valueName):
        playerData = this.getPlayerDataFileOld(playerId)
        return playerData["valueName"]
    
    # def setPlayerDataFile(this, playerId):
    #     file = open(playerId + ".json", "r")
    #     playerData = json.dumps(file.read())
    #     return playerData
    
    # def setPlayerDataFileOld(this, playerId):
    #     file = open(playerId + ".json.old", "r")
    #     playerDataOld = json.dumps(file.read())
    #     return playerDataOld

    # def setPlayerDataValue(this, playerId, valueName):
    #     playerData = this.getPlayerDataFile(playerId)
    #     return playerData["valueName"]
    
    # def setPlayerDataValueOld(this, playerId, valueName):
    #     playerData = this.getPlayerDataFileOld(playerId)
    #     return playerData["valueName"]
    
    def newPlayer(this, ip_address, name):
        playerData = this.getPlayerDataFile()
        player_id = uuid.uuid4()
        date_joined = time.ctime()

        playerData["player_id"] = player_id
        playerData["ip_address"] = ip_address
        playerData["date_joined"] = date_joined
        playerData["name"] = name

        setPlayerDataFile(playerData)
        
