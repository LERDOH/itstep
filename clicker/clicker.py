import tkinter as tk
Level = 1
Coins = 0
HP = 5
if HP <0:
    hp = 0

root = tk.Tk()
root.title("Bombclick")
root.geometry("600x800")
root["bg"] = "grey"
#root.iconbitmap("like.ico")
root.resizable(False, False)

lvl_1 = tk.PhotoImage(file="lvl1.png")
lvl_2 = tk.PhotoImage(file="lvl2.png")
lvl_3 = tk.PhotoImage(file="lvl1.png")
lvl_4 = tk.PhotoImage(file="lvl1.png")
lvl_5 = tk.PhotoImage(file="lvl1.png")

def update():
    Hp.config(text = f"HP: {HP}")
    Lvl.config(text = f"Level: {Level}")
    coins.config(text = f"Coins: {Coins}")

def death():
    global Level
    global HP
    Level+=1
    if Level == 2:
        click_button.config(image=lvl_2)
        HP = 10
    elif Level == 3:
        click_button.config(image=lvl_2)
        HP = 15
    if Level == 4:
        click_button.config(image=lvl_2)
        HP = 20
    elif Level == 5:
        click_button.config(image=lvl_2)
        HP = 25



def click():
    global HP
    global Coins
    HP-=1
    print(HP)
    if HP<=0:
        death()
    Coins+=1
    update()

title = tk.Label(font = ("Arial", 20, "bold"), text = "Bombclick", fg="green", background="white")
title.pack()
coins = tk.Label(font = ("Arial", 14), text = f"Coins: {Coins}", fg="orange", background="grey")
coins.pack()
Lvl = tk.Label(font = ("Arial", 14), text = f"Level: {Level}", fg="orange", background="grey")
Lvl.pack()

click_button = tk.Button(root, image=lvl_1, background="grey", command=click) #command=click
click_button.pack()

Hp = tk.Label(font = ("Arial", 14), text = f"HP: {HP}", fg="orange", background="grey")
Hp.pack()

root.mainloop()