from tkinter import *
window = Tk()
window.title('Event Handler')
window.geometry('100x100')

def handle_keypress(event):
    """Print the character associated with the key pressed"""
    print(event.char)

window.bind("<keys", handle_keypress)

def handle_click(event):
    print("\nThe button clicked")


button = Button(text="Click me")
button.pack()

button.bind("<Button-1>", handle_click)

window.mainloop()