import json

class Player:
    def getPlayerData():
        file = open("playerData.json", "r")
        playerData = json.loads(file.read())
        file.close()
        return playerData

    def getPlayerX():
        return int(Player.getPlayerData()["X"])

    def getPlayerY():
        return int(Player.getPlayerData()["Y"])

    def getSavedX():
        return int(Player.getPlayerData()["X2"])

    def getSavedY():
        return int(Player.getPlayerData()["Y2"])

    def getPlayerIcon():
        return Player.getPlayerData()["icon"]

    def getUseState(useButton):
        return Player.getPlayerData()[useButton]

    def getEditorMode():
        return Player.getPlayerData()["editorMode"]

    def setPlayerData(newPlayerData):
        file = open("playerData.json", "w")
        file.write(json.dumps(newPlayerData))
        file.close()

    def setPlayerX(newX):
        player = Player.getPlayerData()
        player["X"] = newX
        Player.setPlayerData(player)

    def setPlayerY(newY):
        player = Player.getPlayerData()
        player["Y"] = newY
        Player.setPlayerData(player)

    def setPlayerPos(newX, newY):
        player = Player.getPlayerData()
        player["X"] = newX
        player["Y"] = newY
        Player.setPlayerData(player)

    def setSavedX(newX):
        player = Player.getPlayerData()
        player["X2"] = newX
        Player.setPlayerData(player)

    def setSavedY(newY):
        player = Player.getPlayerData()
        player["Y2"] = newY
        Player.setPlayerData(player)

    def setSavedPos(newX, newY):
        player = Player.getPlayerData()
        player["X2"] = newX
        player["Y2"] = newY
        Player.setPlayerData(player)

    def setPlayerIcon(newIcon):
        player = Player.getPlayerData()
        player["icon"] = newIcon
        Player.setPlayerData(player)

    def setUseState(useState, useButton):
        player = Player.getPlayerData()
        player[useButton] = useState
        Player.setPlayerData(player)

    def setInventory(inventory):
        player = Player.getPlayerData()
        player["inventory"] = inventory
        Player.setPlayerData(player)

    def getInventory():
        player = Player.getPlayerData()
        return player["inventory"]

    def giveItem(item):
        if(Player.itemExists(item["itemID"]) == False):
            inventory = Player.getInventory()
            inventory.append(item)
            Player.setInventory(inventory)

    def removeItem(item):
        if(Player.itemExists(item["itemID"]) == True):
            inventory = Player.getInventory()
            inventory.remove(item)
            Player.setInventory(inventory)

    def getPlayerItem(itemID):
        inventory = Player.getInventory()
        for item in inventory:
            if(item["itemID"] == itemID):
                return item

    def getPlayerItemNum(itemID):
        inventory = Player.getInventory()
        i = 0
        for item in inventory:
            if(item["itemID"] == itemID):
                return item
            i = i + 1

    def itemExists(itemID):
        inventory = Player.getInventory()
        control = False
        for item in inventory:
            if(item["itemID"] == itemID):
                control = True
        return control

    def testForItem(condition):
        if(Player.itemExists(condition["itemID"])):
            if(condition["consumable"] == True):
                Player.removeItem(condition["itemID"])
            return True
        else:
            return False

    def getCurrentMap():
        player = Player.getPlayerData()
        return player["currentMap"]

    def setCurrentMap(fileName):
        player = Player.getPlayerData()
        player["currentMap"] = fileName
        Player.setPlayerData(player)

    def getSavedMap():
        player = Player.getPlayerData()
        return player["savedMap"]

    def setSavedMap(fileName):
        player = Player.getPlayerData()
        player["savedMap"] = fileName
        Player.setPlayerData(player)
