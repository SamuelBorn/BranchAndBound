import tkinter as tk

from LinearProgram import LinearProgram
from UserInterface.KeyDataFrame import KeyDataFrame

if __name__ == '__main__':
    root = tk.Tk()
    frame = KeyDataFrame(root)
    frame.grid(row=0, column=0, sticky="news")
    root.mainloop()
