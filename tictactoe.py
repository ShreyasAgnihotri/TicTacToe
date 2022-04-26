theBoard = {

    1: ' ' ,2: ' ' ,3: ' ',
    4: ' ' ,5: ' ' ,6: ' ',
    7: ' ' ,8: ' ' ,9: ' ',
}

def printBoard(board):
    print(' ' + board[1] + '|' + board[2] + '|' + board[3] + ' ')
    print("------- ")
    print(' ' + board[4] + '|' + board[5] + '|' + board[6] + ' ')
    print("------- ")
    print(' ' + board[7] + '|' + board[8] + '|' + board[9] + ' ')
    print("\n")

printBoard(theBoard)


def freespace(move):
    if(theBoard[move] == ' '):
        return True
    else:
        return False

def checkDraw():
    for key in theBoard.keys():
        if theBoard[key] == ' ':
            return False
    return True

def checkWin():
    if theBoard[7] == theBoard[8] == theBoard[9] != ' ':
        return True     
    elif theBoard[4] == theBoard[5] == theBoard[6] != ' ' :
        return True    
    elif theBoard[1] == theBoard[2] == theBoard[3] != ' ' :
        return True 
    elif theBoard[1] == theBoard[5] == theBoard[9] != ' ' :
        return True    
    elif theBoard[3] == theBoard[5] == theBoard[7] != ' ' :
        return True     
    elif theBoard[1] == theBoard[4] == theBoard[7] != ' ' :
        return True 
    elif theBoard[2] == theBoard[5] == theBoard[8] != ' ' :
        return True 
    elif theBoard[3] == theBoard[6] == theBoard[9] != ' ' :
        return True 
    else:
        return False


def winner(temp):
    if theBoard[7] == theBoard[8] == theBoard[9] == temp:
        return True     
    elif theBoard[4] == theBoard[5] == theBoard[6] == temp :
        return True    
    elif theBoard[1] == theBoard[2] == theBoard[3] == temp :
        return True 

    elif theBoard[1] == theBoard[5] == theBoard[9] == temp :
        return True    

    elif theBoard[3] == theBoard[5] == theBoard[7] == temp :
        return True     

    elif theBoard[1] == theBoard[4] == theBoard[7] == temp :
        return True 
        
    elif theBoard[2] == theBoard[5] == theBoard[8] == temp :
        return True 
    elif theBoard[3] == theBoard[6] == theBoard[9] == temp :
        return True 
    else:
        return False


def playMove(turn,move):
    if freespace(move):
        theBoard[move] = turn
        printBoard(theBoard)
        if checkWin():
            if turn == "X":
                print("Player Wins!")
                exit()
            else:
                print("Bot Wins!")
                exit()
        if checkDraw():
            print("Draw!")
            exit()
    else:
        print("The Place is already filled!\n")
        move = int(input("Enter new move: "))
        playMove(turn,move)
    return move 

player = 'X'
bot = 'O'      
def playerMove():
    move = int(input("PLAYER Move: "))
    playMove(player,move)
    return
def compMove():
    bestScore = -1000
    bestMove = 0
    for key in theBoard.keys():
        if theBoard[key] == ' ':
            theBoard[key] = bot
            score = MiniMax(theBoard,0,False)
            theBoard[key] = ' '
            if score > bestScore:
                bestScore = score
                bestMove = key
    temp = playMove(bot,bestMove)
    return temp

def MiniMax(theBoard,depth,Maxturn):
    if winner(bot):
        return 1
    elif winner(player):
        return -1
    elif checkDraw():
        return 0

    if Maxturn:
        bestScore = -1000
        for key in theBoard.keys():
            if theBoard[key] == ' ':
                theBoard[key] = bot
                score = MiniMax(theBoard,depth+1,False)
                theBoard[key] = ' '
                if score > bestScore:
                    bestScore = score
        return bestScore
    else:
        bestScore = 1000
        for key in theBoard.keys():
            if theBoard[key] == ' ':
                theBoard[key] = player
                score = MiniMax(theBoard,depth+1,True)
                theBoard[key] = ' '
                if score < bestScore:
                    bestScore = score
        return bestScore

while not checkWin():
    playerMove()
    move = compMove()
    print(f"Bot Played at {move}")
    print("\n")
    