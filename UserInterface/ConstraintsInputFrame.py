import tkinter as tk
from tkinter import ttk

from Utils import Utils2D
from UserInterface import InputConverter
from UserInterface.ResultsFrame import ResultsFrame
from Utils.BranchAndBoundSolver import BranchAndBoundSolver

SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")


class ConstraintsInputFrame(tk.Frame):
    def __init__(self, root, num_vars, num_constraints, integer_points, selection_rule):
        tk.Frame.__init__(self, root)

        self.integer_points = integer_points
        self.selection_rule = selection_rule

        self.root = root

        self.introduction = tk.Label(self, text="Eingabe der Zielfunktion und NB",
                                     font='Helvetica 18 bold')  # , font=controller.title_font)
        self.introduction.grid(row=0, column=0, pady=10, padx=10, columnspan=1000)

        # place the target function line
        self.min_max = tk.StringVar()
        self.min_max_option_menu = ttk.OptionMenu(self, self.min_max, "max", *["min", "max"])
        self.min_max_option_menu.grid(row=1, column=0)
        self.target_function_entries = []
        for i in range(1, num_vars + 1):
            target_function_entry = tk.Entry(self, width=4)
            target_function_entry.grid(row=1, column=2 * i - 1)
            self.target_function_entries.append(target_function_entry)
            text = f"x{i}".translate(SUB) if i == num_vars else f"x{i} + ".translate(SUB)
            target_function_label = tk.Label(self, text=text)
            target_function_label.grid(row=1, column=2 * i)

        # place all constraints in a grid
        self.constraint_entries = [[] for _ in range(num_constraints)]
        self.comparative_operators = []
        for row in range(0, num_constraints):
            for column in range(0, num_vars):
                constraint_entry = tk.Entry(self, width=4)
                constraint_entry.grid(row=row + 2, column=2 * column + 1, pady=3)
                self.constraint_entries[row].append(constraint_entry)

                text = f"x{column+1}".translate(SUB) if column == num_vars - 1 else f"x{column+1} + ".translate(SUB)
                constraint_label = tk.Label(self, text=text)
                constraint_label.grid(row=row + 2, column=2 * column + 2)

            comparative_operator = tk.StringVar()
            comparative_operator_option_menu = ttk.OptionMenu(self, comparative_operator, "<=", *["<=", ">=", "="])
            comparative_operator_option_menu.grid(row=row + 2, column=2 * num_vars + 1)
            self.comparative_operators.append(comparative_operator)

            constraint_entry = tk.Entry(self, width=4)
            constraint_entry.grid(row=row + 2, column=2 * num_vars + 2)
            self.constraint_entries[row].append(constraint_entry)

        self.button = tk.Button(self, text="Nächster Schritt", command=self.next_step, bg="#659666")
        self.button.grid(row=2 * num_vars + 3, column=0, pady=10, padx=10)

    def next_step(self):
        try:
            lin_prog = InputConverter.convert(self.min_max,
                                              self.target_function_entries,
                                              self.constraint_entries,
                                              self.comparative_operators)
        except Exception as e:
            error_label = tk.Label(self, text=f"Fehler beim einlesen: {e}", fg="red")
            error_label.grid(row=5, column=0, padx=10, pady=10)
            return

        y = tk.Tk()
        y.geometry("800x800")
        x = ResultsFrame(y)

        BranchAndBoundSolver(lin_prog, x.interior, self.selection_rule, self.integer_points).solve()
        x.pack(fill=tk.BOTH, expand=1)

        self.root.destroy()
        y.mainloop()
