board = [0] * 10
board = [board] * 22
for row in board:
    print row

board[1][2] = 2
print 'board[1][2] = 2'

for row in board:
    print row