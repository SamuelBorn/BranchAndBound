import tkinter as tk

from LinearProgram import LinearProgram

SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")


def draw_equations(lin_prog: LinearProgram, frame: tk.Frame):
    equations = get_target_function(lin_prog)
    equations += get_constraints(lin_prog)

    lab = tk.Label(frame, text=equations)
    lab.pack()


def get_target_function(lin_prog):
    ret = ""
    if lin_prog.was_maximize:
        ret += "max "
        for idx, parameter in enumerate(lin_prog.minimize_function[:-1]):
            ret += f"{-1 * parameter}"
            ret += f"x{idx} + ".translate(SUB)
        ret += f"{-1 * lin_prog.minimize_function[-1]}"
        ret += f"x{len(lin_prog.minimize_function)-1}".translate(SUB)
    else:
        ret += "min "
        for idx, parameter in enumerate(lin_prog.minimize_function[:-1]):
            ret += f"{parameter}"
            ret += f"x{idx} + ".translate(SUB)
        ret += f"{lin_prog.minimize_function[-1]}"
        ret += f"x{len(lin_prog.minimize_function) - 1}".translate(SUB)
    ret += "\n"
    return ret


def get_constraints(lin_prog: LinearProgram):
    ret = ""
    for constraint in lin_prog.constraints:
        for idx, parameter in enumerate(constraint[:-2]):
            ret += f"{parameter}"
            ret += f"x{idx} + ".translate(SUB)
        ret += f"{constraint[-2]}"
        ret += f"x{len(constraint) - 2}".translate(SUB)
        ret += " <= "
        ret += f"{constraint[-1]}"
        ret += "\n"
    return ret
