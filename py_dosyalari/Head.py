import jobs

board = jobs.board

def SpaceIsFree(position):
    if(board[position] == " "):
        return True
    else:
        return False

def printBoard(board):
    print(board[1] + "|" + board[2] + "|" + board[3])
    print("-+-+-")
    print(board[4] + "|" + board[5] + "|" + board[6])
    print("-+-+-")
    print(board[7] + "|" + board[8] + "|" + board[9])
    print("\n")

def InsertLetter(letter, position):
    if SpaceIsFree(position):
        board[position] = letter
        printBoard(board);

        if(checkForWin()):
            if(letter == "o"):
                print("Player Won")
                jobs.ısFinished = True
                exit()
            else:
                print("Comp Won")
                jobs.ısFinished = True
                exit()

        if (checkForDraw()):
            print("Draw")
            jobs.ısFinished = True
            exit()

        return
    else:
        position = int(input("This position is full, try another position"))
        InsertLetter(letter, position)
        return


def checkForWin():
    if (board[1] == board[2] and board[1] == board[3] and board[1] != ' '):
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] != ' '):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] != ' '):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] != ' '):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] != ' '):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] != ' '):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] != ' '):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] != ' '):
        return True
    else:
        return False


def checkForDraw():
    for key in board.keys():
        if(board[key] == " "):
            return False
    return True