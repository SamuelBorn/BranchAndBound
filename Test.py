from tkinter import *
from tkinter import ttk
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np

root = Tk()
root.title('Learn To Code at Codemy.com')
root.geometry("500x400")

# Create A Main Frame
main_frame = Frame(root)
main_frame.pack(fill=BOTH, expand=1)

# Create A Canvas
my_canvas = Canvas(main_frame)
my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

# Add A Scrollbar To The Canvas
my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
my_scrollbar.pack(side=RIGHT, fill=Y)

# Configure The Canvas
my_canvas.configure(yscrollcommand=my_scrollbar.set)
my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

# Create ANOTHER Frame INSIDE the Canvas
second_frame = Frame(my_canvas)

# Add that New frame To a Window In The Canvas
my_canvas.create_window((0, 0), window=second_frame, anchor="nw")

for thing in range(100):
    t = np.arange(0, 3, .01)
    fig1 = Figure(figsize=(7, 4))
    fig1.add_subplot(111).plot(t, 2 * np.sin(2 * np.pi * t))
    canvas = FigureCanvasTkAgg(second_frame)
    canvas.get_tk_widget().pack(fill=tk.BOTH)
    Button(second_frame, text=f'Button {thing} Yo!').grid(row=thing, column=0, pady=10, padx=10)

root.mainloop()
