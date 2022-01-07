import tkinter as tk

from LinearProgram import LinearProgram
from Utils.BranchAndBoundSolver import BranchAndBoundSolver
from Utils.ProblemSelector import LIFOSelector, MaxUpperBoundSelector


class ResultsFrame(tk.Frame):

    def _on_mousewheel(self, event):
        self.cv.yview_scroll(-1 * (event.delta / 120), "units")

    def __init__(self, parent):
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


if __name__ == '__main__':
    root = tk.Tk()
    lin_prog = LinearProgram([[2, 1, 4], [1, 2, 4], [-1, 0, 0], [0, -1, 0]], [-1, -1], True)
    # lin_prog = LinearProgram([[2, 1, 1, 5], [1, 1, 2, 5], [1, 2, 1, 5], [-1, 0, 0, 0], [0, -1, 0, 0], [0, 0, -1, 0]],[-1, -1, -1],True)
    frame = ResultsFrame(root)

    ps = MaxUpperBoundSelector()
    BranchAndBoundSolver(lin_prog, frame.interior, ps, True).solve()

    frame.pack(fill=tk.BOTH, expand=1)
    root.geometry("800x800")
    root.mainloop()
