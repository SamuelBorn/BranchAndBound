import tkinter as tk

SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")


class ConstraintsInputFrame(tk.Frame):
    def __init__(self, parent, controller, num_vars, num_constraints, integer_points):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.introduction = tk.Label(self, text="Eingabe der Zielfunktion und NB", font=controller.title_font)
        self.introduction.grid(row=0, column=0, pady=10, padx=10, columnspan=1000)

        # place the target function line
        self.min_max = tk.StringVar()
        self.min_max_option_menu = tk.OptionMenu(self, self.min_max, *["min", "max"])
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
                constraint_entry.grid(row=row + 2, column=2 * column+1)
                self.constraint_entries[row].append(constraint_entry)

                text = f"x{column}".translate(SUB) if column == num_vars - 1 else f"x{column} + ".translate(SUB)
                constraint_label = tk.Label(self, text=text)
                constraint_label.grid(row=row + 2, column=2 * column + 2)

            comparative_operator = tk.StringVar()
            comparative_operator_option_menu = tk.OptionMenu(self, comparative_operator, *["<=", ">=", "="])
            comparative_operator_option_menu.grid(row=row + 2, column=2 * num_vars+1)
            self.comparative_operators.append(comparative_operator)

            constraint_entry = tk.Entry(self, width=4)
            constraint_entry.grid(row=row + 2, column=2 * num_vars + 2)
            self.constraint_entries[row].append(constraint_entry)
