import json
import os
import shutil

from MapTriggers import *
from Player import *

class Map:
    def getMapData():
        saveFilePath = Player.getCurrentMap()
        originalFilePath = str(saveFilePath).replace("save","maps",1)
        if(os.path.exists(saveFilePath) == False):
            shutil.copyfile(originalFilePath, saveFilePath)
        
        file = open(saveFilePath, "r")

        jsonObject = json.loads(file.read())

        return jsonObject

    def getOtherMapData(fileName):
        file = open(fileName, "r")
        jsonObject = json.loads(file.read())

        return jsonObject

    def setMapData(mapData):
        file = open(Player.getCurrentMap(), "W")

    def printMap():
        mapFile = getMapData()

        if mapFile["mapType"] == "simple":
            Map.printMapSimple(mapFile)
        elif mapFile["mapType"] == "text":
            Map.printMapText(mapFile)
        elif mapFile["mapType"] == "unicode":
            Map.printMapUnicode(mapFile)
        else:
            return -1

    def printMapSimple(mapFile):
        map = mapFile["map"]
        y = 0
        x = 0
        for i in map:
            for j in i:
                print(j, end = "")
                if(x == Player.getPlayerX() and y == Player.getPlayerY()):
                    print("\b" + Player.getPlayerIcon(), end = "")
                x = x + 1
            print("")
            y = y + 1
            x = 0

    def printMapText(mapFile):
        map = mapFile["map"]
        y = 0
        x = 0
        for i in map:
            for j in i:
                if(j == "wall1" or j == "ghost1"):
                    print(Map.wallStyle(y,x,map,1), end = "")
                elif(j == "wall2" or j == "ghost2"):
                    print(Map.wallStyle(y,x,map,2), end = "")
                elif(j == "light1" or j == "kaizo1"):
                    print("░", end = "")
                elif(j == "light2" or j == "kaizo2"):
                    print("▒", end = "")
                elif(j == "dark1" or j == "kaizo3"):
                    print("▓", end = "")
                elif(j == "dark2" or j == "kaizo4"):
                    print("█", end = "")
                elif(j == "up1"):
                    print("▲", end = "")
                elif(j == "down1"):
                    print("▼", end = "")
                elif(j == "left1"):
                    print("◄", end = "")
                elif(j == "right1"):
                    print("►", end = "")
                elif(j == "up2"):
                    print("↑", end = "")
                elif(j == "down2"):
                    print("↓", end = "")
                elif  j == "left2":
                    print("←", end = "")
                elif  j == "right2":
                    print("→", end = "")
                elif  j == "":
                    print("�", end = "")
                else:
                    print(j, end = "")
                if(x == Player.getPlayerX() and y == Player.getPlayerY()):
                    print("\b" + Player.getPlayerIcon(), end = "")
                x = x + 1
            print("")
            y = y + 1
            x = 0

    def printMapUnicode(mapFile):
        map = mapFile["map"]
        y = 0
        x = 0
        for i in map:
            for j in i:
                print(j, end = "")
                if(x == Player.getPlayerX() and y == Player.getPlayerY()):
                    print("\b" + Player.getPlayerIcon(), end = "")
                x = x + 1
            print("")
            y = y + 1
            x = 0

    def wallStyle(i,j,map,wallType):
        north = Map.wallExists((i-1),j,map)
        east = Map.wallExists(i,(j+1),map)
        south = Map.wallExists((i+1),j,map)
        west = Map.wallExists(i,(j-1),map)

        if (wallType == 1):
            if (north and east and south and west):
                wallStyle = "╬"
            elif (north and east and south):
                wallStyle = "╠"
            elif (east and south and west):
                wallStyle = "╦"
            elif (south and west and north):
                wallStyle = "╣"
            elif (west and north and east):
                wallStyle = "╩"
            elif (north and east):
                wallStyle = "╚"
            elif (east and south):
                wallStyle = "╔"
            elif (south and west):
                wallStyle = "╗"
            elif (west and north):
                wallStyle = "╝"
            elif (north or south):
                wallStyle = "║"
            else:
                wallStyle = "═"
        else:
            if (north and east and south and west):
                wallStyle = "╬"
            elif (north and east and south):
                wallStyle = "╠"
            elif (east and south and west):
                wallStyle = "╦"
            elif (south and west and north):
                wallStyle = "╣"
            elif (west and north and east):
                wallStyle = "╩"
            elif (north and east):
                wallStyle = "╚"
            elif (east and south):
                wallStyle = "╔"
            elif (south and west):
                wallStyle = "╗"
            elif (west and north):
                wallStyle = "╝"
            elif (north or south):
                wallStyle = "║"
            else:
                wallStyle = "═"

        return wallStyle

    def wallExists(i,j,map):
        doesWallExist = False

        if (i >= 0 and j >= 0 and i < len(map) and j < len(map[i])):
            if (map[i][j] == "wall1" or map[i][j] == "wall2" or map[i][j] == "ghost1" or map[i][j] == "ghost2"):
                doesWallExist = True

        return doesWallExist

    def wallExistsPlayer(i,j,map):
        doesWallExist = False

        if (i >= 0 and j >= 0 and i < len(map) and j < len(map[i])):
            if (map[i][j] == "wall1" or map[i][j] == "wall2" or map[i][j] == "kaizo1" or map[i][j] == "kaizo2" or map[i][j] == "kaizo3" or map[i][j] == "kaizo4"):
                doesWallExist = True

        return doesWallExist
        