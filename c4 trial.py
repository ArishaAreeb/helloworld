#LAST UPDATED APRIL 29
#HORAZONTAL VERTICAL FUNCTIONING

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
    for r in range(rowNum - 1, -1, -1):
        if grid[r][tarCol] not in 'XO':
            grid[r][tarCol] = token
            break
    return r


def winner(grid, row, cols):  # Define functions winner
    # horizontal winning possibilities
    startToken = grid[row][cols]

    count = 0
    numcol = len(grid[0])
    leftLimit = max(cols - 3, 0)
    rightLimit = min(cols + 3, numcol - 1)

    # left side
    for currentCol in range(cols - 1, leftLimit - 1, -1):
        currentToken = grid[row][currentCol]
        if not startToken == currentToken:
            break
        else:
            count = count + 1

    # right side
    for currentCol in range(cols + 1, rightLimit + 1):
        currentToken = grid[row][currentCol]
        if not startToken == currentToken:
            break
        else:
            count = count + 1

    if count >= 3:
        return str(startToken)
    else:
        count = 0

    numrows = len(grid)
    upLimit = max(row - 3, 0)
    downLimit = min(row + 3, numrows - 1)
    for currentrow in range(row - 1, upLimit - 1, -1):
        currentToken = grid[currentrow][cols]
        if startToken == currentToken:
            count = count + 1
        else:
            break
    for currentrow in range(row + 1, downLimit + 1):
        currentToken = grid[currentrow][cols]
        if not startToken == currentToken:
            break
        else:
            count = count + 1

    if count >= 3:
        return str(startToken)
    else:
        count = 0

    # diagonal winning possibilities
    currentrow = row - 1
    currentCol = cols - 1
    #Left Diagonal
    while currentrow >= upLimit and currentCol >= leftLimit:
        currentToken = grid[currentrow][currentCol]
        if startToken == currentToken:
            count = count + 1
            currentrow = currentrow - 1
            currentCol = currentCol - 1
        else :
            break
    if count == 3:
        return str(startToken)

    currentrow = row + 1
    currentCol = cols + 1


    rowLimit = min(row + 3, numrows - 1)
    colLimit = min(cols +3, numcol - 1)
    while currentrow <= rowLimit and currentCol <= colLimit:
        currentToken = grid[currentrow][currentCol]
        if startToken == currentToken:
            count = count + 1
            currentrow = currentrow + 1
            currentCol = currentCol + 1
        else :
            break
    if count == 3:
        return str(startToken)
    else:
        count = 0

    # Right diagonal
    '''
    while currentrow >= upLimit and currentCol >= leftLimit:
        currentToken = grid[currentrow][currentCol]
        if startToken == currentToken:
            count = count + 1
            currentrow = currentrow - 1
            currentCol = currentCol - 1
        else:
            break
    if count == 3:
        return str(startToken)'''
#Bottom
    currentrow = row + 1
    currentCol = cols - 1

    rowLimit = min(row + 3, numrows - 1)
    colLimit = min(cols - 3, 0)

    while currentrow <= rowLimit and currentCol >= colLimit:
        currentToken = grid[currentrow][currentCol]
        if startToken == currentToken:
            count = count + 1
            currentrow = currentrow + 1
            currentCol = currentCol - 1
        else:
            break
    if count == 3:
        return str(startToken)
    else:
        count = 0

    return 'continue'


nameX = input('Player X, enter your name:')
nameO = input('Player O, enter your name:')
grid = genGrid(6, 7, '.')
print('             ')
print('0 1 2 3 4 5 6')
printGrid(grid)

for user in range(0, 41):
    if user % 2 == 0:
        token = 'X'
        name = nameX
    else:
        token = 'O'
        name = nameO

    print('             ')
    tarCol = input(name + ''', you're ''' + token + '''. What column do you want to play in?''')
    while tarCol not in '0123456':
        tarCol = input('Sorry, ' + str(name) + '. That is an invalid colum. Please input a column between 0-6.')
    tarCol = int(tarCol)
    print('             ')
    row = dropToken(grid, token, tarCol)
    print('0 1 2 3 4 5 6')
    printGrid(grid)
    status = winner(grid, row, tarCol)
    if status in 'XO':
        print('Congratulations, ' + str(name) + ', you won!')
        break
    if token == 42:
        print('Congratulations, ' + str(name) + ', you won!')
        break
#COMPLETED!