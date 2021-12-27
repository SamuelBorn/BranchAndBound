import tkinter as tk

from UserInterface.ConstraintsInputFrame import ConstraintsInputFrame
from UserInterface.ResultsFrame import ResultsFrame


class KeyDataFrame(tk.Frame):
    def __init__(self, root):
        tk.Frame.__init__(self, root)
        self.root = root

        self.introduction = tk.Label(self, text="Eingabe der Eckdaten", font='Helvetica 18 bold')  # , font=controller.title_font)
        self.introduction.grid(row=0, column=0, pady=10, padx=10)

        self.var_count_label = tk.Label(self, text="Anzahl der Variablen:")
        self.var_count_label.grid(row=1, column=0, pady=10, padx=10)
        self.var_count_entry = tk.Entry(self)
        self.var_count_entry.grid(row=1, column=1)
        self.var_count_entry.insert(tk.END, "1")

        self.constraints_count_label = tk.Label(self, text="Anzahl der Nebenbedinungen.")
        self.constraints_count_label.grid(row=2, column=0, pady=10, padx=10)
        self.constraints_count_entry = tk.Entry(self)
        self.constraints_count_entry.grid(row=2, column=1)
        self.constraints_count_entry.insert(tk.END, "1")

        self.show_integer_points = tk.BooleanVar()
        self.show_integer_points.set(True)
        self.show_integer_points_label = tk.Label(self, text="Sollen ganzzahlige Punkte angezigt werden? ")
        self.show_integer_points_label.grid(row=3, column=0, pady=10, padx=10)
        self.show_integer_points_check_box = tk.Checkbutton(self, var=self.show_integer_points)
        self.show_integer_points_check_box.grid(row=3, column=1)

        self.button = tk.Button(self, text="Nächster Schritt", command=self.next_step, bg="#659666")
        self.button.grid(row=4, column=0, pady=10, padx=10)

    def next_step(self):
        try:
            var_count = int(self.var_count_entry.get())
            constraint_count = int(self.constraints_count_entry.get())
        except ValueError:
            error_label = tk.Label(self, text="Bitte Zahlen angeben.", fg="red")
            error_label.grid(row=5, column=0, padx=10, pady=10)
            return

        y = tk.Tk()
        ResultsFrame(y)
        self.root.destroy()
        y.mainloop()
