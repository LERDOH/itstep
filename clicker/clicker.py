import tkinter as tk
Level = 1
Coins = 0
HP = 50
Up = 0
Addcoins = 1
Attack = 1

root = tk.Tk()
root.title("Bombclick")
root.geometry("600x800")
root["bg"] = "grey"
#root.iconbitmap("like.ico")
root.resizable(False, False)

lvl_1 = tk.PhotoImage(file="lvl1.png")
lvl_2 = tk.PhotoImage(file="lvl2.png")
lvl_3 = tk.PhotoImage(file="lvl3.png")
lvl_4 = tk.PhotoImage(file="lvl4.png")
lvl_5 = tk.PhotoImage(file="lvl5.png")
upgrade_b = tk.PhotoImage(file="upgrade.png")

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
        click_button.config(image=lvl_3)
        HP = 15
    if Level == 4:
        click_button.config(image=lvl_4)
        HP = 20
    elif Level == 5:
        click_button.config(image=lvl_5)
        HP = 25

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
    HP-=Attack
    print(HP)
    if HP<=0:
        death()
    update()
    Coins += Addcoins

def AutoAttack():
    print ("Auto")

title = tk.Label(font = ("Arial", 20, "bold"), text = "Bombclick", fg="green", background="white")
title.pack()
coins = tk.Label(font = ("Arial", 14), text = f"Coins: {Coins}", fg="orange", background="grey")
coins.pack()
Lvl = tk.Label(font = ("Arial", 14), text = f"Level: {Level}", fg="orange", background="grey")
Lvl.pack()

click_button = tk.Button(root, image=lvl_1, background="grey", command=click) #command=click
click_button.pack()
upgrade_button = tk.Button(root, image=upgrade_b, background="grey", command=upgrade)
upgrade_button.pack()
Auto_button = tk.Button(root, image=upgrade_b, background="grey", command=AutoAttack)
Auto_button.pack()


Hp = tk.Label(font = ("Arial", 14), text = f"HP: {HP}", fg="orange", background="grey")
Hp.pack()

root.mainloop()