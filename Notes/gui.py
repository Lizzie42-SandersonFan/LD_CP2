# GUI notes
import tkinter as tk


root = tk.Tk()
# Everything we want to happen must be inbetween these two commands

root.title("Testing")
root.configure(background="orange")
root.minsize(250, 250)
root.maxsize(1000,1000)
root.geometry("300x300+100+100") # Starting size, x start, y start
label = tk.Label(root, text="This is currently working!", font=("Comic Sans", 14, "bold"))
label.config(fg = "purple", background="orange")
# Button
root.count = 0
def add():
    root.count += 1
    tk.Label(root, text=root.count).pack()

btn = tk.Button(root, text="ADD", command=add)
btn.pack()


label.pack()
#image = tk.PhotoImage(file = "Notes\imgs\swiss_cheese.png")
#tk.Label(root, image=image).pack()

root.mainloop()