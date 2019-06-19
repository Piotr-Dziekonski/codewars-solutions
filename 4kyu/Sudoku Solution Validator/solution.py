def validSolution(board):
    x = 0
    row = board[0]
    print(board)
    if sum(row) != 45: return False
    for elem in row:
        x = elem
        i = row.index(elem)
        for y in range(1,9):
            x += board[y][i]
        if x != 45: return False
    for i in range(0,7,3):
        for j in range(0,7,3):
            x = sum([board[i][j], board[i][j+1], board[i][j+2], board[i+1][j], board[i+1][j+1], board[i+1][j+2], board[i+2][j], board[i+2][j+1], board[i+2][j+2]])
            if x != 45: return False   
    return True