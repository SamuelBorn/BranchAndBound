import tkinter as tk

from LinearProgram import LinearProgram

SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")


def draw_equations(lin_prog: LinearProgram, frame: tk.Frame):
    equations = get_target_function(lin_prog)
    equations += get_constraints(lin_prog)

    x = lin_prog.solve()
    print(x)
    if x[0] is not None:
        o = tuple([round(y, 2) for y in x[0]])
        equations += f"\nOptimaler relaxierter Punkt: {o}\n"
        equations += f"Optimaler relaxierter Wert: {round(x[1], 2)}"
    else:
        equations += "\n Die Lösungsmenge des relaxierten Problems ist leer."

    lab = tk.Label(frame, text=equations, bg="white")
    lab.pack()


def get_target_function(lin_prog) -> str:
    ret = "\n"
    if lin_prog.was_maximize:
        ret += "max "
        for idx, parameter in enumerate(lin_prog.minimize_function[:-1]):
            ret += f"{-1 * parameter}"
            ret += f"x{idx + 1} + ".translate(SUB)
        ret += f"{-1 * lin_prog.minimize_function[-1]}"
        ret += f"x{len(lin_prog.minimize_function)}".translate(SUB)
    else:
        ret += "min "
        for idx, parameter in enumerate(lin_prog.minimize_function[:-1]):
            ret += f"{parameter}"
            ret += f"x{idx + 1} + ".translate(SUB)
        ret += f"{lin_prog.minimize_function[-1]}"
        ret += f"x{len(lin_prog.minimize_function)}".translate(SUB)
    ret += "\n"
    return ret


def get_constraints(lin_prog: LinearProgram) -> str:
    ret = ""
    for constraint in lin_prog.constraints:
        for idx, parameter in enumerate(constraint[:-2]):
            ret += f"{parameter}"
            ret += f"x{idx + 1} + ".translate(SUB)
        ret += f"{constraint[-2]}"
        ret += f"x{len(constraint) - 1}".translate(SUB)
        ret += " <= "
        ret += f"{constraint[-1]}"
        ret += "\n"
    return ret


def draw_int_vec(vec, frame):
    for idx, num in enumerate(vec):
        var_str = f"x{idx + 1}".translate(SUB)
        tk.Label(frame, text=f"{var_str} = {round(num)}", bg="white").pack()
