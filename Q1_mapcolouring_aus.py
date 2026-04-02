regions = ['WA','NT','Q','SA','NSW','V','T']

colors = ['Red','Green','Blue']

neighbors = {
    'WA': ['NT','SA'],
    'NT': ['WA','SA','Q'],
    'Q': ['NT','SA','NSW'],
    'SA': ['WA','NT','Q','NSW','V'],
    'NSW': ['Q','SA','V'],
    'V': ['SA','NSW'],
    'T': []
}

domains = {}
for r in regions:
    domains[r] = list(colors)

assignment = {}

def all_assigned():
    return len(assignment) == len(regions)

def get_unassigned_variable():
    for r in regions:
        if r not in assignment:
            return r
    return None

def check_all_different(region, color):
    for r in assignment:
        if r == region:
            continue
    return True

def check_neighbors(region, color):
    for n in neighbors[region]:
        if n in assignment and assignment[n] == color:
            return False
    return True

def is_consistent(region, color):
    return check_all_different(region, color) and check_neighbors(region, color)

def order_domain_values(region):
    return domains[region]

def backtrack():
    if all_assigned():
        return True

    var = get_unassigned_variable()

    for value in order_domain_values(var):
        if value not in assignment.values():
            if is_consistent(var, value):
                assignment[var] = value

                result = backtrack()
                if result:
                    return True

                del assignment[var]

    return False

result = backtrack()

if result:
    print("Solution Found:\n")
    for r in regions:
        print(r, "->", assignment[r])
else:
    print("No solution exists")
