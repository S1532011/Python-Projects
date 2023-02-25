from tkinter import *

from Game import *
from Window import *

class Main:

    def __init__(self, gameName, battleName):   
        Window.window.geometry("960x600")
        Window.window.wm_attributes("-transparentcolor", "#ab23ff")

        game = Game(gameName, battleName)
        battleSave = game.getBattleSave()
        game.setTurnOrder()

        print(game.turnOrder)
        str = StringVar()
        def showInfo(creature):
                game.showInfo(creature)

        for i in range(0, len(game.turnOrder)):
            # button = Button(self.window, text=Game.getCreatureName(game.turnOrder[i]))
            button = Button(Window.window, text=game.turnOrder[i], width=25, anchor="w", command=lambda creature=game.turnOrder[i]:showInfo(creature))
            button.grid(column=0, row=i, padx=2, pady=2)

        Window.window.mainloop()

if(__name__ == "__main__"):
    # gameName = input("Enter game name: ")
    # battleName = input("Enter battle name: ")
    # main = Main(gameName, battleName)
    main = Main("obliette", "tall_room")