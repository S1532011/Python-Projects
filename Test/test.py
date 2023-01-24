from tkinter import *
from tkinter import scrolledtext
from tkinter import messagebox
from tkinter.ttk import Progressbar
from tkinter.ttk import Combobox, Checkbutton

def btn1Clicked():
    lbl1.configure(text = "Button Clicked!")

def setText():
    lbl1.configure(text = txt.get())
    lbl2.configure(text = combo.get())

window = Tk()
window.title("Castle Game")

lbl1 = Label(window, text = "Hello", font = ("Aria Bold", 50))
lbl1.grid(column = 0, row = 0)

lbl2 = Label(window)
lbl2.grid(column = 1, row = 2)

btn1 = Button(window, text = "quit", command = window.destroy, bg = "orange", fg = "red")
btn1.grid(column = 0, row = 1)

txt = Entry(window, width = 10, state = "normal")
txt.grid(column = 0, row = 3)

btn2 = Button(window, text = "Set Text", command = setText)
btn2.grid(column = 1, row = 3)

txt.focus()

combo = Combobox(window)
combo["values"] = ("Apples","Oranges","Bananas")
combo.current(2)
combo.grid(column = 1, row = 0)

chk_state = BooleanVar()
chk_state.set(True) #set check state
chk = Checkbutton(window, text='Choose', var=chk_state)
chk.grid(column=0, row=4)

selected = IntVar()
rad1 = Radiobutton(window, text = "First", value = 1, variable = selected, command = setText)
rad2 = Radiobutton(window, text = "Second", value = 2, variable = selected)
rad3 = Radiobutton(window, text = "Third", value = 3, variable = selected)
rad1.grid(column = 2, row = 0)
rad2.grid(column = 2, row = 1)
rad3.grid(column = 2, row = 2)

txt2 = scrolledtext.ScrolledText(window, height = 5, width = 10)
txt2.grid(column = 0, row = 5)
txt2.insert(INSERT, "text")

def messageBox():
    messagebox.showinfo('Alert!','You clicked the button, HOORAY!!!')
    # res = messagebox.askquestion('Message title','Message content')

    # res = messagebox.askyesno('Message title','Message content')

    # res = messagebox.askyesnocancel('Message title','Message content')

    # res = messagebox.askokcancel('Message title','Message content')

    # res = messagebox.askretrycancel('Message title','Message content')
    # messagebox.showwarning('Message title', 'Message content')  #shows warning message
    # messagebox.showerror('Message title', 'Message content')    #shows error message
btn = Button(window,text = 'Click here', command = messageBox)
btn.grid(column=1,row=5)

spinBoxVar = IntVar()
spinBoxVar.set(20)

spin = Spinbox(window, from_=0, to=100, width = 10, textvariable = spinBoxVar)
spin.grid(column = 2, row = 5)

spin2 = Spinbox(window, values = (1, 3, 5, 7, 9))
spin2.grid(column = 3, row = 5)

bar = Progressbar(window, length = 200)
bar["value"] = 70
bar.grid(column = 0, row = 6)
 
window.geometry("640x360")
# window.geometry("350x200")

window.mainloop()
