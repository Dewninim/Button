import tkinter as tk

root = tk.Tk()
root.title("tkinter Button")

label = tk.Label(root, text= "Hello!!")
label.pack()

def on_btn_click():
    label.config(text="Button Clicked")

button = tk.Button(root, text= "Click Me" , command = on_btn_click)
button.pack()

root.mainloop()
