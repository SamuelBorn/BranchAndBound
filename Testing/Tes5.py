from scipy.optimize import linprog

from LinearProgram import LinearProgram

if __name__ == '__main__':
    lin_prog = LinearProgram([[2, 1, 5], [1, 2, 5], [-1, 0, 0], [0, -1, 0]], [-1, -1], True)
    res = linprog(c=lin_prog.minimize_function, A_ub=lin_prog.get_constraints_matrix(),
                  b_ub=lin_prog.get_constraint_vector())
    print(list(res.x), res.fun)
