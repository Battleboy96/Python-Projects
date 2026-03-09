import tkinter as tk

window = tk.Tk()
window.title("Window Testing")
window.geometry("300x300")

label = tk.Label(window, text="")
label.pack()

def on_click():
    label.config(text="Button Clicked!")
    
button = tk.Button(window, text="Click me!", command=on_click)
button.pack()
window.mainloop()
