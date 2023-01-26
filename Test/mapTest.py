import tkinter
from tkinter import *

map = [
    ["wall1","wall1","wall1","wall1","wall1","wall1","wall1","wall1","wall1"],
    ["wall1","light1","light1","light1","light1","light1","light1","light1","wall1"],
    ["wall1","light1","light1","light1","light1","light1","light1","light1","wall1"],
    ["wall1","light1","light1","light1","wall1","light1","light1","light1","wall1"],
    ["wall1","light1","light1","light1","wall1","light1","light1","light1","wall1"],
    ["wall1","light1","light1","light1","light1","light1","light1","light1","wall1"],
    ["wall1","light1","light1","light1","light1","light1","light1","light1","wall1"],
    ["wall1","light1","light1","light1","light1","light1","light1","light1","wall1"],
    ["wall1","wall1","wall1","wall1","wall1","wall1","wall1","wall1","wall1"]
]

window = Tk()
window.geometry("640x360")

canvas = tkinter.Canvas(window, bg="white", height=300, width=300)

x = 0
y = 0
size = 10

for i in map:
    for j in i:
        if(j == "wall1"):
            canvas.create_polygon(x * size, y * size, x * size + size, y * size, x * size + size, y * size + size, x * size, y * size + size, fill = "black")
        elif(j == "light1"):
            canvas.create_polygon(x * size, y * size, x * size + size, y * size, x * size + size, y * size + size, x * size, y * size + size, fill= "white")
        x += 1
    y += 1
    x = 0

canvas.pack()
window.mainloop()
