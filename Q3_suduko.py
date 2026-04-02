grid = [
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9]
]

def print_grid(g):
    for i in range(9):
        for j in range(9):
            print(g[i][j], end=" ")
        print()

def find_unassigned(g):
    for i in range(9):
        for j in range(9):
            if g[i][j] == 0:
                return i, j
    return None

def used_in_row(g, row, num):
    for j in range(9):
        if g[row][j] == num:
            return True
    return False

def used_in_col(g, col, num):
    for i in range(9):
        if g[i][col] == num:
            return True
    return False

def used_in_box(g, box_row, box_col, num):
    for i in range(3):
        for j in range(3):
            if g[i + box_row][j + box_col] == num:
                return True
    return False

def is_safe(g, row, col, num):
    return (not used_in_row(g, row, num) and
            not used_in_col(g, col, num) and
            not used_in_box(g, row - row % 3, col - col % 3, num))

def solve_sudoku(g):
    pos = find_unassigned(g)
    if not pos:
        return True
    row, col = pos
    for num in range(1, 10):
        if is_safe(g, row, col, num):
            g[row][col] = num
            if solve_sudoku(g):
                return True
            g[row][col] = 0
    return False

print("Input Sudoku:\n")
print_grid(grid)

if solve_sudoku(grid):
    print("\nSolved Sudoku:\n")
    print_grid(grid)
else:
    print("No solution exists")
