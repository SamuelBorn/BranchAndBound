import itertools


# all lines ax0 + bx1 + ... <= c are stored as tuples (a,b,...,c)

# ax0 + bx1 >= c are rewritten as -ax0 - bx1 <= -c
# ax0 + bx1 = c are rewritten as -ax0 - bx1 <= -c and ax0 + bx1 <= c


def solve_linprog_2d(function, lines):
    optimal_point = None
    optimal_value = float("inf")
    for intersection in get_all_intersections(lines):
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


# returns all intersections of all 2D lines
def get_all_intersections(lines):
    intersections = []
    for line_a, line_b in get_all_pairs(lines):
        if not parallel(line_a, line_b):
            intersections.append(get_intersection(line_a, line_b))
    return intersections


# returns the intersection of two 2D lines
def get_intersection(line_a, line_b):
    assert not parallel(line_a, line_b)

    a, b, c = line_a
    d, e, f = line_b

    x, y = None, None
    if b == 0:  # e != 0 or parallel, a != 0 or 0x+0y not a line
        y = (a * f - d * c) / (a * e - d * b)
        x = (c - b * y) / a
    else:
        x = (b * f - e * c) / (b * d - e * a)
        y = (c - a * x) / b
    return x, y


# checks if two 2D lines are parallel
def parallel(line_a, line_b):
    a, b, c = line_a
    d, e, f = line_b
    if a == 0 or d == 0:
        return a == 0 and d == 0
    if b == 0 or e == 0:
        return b == 0 and e == 0
    return abs(a / b - d / e) <= 0.00001


def get_all_pairs(lines):
    return list(itertools.combinations(lines, 2))


if __name__ == '__main__':
    get_intersection((4, 2, 6), (3, 9, 1))
    # plt.plot(x,x*m1+b1)
