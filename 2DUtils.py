import itertools


# Solve:
# min cTx
# Ax <= b

# all constraints ax0 + bx1 + ... <= c are stored as tuples (a,b,...,c)

# ax0 + bx1 >= c are rewritten as -ax0 - bx1 <= -c
# ax0 + bx1 = c are rewritten as -ax0 - bx1 <= -c and ax0 + bx1 <= c


def solve_linprog_2d(function, constraints):
    optimal_point = None
    optimal_value = float("inf")
    for intersection in get_valid_intersections(constraints):
        if evaluate(function, intersection) < optimal_value:
            optimal_point = intersection
            optimal_value = evaluate(function, intersection)
    return optimal_point, optimal_value


# evaluates a function ax + by + cz + ... at a point (p1,p2,p3,...)
def evaluate(function, point):
    assert len(function) == len(point)
    result = 0
    for m, x in zip(function, point):
        result += m * x
    return result


def get_valid_intersections(constraints):
    valid_intersections = []
    for intersection in get_all_intersections(constraints):
        if is_valid(intersection, constraints):
            valid_intersections.append(intersection)
    return valid_intersections


def is_valid(intersection, constraints):
    for line in constraints:
        if evaluate(line[:-1], intersection) > line[-1] + 0.0001:
            return False
    return True


# returns all intersections of all 2D constraints
def get_all_intersections(constraints):
    intersections = []
    for constraint_a, constraint_b in get_all_pairs(constraints):
        if not parallel(constraint_a, constraint_b):
            intersections.append(get_intersection(constraint_a, constraint_b))
    return intersections


# returns the intersection of two 2D constraints
def get_intersection(constraint_a, constraint_b):
    assert not parallel(constraint_a, constraint_b)

    a, b, c = constraint_a
    d, e, f = constraint_b

    x, y = None, None
    if b == 0:  # e != 0 or parallel, a != 0 or 0x+0y not a line
        y = (a * f - d * c) / (a * e - d * b)
        x = (c - b * y) / a
    else:
        x = (b * f - e * c) / (b * d - e * a)
        y = (c - a * x) / b
    return x, y


# checks if two 2D constraints are parallel
def parallel(constraint_a, constraint_b):
    a, b, c = constraint_a
    d, e, f = constraint_b
    if a == 0 or d == 0:
        return a == 0 and d == 0
    if b == 0 or e == 0:
        return b == 0 and e == 0
    return abs(a / b - d / e) <= 0.0001


def get_all_pairs(constraints):
    return list(itertools.combinations(constraints, 2))


if __name__ == '__main__':
    fun = (-1, -1)
    cons = [(1, 2, 10), (2, 1, 10), (-1, 0, 0), (0, -1, 0)]
    print("Test 2D Utils:")
    print(f"{get_all_intersections(cons)=}")
    print(f"{get_valid_intersections(cons)=}")
    print(f"{solve_linprog_2d(fun, cons)=}")
