import json
from tkinter import *

from Game import *

class Main:
    game = Game("obliette", "tall_room")
    for monster in game.monsters:
        print(monster["id"], end=", ")
        print(monster["data"].rollHitPoints(), end="")
        print()
    print(game.getBattleSave())
    # window = Tk()

    # def __init__(self):
    #     self.window.geometry("960x600")
    #     self.window.mainloop()

if(__name__ == "__main__"):
    main = Main()