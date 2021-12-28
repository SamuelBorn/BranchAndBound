from LinearProgram import LinearProgram


# converts the UserInterface Table into machine interpretable lines
def convert(min_max_var, target_function_entries, nested_constraint_entries, comparative_operators):
    constraints = []
    for comparative_operator, constraint_entries in zip(comparative_operators, nested_constraint_entries):
        if comparative_operator.get() == "<=":
            constraints.append([float(constraint_entry.get()) for constraint_entry in constraint_entries])
        elif comparative_operator.get() == ">=":
            constraints.append([-1 * float(constraint_entry.get()) for constraint_entry in constraint_entries])
        elif comparative_operator.get() == "=":
            constraints.append([float(constraint_entry.get()) for constraint_entry in constraint_entries])
            constraints.append([-1 * float(constraint_entry.get()) for constraint_entry in constraint_entries])
        else:
            raise Exception("Did not select comparative operator")

    for i in range(len(target_function_entries)):
        x = [0 for _ in range(len(target_function_entries) + 1)]
        x[i] = -1
        constraints.append(x)

    target_function = []
    if min_max_var.get() == "min":
        for target_entry in target_function_entries:
            target_function.append(float(target_entry.get()))
    elif min_max_var.get() == "max":
        for target_entry in target_function_entries:
            target_function.append(-1 * float(target_entry.get()))  # max cTx is stored as -min -cTx.
    else:
        raise Exception("Did not select min max var")

    return LinearProgram(constraints, target_function, min_max_var.get() == "max")
