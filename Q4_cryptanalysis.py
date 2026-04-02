letters = ['S','E','N','D','M','O','R','Y']

domains = {l: list(range(10)) for l in letters}

assignment = {}

def all_different():
    values = list(assignment.values())
    return len(values) == len(set(values))

def leading_non_zero():
    if 'S' in assignment and assignment['S'] == 0:
        return False
    if 'M' in assignment and assignment['M'] == 0:
        return False
    return True

def partial_sum_valid():
    if all(k in assignment for k in ['D','E','Y']):
        if (assignment['D'] + assignment['E']) % 10 != assignment['Y']:
            return False

    if all(k in assignment for k in ['N','R','E']):
        if (assignment['N'] + assignment['R']) % 10 != assignment['E']:
            return False

    if all(k in assignment for k in ['E','O','N']):
        if (assignment['E'] + assignment['O']) % 10 != assignment['N']:
            return False

    if all(k in assignment for k in ['S','M','O']):
        if (assignment['S'] + assignment['M']) % 10 != assignment['O']:
            return False

    return True

def full_equation_valid():
    if len(assignment) != 8:
        return True

    S = assignment['S']
    E = assignment['E']
    N = assignment['N']
    D = assignment['D']
    M = assignment['M']
    O = assignment['O']
    R = assignment['R']
    Y = assignment['Y']

    send = 1000*S + 100*E + 10*N + D
    more = 1000*M + 100*O + 10*R + E
    money = 10000*M + 1000*O + 100*N + 10*E + Y

    return send + more == money

def is_consistent():
    return all_different() and leading_non_zero() and partial_sum_valid() and full_equation_valid()

def select_unassigned_variable():
    for l in letters:
        if l not in assignment:
            return l
    return None

def backtrack():
    if len(assignment) == len(letters):
        if full_equation_valid():
            return True
        return False

    var = select_unassigned_variable()

    for value in domains[var]:
        if value not in assignment.values():
            assignment[var] = value

            if is_consistent():
                if backtrack():
                    return True

            del assignment[var]

    return False

result = backtrack()

if result:
    print("Solution Found:\n")
    for k in sorted(assignment):
        print(k, "=", assignment[k])

    S = assignment['S']
    E = assignment['E']
    N = assignment['N']
    D = assignment['D']
    M = assignment['M']
    O = assignment['O']
    R = assignment['R']
    Y = assignment['Y']

    send = 1000*S + 100*E + 10*N + D
    more = 1000*M + 100*O + 10*R + E
    money = 10000*M + 1000*O + 100*N + 10*E + Y

    print("\nVerification:")
    print(send, "+", more, "=", money)

else:
    print("No solution exists")
