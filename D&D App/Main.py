from tkinter import *

from Character import *
from TurnOrder import *

class Main:
    window = Tk()
    turnOrder = TurnOrder("game", "battle")

    def __init__(self):
        self.window.geometry("960x600")
        self.window.mainloop()

if(__name__ == "__main__"):
    main = Main()