from Utils import Utils2D

import scipy.optimize


class LinearProgram:

    # Functions are stored as
    # min cTx
    # with respect to mx<=b where constraints = (m|b)
    def __init__(self, constraints, minimize_function, was_maximize):
        self.constraints = constraints
        self.minimize_function = minimize_function
        self.was_maximize = was_maximize  # max cTx is stored as -min -cTx. This stores the - at the front

    def __str__(self):
        ret = f"min: {self.minimize_function}\n\n"
        for x in self.constraints:
            ret += f"{x}\n"
        return ret

    def solve(self):
        if len(self.minimize_function) == 2:
            return Utils2D.solve_linprog_2d(self.minimize_function, self.constraints)
        else:
            res = scipy.optimize.linprog(c=self.minimize_function, A_ub=self.get_constraints_matrix(),
                                         b_ub=self.get_constraint_vector())
            return list(res.x), res.fun

    def get_constraints_matrix(self):
        ret = []
        for constraint in self.constraints:
            ret.append(constraint[:-1])
        return ret

    def get_constraint_vector(self):
        ret = []
        for constraint in self.constraints:
            ret.append(constraint[-1])
        return ret
