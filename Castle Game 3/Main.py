from BasicInput import *
from Map import *
from Player import *
from Functions import *
from MapTriggers import *


startGame()

while True:
    os.system("cls")
    if(MapTriggers.testTriggers("teleport") == "quit"):
        break
    print(str(Player.getPlayerX()) + " " + str(Player.getPlayerY()))
    Map.printMap()
    MapTriggers.testTriggers("text")
    getInput()