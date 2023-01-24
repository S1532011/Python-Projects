import json

class Player:
    def getData(playerFile):
        file = open(playerFile, "r")
        player = json.dumps(file.read())
        file.close()
        return player

    def getName(playerFile):
        player = Player.getData(playerFile)
        return player["name"]

    def getRace(playerFile):
        player = Player.getData(playerFile)
        return player["race"]
    
    def getSubRace(playerFile):
        player = Player.getData(playerFile)
        return player["race"]

    def getClass(playerFile):
        player = Player.getData(playerFile)
        return player["class"]

    def getSubClass(playerFile):
        player = Player.getData(playerFile)
        return player["subClass"]

    def getArmorClass(playerFile):
        player = Player.getData(playerFile)
        return player["armorClass"]

    def getHealth(playerFile):
        player = Player.getData(playerFile)
        return player["health"]

    def getMaxHealth(playerFile):
        player = Player.getData(playerFile)
        return player["maxHealth"]

    def getLevel(playerFile):
        player = Player.getData(playerFile)
        return player["level"]

    def getProficiencyBonus(playerFile):
        player = Player.getData(playerFile)
        return player["proficiencyBonus"]

    def getSpeed(playerFile):
        player = Player.getData(playerFile)
        return player["speed"]

    def getInitiative(playerFile):
        player = Player.getData(playerFile)
        return player["initiative"]

    def getPassivePerception(playerFile):
        player = Player.getData(playerFile)
        return player["passivePerception"]

    def getAlignment(playerFile):
        player = Player.getData(playerFile)
        return player["alignment"]
    
    def getMorals(playerFile):
        alignment = Player.getAlignment(playerFile)
        return alignment["morals"]

    def getEthics(playerFile):
        alignment = Player.getAlignment(playerFile)
        return alignment["ethics"]

    def getSpells(playerFile):
        player = Player.getData(playerFile)
        return player["spells"]

    # Add functions to get a spell by ID, name, add a spell, and remove a spell

    def getStats(playerFile):
        player = Player.getData(playerFile)
        return player["stats"]
    
    def getStrength(playerFile):
        stats = Player.getStats(playerFile)
        return stats["strength"]

    def getDexterity(playerFile):
        stats = Player.getStats(playerFile)
        return stats["dexterity"]

    def getConstitution(playerFile):
        stats = Player.getStats(playerFile)
        return stats["constitution"]

    def getIntelligence(playerFile):
        stats = Player.getStats(playerFile)
        return stats["intelligence"]

    def getWisdom(playerFile):
        stats = Player.getStats(playerFile)
        return stats["wisdom"]

    def getCharisma(playerFile):
        stats = Player.getStats(playerFile)
        return stats["charisma"]
    
    def getStat(playerFile, stat):
        stats = Player.getStats(playerFile)
        return stats[stat]

    def getDeathSaves(playerFile):
        player = Player.getData(playerFile)
        return player["deathSaves"]
    
    def getDeathSuccesses(playerFile):
        deathSaves = Player.getDeathSaves(playerFile)
        return deathSaves["successes"]
    
    def getDeathFails(playerFile):
        deathSaves = Player.getDeathSaves(playerFile)
        return deathSaves["fails"]

    def getInventory(playerFile):
        player = Player.getData(playerFile)
        return player["inventory"]
    
    # get Inventory item by name, ID, give item, and remove item

    def getCurrencies(playerFile):
        player = Player.getData(playerFile)
        return player["currency"]
    
    def getCurrency(playerFile, currency):
        currencies = Player.getCurrencies(playerFile)
        return currencies[currency]
    
    def getCopper(playerFile):
        currency = Player.getCurrency(playerFile)
        return currency["copper"]

    def getSilver(playerFile):
        currency = Player.getCurrency(playerFile)
        return currency["silver"]

    def getElectrum(playerFile):
        currency = Player.getCurrency(playerFile)
        return currency["electrum"]

    def getGold(playerFile):
        currency = Player.getCurrency(playerFile)
        return currency["gold"]

    def getPlatinum(playerFile):
        currency = Player.getCurrency(playerFile)
        return currency["platinum"]

    def getLanguages(playerFile):
        player = Player.getData(playerFile)
        return player["languages"]

    def getConditions(playerFile):
        player = Player.getData(playerFile)
        return player["conditions"]
    
    def getCondition(playerFile, condition):
        conditions = Player.getConditions(playerFile)
        return conditions[condition]