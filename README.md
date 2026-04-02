### AI Assignment 4 – CSP Problems

This project demonstrates solving different problems using Constraint Satisfaction Problem (CSP) techniques with backtracking.

### 1. Map Coloring (Australia)

The map coloring problem assigns colors (Red, Green, Blue) to regions of Australia (WA, NT, Q, SA, NSW, V, T) such that no adjacent regions share the same color. It is modeled as a CSP with regions as variables, colors as domains, and adjacency as constraints. The solution uses backtracking to ensure valid assignments.

### 2. Map Coloring (Telangana)

This extends the CSP approach to the 33 districts of Telangana. Each district is assigned a color (Red, Green, Blue, Yellow) while ensuring neighboring districts have different colors. The solution uses adjacency lists and backtracking to find a valid coloring.

### 3. Sudoku Solver

This project solves a 9×9 Sudoku puzzle using CSP. Each cell is treated as a variable with values from 1–9. Constraints ensure no repetition in rows, columns, and 3×3 subgrids. Backtracking is used to fill the grid and guarantee a correct solution.

### 4. Crypt-Arithmetic Puzzle

This solves the puzzle SEND + MORE = MONEY using CSP. Each letter is assigned a unique digit (0–9) with constraints like no repetition and non-zero leading digits. Backtracking ensures the arithmetic equation is satisfied.

### Key Features
Uses CSP with backtracking
Applies constraints effectively
Simple and modular implementation
Works for multiple AI problems

### Limitations
Uses basic backtracking only
No advanced techniques like MRV or AC-3
May be slow for complex cases

### Applications
Map coloring
Puzzle solving
Scheduling and resource allocation
AI problem solving

### Conclusion
This project shows how CSP and backtracking can efficiently solve real-world and logical problems while satisfying all constraints.
