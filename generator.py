import sqlite3
from tkinter import *
from tkinter import messagebox
import random 

#list of lines
pickup = list()

#functions(3)
def pickuplines():
    index = random.randrange(0,len(data))
    lineStr = str(data[index])
    for char in ["{","}","(",")",","]:
        lineStr=lineStr.replace(char,"")
    line.config(text=lineStr)




#connect database(1)
conn = sqlite3.connect("pick-lines.db")
cur = conn.cursor()
cur.execute('SELECT line FROM Picklines')
data = cur.fetchall()

#make our UI & components(2)
root = Tk()
root.geometry("750x500+560+200")
root.title("Pick Lines")
root.columnconfigure(0, weight=1)
image_icon = PhotoImage(file="icon.png")
root.iconphoto(False, image_icon)

#pick-up line
lineStr = "LMAO! 😂, you fu*king nerd just press the below ⬇ button"
line = Label(root, text=lineStr, font=("monospace", 16), width=80, height=3)
line.grid(pady=(70))

#next line button
nextLine = Button(root, text="get another❤", width=14, font=("consolas"), bg="#2a9d8f", fg="#dee2e6", command=pickuplines)
nextLine.grid(pady=(10))


root.mainloop()