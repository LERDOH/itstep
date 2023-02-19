import tkinter as tk

root = tk.Tk()
root.title("Bombclick")
root.geometry("600x825")
root.resizable(False, False)

M_images = [tk.PhotoImage(file="lvl1.png"), tk.PhotoImage(file="lvl2.png")]

#lvl_1 = tk.PhotoImage(file="lvl1.png")

print (M_images[0])
print (M_images[1])

root.mainloop()