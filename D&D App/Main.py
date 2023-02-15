import json
from tkinter import *

from Character import *
from TurnOrder import *

class Main:
    character1 = Character("ander_zytolga")
    print("Speed:", character1.getSpeed())
    print("Proficiency Bonus:", character1.getProficiencyBonus())
    print("Dexterity Modifier:", character1.getStatModifier("dexterity"))
    print("Stealth:", character1.getSkillModifier("stealth"))
    # window = Tk()
    # turnOrder = TurnOrder("game", "battle")

    # def __init__(self):
    #     self.window.geometry("960x600")
    #     self.window.mainloop()

if(__name__ == "__main__"):
    main = Main()