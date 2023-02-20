import json
from tkinter import *

from Game import *

class Main:
    game = Game("chrono_trigger")
    print(game.characters[0].character["equipment"][0]["item_name"])
    # window = Tk()
    # turnOrder = TurnOrder("game", "battle")

    # def __init__(self):
    #     self.window.geometry("960x600")
    #     self.window.mainloop()

if(__name__ == "__main__"):
    main = Main()