import tkinter as tk
from threading import Timer

Level = 1
Coins = 0
HP = 50
Up = 0
Addcoins = 1
Attack = 1
AutoA = 0

root = tk.Tk()
root.title("Bombclick")
root.geometry("600x825")
root["bg"] = "white"
root.iconbitmap("icon.ico")
root.resizable(False, False)

M_images = [tk.PhotoImage(file="lvl1.png"),tk.PhotoImage(file="lvl2.png"),tk.PhotoImage(file="lvl3.png"),tk.PhotoImage(file="lvl4.png"),tk.PhotoImage(file="lvl5.png")]

upgrade_b = tk.PhotoImage(file="upgrade.png")
Autoattack = tk.PhotoImage(file="AutoAttack.png")
Title = tk.PhotoImage(file="Title.png")

def update():
    Hp.config(text = f"HP: {HP}")
    Lvl.config(text = f"Level: {Level}")
    coins.config(text = f"Coins: {Coins}")

def death():
    global Level
    global HP
    Level+=1
    click_button.config(image=M_images[Level - 1])
    HP = 50*Level
    update()
def upgrade():
    global Up
    global Addcoins
    global Attack
    if Up == 1:
        None
    elif Up == 0:
        Up += 1
        Addcoins += 4
        Attack += 4
        print(Up)


def click():
    global HP
    global Coins
    global Addcoins
    global Level
    HP-=Attack
    print(HP)
    if HP<=0:
        death()
    elif HP<0:
        HP = 0
        Addcoins = 0
        Level = 5
    update()
    Coins += Addcoins

def AutoAttack():
    global AutoA
    global HP
    if AutoA == 0:
        AutoA += 1
    elif AutoA == 1:
        startAttack()


def startAttack():
    global HP
    global Attack
    global Level
    global Addcoins
    global Coins
    HP-=Attack
    Coins += Addcoins
    if HP < 0:
        HP = 0
        Addcoins = 0
        Level = 5
    print("123")
    update()
    Timer(2,startAttack).start()



title = tk.Button(root, image=Title, background="white", command=click)
title.pack()
coins = tk.Label(font = ("Arial", 19), text = f"Coins: {Coins}", fg="black", background="white")
coins.pack()
Lvl = tk.Label(font = ("Arial", 19), text = f"Level: {Level}", fg="black", background="white")
Lvl.pack()

click_button = tk.Button(root, image=M_images[0], background="white", command=click) #command=click
click_button.pack()

Hp = tk.Label(font = ("Arial", 19), text = f"HP: {HP}", fg="black", background="white")
Hp.pack()

upgrade_button = tk.Button(root, image=upgrade_b, background="white", command=upgrade)
upgrade_button.pack()
Auto_button = tk.Button(root, image=Autoattack, background="white", command=AutoAttack)
Auto_button.pack()

root.mainloop()