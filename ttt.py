import os

def printBoard(b):
    for l in b:
        print(l, '\n')


# n should be from 1 to 9, indicating the position of board
def move(b, n, p):
    if n > 9 or n < 1:
        print("Invalid selection. Please select a number from 1 to 9.")
        return -1
    elif not str(n).isnumeric() or n > 9 or n < 1:
        print("Invalid selection. Please select a number from 1 to 9.")
        return -1
    n -= 1
    l = n // 3
    n = n % 3
    if b[l][n] != '-':
        print('Position already taken, please re-select.')
        return -1
    else:
        if p == 1:
            b[l][n] = 'o'
        else:
            b[l][n] = 'x'
        return checkWin(b, l, n)

def checkVertWin(b, n):
    temp = b[0][n]
    for l in b:
        if l[n] != temp:
            return False
    return True

def checkHoriWin(b, l):
    temp = b[l][0]
    for c in b[l]:
        if c != temp:
            return False
    return True

def checkDiaWin(b):
    return checkDia1(b) or checkDia2(b)

def checkDia1(b):
    temp = b[0][0]
    if temp != '-':
        return temp == b[1][1] and temp == b[2][2]
    return False

def checkDia2(b):
    temp = b[1][1]
    if temp != '-':
        return temp == b[2][0] and temp == b[0][2]
    return False

def checkWin(b, l, n):
    return checkDiaWin(b) or checkHoriWin(b, l) or checkVertWin(b, n)

def play():
    board = []

    for i in range(3):
        temp = []
        for j in range(3):
            temp.append('-')
        board.append(temp)
        del temp
    p = True
    while 1:
        os.system('clear')
        printBoard(board)
        if p:
            print("Player 1, please make a move")
            pos = int(input())
            res = move(board, pos, 1)
            if res:
                printBoard(board)
                print('Congrats, Player 1 wins.')
                break
            else:
                if res == -1:
                    continue
                else:
                    p = not p
                    continue
        else:
            print("Player 2, please make a move")
            pos = int(input())
            res = move(board, pos, 2)
            if res:
                printBoard(board)
                print('Congrats, Player 2 wins.')
                break
            else:
                if res == -1:
                    continue
                else:
                    p = not p
                    continue
    return

play()
    