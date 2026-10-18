# You're given a building represented by a rectangular grid.
# Each cell contains one of three characters:
# - "S" — Your starting position.
# - "." — An open room that you can enter.
# - "#" — A wall that you cannot enter.
# You can move up, down, left, or right, but not diagonally.
# An exit is any open room "." located on the outer boundary of the grid. The starting position does not count as an exit.
# Your task is to return the minimum number of moves required to reach an exit, or -1 if no exit is reachable.

# How can you determine whether a particular cell is an exit?
# What information do you need to track as you move through the building?
# How would you ensure that the exit you find is the closest one rather than just any exit?


from collections import deque


def minimum_exit_moves(grid):
    rows = len(grid)
    cols = len(grid[0])

    # Find the starting position
    for r in range(rows):
        if "S" in grid[r]:
            start_row = r
            start_col = grid[r].index("S")
            break

    # Initialize BFS
    queue = deque([(start_row, start_col, 0)])
    visited = {(start_row, start_col)}

    directions = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]

    while queue:
        row, col, moves = queue.popleft()

        for dr, dc in directions:
            new_row = row + dr
            new_col = col + dc

            # Skip positions outside the grid
            if not (0 <= new_row < rows and 0 <= new_col < cols):
                continue

            # Skip walls
            if grid[new_row][new_col] == "#":
                continue

            # Skip visited positions
            if (new_row, new_col) in visited:
                continue

            # Check whether this location is an exit
            if (
                new_row == 0
                or new_row == rows - 1
                or new_col == 0
                or new_col == cols - 1
            ):
                return moves + 1

            # Save this position for later exploration
            visited.add((new_row, new_col))
            queue.append((new_row, new_col, moves + 1))

    return -1


# Test 1: Reachable exit
grid1 = [
    ["#", "#", "#", "#", "#", "#"],
    ["#", "S", ".", ".", ".", "#"],
    ["#", "#", "#", ".", ".", "#"],
    ["#", ".", ".", ".", ".", "#"],
    ["#", "#", ".", "#", "#", "#"]
]
print(minimum_exit_moves(grid1))  # Expected: 6


# Test 2: No reachable exit
grid2 = [
    ["#", "#", "#"],
    ["#", "S", "#"],
    ["#", "#", "#"]
]
print(minimum_exit_moves(grid2))  # Expected: -1


# Test 3: Exit one move away
grid3 = [
    ["#", ".", "#"],
    ["#", "S", "#"],
    ["#", "#", "#"]
]
print(minimum_exit_moves(grid3))  # Expected: 1


# Test 4: Start on boundary (does not count as exit)
grid4 = [
    ["S", ".", "#"],
    ["#", ".", "#"],
    ["#", "#", "#"]
]
print(minimum_exit_moves(grid4))  # Expected: 1
