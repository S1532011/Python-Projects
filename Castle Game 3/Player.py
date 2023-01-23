import json


def getPlayerData():
    file = open("playerData.json", "r")
    playerData = json.loads(file.read())
    file.close()
    return playerData

def getPlayerX():
    return int(getPlayerData()["X"])

def getPlayerY():
    return int(getPlayerData()["Y"])

def getSavedX():
    return int(getPlayerData()["X2"])

def getSavedY():
    return int(getPlayerData()["Y2"])

def getPlayerIcon():
    return getPlayerData()["icon"]

def getUseState(useButton):
    return getPlayerData()[useButton]

def getEditorMode():
    return getPlayerData()["editorMode"]

def setPlayerData(newPlayerData):
    file = open("playerData.json", "w")
    file.write(json.dumps(newPlayerData))
    file.close()

def setPlayerX(newX):
    player = getPlayerData()
    player["X"] = newX
    setPlayerData(player)

def setPlayerY(newY):
    player = getPlayerData()
    player["Y"] = newY
    setPlayerData(player)

def setPlayerPos(newX, newY):
    player = getPlayerData()
    player["X"] = newX
    player["Y"] = newY
    setPlayerData(player)

def setSavedX(newX):
    player = getPlayerData()
    player["X2"] = newX
    setPlayerData(player)

def setSavedY(newY):
    player = getPlayerData()
    player["Y2"] = newY
    setPlayerData(player)

def setSavedPos(newX, newY):
    player = getPlayerData()
    player["X2"] = newX
    player["Y2"] = newY
    setPlayerData(player)

def setPlayerIcon(newIcon):
    player = getPlayerData()
    player["icon"] = newIcon
    setPlayerData(player)

def setUseState(useState, useButton):
    player = getPlayerData()
    player[useButton] = useState
    setPlayerData(player)

def setInventory(inventory):
    player = getPlayerData()
    player["inventory"] = inventory
    setPlayerData(player)

def getInventory():
    player = getPlayerData()
    return player["inventory"]

def addItem(item):
    if(itemExists(item["itemID"]) == False):
        inventory = getInventory()
        inventory.append(item)
        setInventory(inventory)

def removeItem(item):
    if(itemExists(item["itemID"]) == True):
        inventory = getInventory()
        inventory.remove(item)
        setInventory(inventory)

# def removeItem(itemID):
#     player = getPlayerData()
#     player["inventory"].remove(getPlayerItem(itemID))
#     setPlayerData(player)

def getPlayerItem(itemID):
    inventory = getInventory()
    for item in inventory:
        if(item["itemID"] == itemID):
            return item

def getPlayerItemNum(itemID):
    inventory = getInventory()
    i = 0
    for item in inventory:
        if(item["itemID"] == itemID):
            return item
        i = i + 1

def itemExists(itemID):
    inventory = getInventory()
    control = False
    for item in inventory:
        if(item["itemID"] == itemID):
            control = True
    return control

def testForItem(condition):
    if(itemExists(condition["itemID"])):
        if(condition["consumable"] == True):
            removeItem(condition["itemID"])
        return True
    else:
        return False

def getCurrentMap():
    player = getPlayerData()
    return player["currentMap"]

def setCurrentMap(fileName):
    player = getPlayerData()
    player["currentMap"] = fileName
    setPlayerData(player)

def getSavedMap():
    player = getPlayerData()
    return player["savedMap"]

def setSavedMap(fileName):
    player = getPlayerData()
    player["savedMap"] = fileName
    setPlayerData(player)
