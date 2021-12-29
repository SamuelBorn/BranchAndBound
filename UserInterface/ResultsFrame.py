import tkinter as tk
from tkinter import ttk

import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

import DrawEquationUtils
import DrawGraphUtils
from LinearProgram import LinearProgram


class ResultsFrame(tk.Frame):

    def _on_mousewheel(self, event):
        self.cv.yview_scroll(-1 * (event.delta / 120), "units")

    def __init__(self, parent, lin_prog):
        tk.Frame.__init__(self, parent)

        # create a canvas object and a vertical scrollbar for scrolling it
        v_scrollbar = tk.Scrollbar(self, orient=tk.VERTICAL)
        v_scrollbar.pack(fill=tk.Y, side=tk.RIGHT, expand=tk.FALSE)
        canvas = tk.Canvas(self, bd=0, highlightthickness=0, yscrollcommand=v_scrollbar.set)
        self.cv = canvas
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=tk.TRUE)
        v_scrollbar.config(command=canvas.yview)

        # reset the view
        canvas.xview_moveto(0)
        canvas.yview_moveto(0)

        # create a frame inside the canvas which will be scrolled with it
        self.interior = interior = tk.Frame(canvas)
        interior_id = canvas.create_window(0, 0, window=interior, anchor=tk.NW)

        # track changes to the canvas and frame width and sync them,
        # also updating the scrollbar
        def _configure_interior(event):
            # update the scrollbars to match the size of the inner frame
            size = (interior.winfo_reqwidth(), interior.winfo_reqheight())
            canvas.config(scrollregion="0 0 %s %s" % size)
            if interior.winfo_reqwidth() != canvas.winfo_width():
                # update the canvas's width to fit the inner frame
                canvas.config(width=interior.winfo_reqwidth())

        interior.bind('<Configure>', _configure_interior)

        def _configure_canvas(event):
            if interior.winfo_reqwidth() != canvas.winfo_width():
                # update the inner frame's width to fill the canvas
                canvas.itemconfigure(interior_id, width=canvas.winfo_width())

        canvas.bind('<Configure>', _configure_canvas)

        for i in range(1):
            DrawEquationUtils.draw_equations(lin_prog, self.interior)
            DrawGraphUtils.draw_graph(lin_prog, self.interior)
            # l = tk.Label(self.interior, text="3x + 4x <= 4")
            # l.pack()
            #
            # t = np.arange(0, 3, .01)
            # fig = Figure(figsize=(7, 4))
            # fig.add_subplot(111).plot(t, 2 * np.sin(2 * np.pi * t))
            # FigureCanvasTkAgg(fig, master=self.interior).get_tk_widget().pack(fill=tk.BOTH)


if __name__ == '__main__':
    root = tk.Tk()
    lin_prog = LinearProgram([[2, 1, 10], [1, 0, 3], [0, 1, 3], [-1, 0, 0], [0, -1, 0]],
                             [-2, -2], True)
    frame = ResultsFrame(root, lin_prog)
    frame.pack(fill=tk.BOTH, expand=1)
    root.geometry("800x800")
    root.mainloop()
