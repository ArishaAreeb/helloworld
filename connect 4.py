# ---->>FUNCTIONS <<----
def printGrid(grid):

    rows = len(grid)

    cols = len(grid[0])

    for row in range(0, rows):
        for col in range(0, cols):
            print(grid[row][col], end=' ')
        print()

def genGrid(row, col, intvalue):
     grid = []
     for i in range(row):
         grid.append([intvalue] * col)
     return grid

def dropToken(grid, token, tarCol):
    rowNum = len(grid)
    for r in range(rowNum-1,-1,-1):
        if grid[r][tarCol] not in 'XO':
            grid[r][tarCol] = token
            break
    return r

def winner (grid,row,cols ):  #Define functions winner
    # finding if horizontal
    startToken = grid[row][cols]
    count = 0
    numcol = len(grid[0])
    leftLimit = max(cols - 3,0)
    rightLimit = min(cols + 3, numcol - 1)

    # left side
    for currentCol in range(cols -1,leftLimit-1, -1):
        currentToken = grid[row][currentCol]
        if not startToken == currentToken:
            break
        else:
            count = count + 1

    # right side
    for currentCol in range(cols + 1, rightLimit +1):
        currentToken = grid[row][currentCol]
        if not startToken == currentToken:
            break
        else:
            count = count + 1
    if count == 3:
        return str(startToken)

    numrows = len(grid)
    upLimit = max(row - 3,0)
    downLimit = min(row + 3, numrows - 1)



   #TOP
    for currentrow in range(row - 1, upLimit - 1, -1):
        currentToken = grid[currentrow][row]
        if not startToken == currentToken:
            break
        else:
            count = count + 1
 # BOTTOM
    for currentrow in range(row + 1, downLimit + 1):
        currentToken = grid[currentrow][row]
        if not startToken == currentToken:
            break
        else:
            count = count + 1
    if count == 3:
        return str(startToken)
    return 'continue'

# Initialization
nameX = input('Player X, enter your name:')
nameO = input('Player O, enter your name:')
grid = genGrid(6,7,'.')
print('             ')
print('0 1 2 3 4 5 6')
printGrid(grid)
for user in range(0,41):
    if user%2 == 0:
        token = 'X'
        print('             ')


        tarCol = int(input(nameX + ''', you're X. What column do you want to play in?'''))
        print('             ')
        row=dropToken(grid, token, tarCol)
        print('0 1 2 3 4 5 6')
        printGrid(grid)
        status = winner(grid, row, tarCol)
        if status in 'XO':
            print('Congratulations, '+ str(nameX)+ ', you won!')
            break

    else:
        token = 'O'
        print('             ')
        tarCol = int(input(nameO + ''', you're O. What column do you want to play in?'''))
        print('             ')
        dropToken(grid, token, tarCol)
        print('0 1 2 3 4 5 6')
        printGrid(grid)
        status = winner(grid, row-1, tarCol)
        if status in 'XO':
            print('Congratulations, '+ str(nameO)+ ', you won!')
            break

