import tkinter as tk

root = tk.Tk()
root.title("Bombclick")
root.geometry("600x800")
#root.iconbitmap("like.ico")
root.resizable(False, False)
title = tk.Label(font = ("Arial", 20, "bold"), text = "Bombclick", fg="green",relief=tk.RAISED)
title.pack()
coins = tk.Label(font = ("Arial", 14), text = "Coins = ", fg="orange")
coins.pack()
Lvl = tk.Label(font = ("Arial", 14), text = "Level = ", fg="orange")
Lvl.pack()

click_button = tk.Button(width=30, height=15) #command=click
click_button.pack()

root.mainloop()