def printGrid(rows,cols,grid):
    for row in range(0, rows):
        for col in range(0, cols):
            print(grid[row][col], end=' ')
        print()
rows = 6
cols = 7

printGrid(rows, cols, grid)
