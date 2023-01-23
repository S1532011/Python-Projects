from BasicInput import *
from Map import *
from Player import *
from Functions import *
from MapTriggers import *


startGame()

while True:
    os.system("cls")
    if(testTriggers("teleport") == "quit"):
        break
    print(str(getPlayerX()) + " " + str(getPlayerY()))
    printMap()
    testTriggers("text")
    getInput()