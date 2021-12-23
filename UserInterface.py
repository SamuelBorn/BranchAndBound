import tkinter as tk

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

import numpy as np

window = tk.Tk()
window.wm_title("Sonderleistung")

scrollbar = tk.Scrollbar(window)
scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

t = np.arange(0, 3, .01)
fig1 = Figure(figsize=(7, 4))
fig1.add_subplot(111).plot(t, 2 * np.sin(2 * np.pi * t))

fig2 = Figure(figsize=(7, 4))
fig2.add_subplot(111).plot(t, 2 * np.cos(2 * np.pi * t))

fig3 = Figure(figsize=(7, 4))
fig3.add_subplot(111).plot(t, 2 * np.cos(2 * np.pi * t))

canvas = FigureCanvasTkAgg(fig1, master=window)
canvas.draw()
canvas.get_tk_widget().pack()

canvas = FigureCanvasTkAgg(fig2, master=window)
canvas.draw()
canvas.get_tk_widget().pack(fill=tk.BOTH)

canvas = FigureCanvasTkAgg(fig3, master=window)
canvas.draw()
canvas.get_tk_widget().pack(fill=tk.BOTH)

tk.mainloop()
