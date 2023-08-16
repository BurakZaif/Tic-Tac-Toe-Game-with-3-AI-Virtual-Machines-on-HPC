import jobs

def checkWhichMarkWon(mark, board):
    if (board[1] == board[2] and board[1] == board[3] and board[1] == mark):
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] == mark):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] == mark):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] == mark):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] == mark):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] == mark):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] == mark):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] == mark):
        return True
    else:
        return False


def player2Move(board):
    BestScore = 800
    bestMove = 0

    for key in board.keys():
        if (board[key] == " "):
            board[key] = player
            score = minimax(board, 0, True)
            board[key] = " "
            if (score < BestScore):
                BestScore = score
                bestMove = key

    return FinalMove()


def FinalMove(bestmove):
    final = bestmove
    return final


def checkForDraw(board):
    for key in board.keys():
        if (board[key] == " "):
            return False
    return True


def minimax(board, depth, IsMax):
    if (checkWhichMarkWon(comp, board)):
        return 1
    elif (checkWhichMarkWon(player, board)):
        return -1
    elif (checkForDraw(board)):
        return 0

    if (IsMax):
        BestScore = -800

        for key in board.keys():
            if (board[key] == " "):
                board[key] = comp
                score = minimax(board, 0, False)
                board[key] = " "
                if (score > BestScore):
                    BestScore = score
        return BestScore

    else:
        BestScore = 800

        for key in board.keys():
            if (board[key] == " "):
                board[key] = player
                score = minimax(board, 0, True)
                board[key] = " "
                if (score < BestScore):
                    BestScore = score
        return BestScore


comp = "x"
player = "o"