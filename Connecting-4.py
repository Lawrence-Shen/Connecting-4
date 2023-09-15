#This program is a game of Connect 4, which sees two players taking turns
#placing their tokens of X's or O's on a 6x6 board until either the board is
#full(tie game) or one player wins by making a connection of at least 4 of
#their token vertically, horiizontally, or diagonally

"""
Takes the current game board and prints it. Parameter is the dictionary which
makes up the board. Funtion does not return a value
"""
def displayBoard(board):
    print()
    for i in board:
        print(i, end = "\t")

    print()

    for k in range(len(board[i])):
        for j in board:
            print(board[j][k], end = "\t")
        print()

"""
Asks the user to input the token they would like to use - either "X" or "O". No
parameters. Returns player 1 and player 2's chosen tokens
"""
def playerTokens():
    p1Token = ""
    while p1Token != "X" and p1Token != "O":
        print()
        print("There are two tokens available - 'X' and 'O'")
        p1Token = input("Player 1 - Which token would you like to use? ")

    if p1Token == "X":
        p2Token = "O"
    else:
        p2Token = "X"

    print("Player 2 - You will use token " + p2Token)

    return p1Token, p2Token

"""
Takes the players inputted column and places their token in the next available
row of that column - in case column is full, it will prompt the user to select a different
column. Parameters are the player whose turn it is, their token, and the
board's current dictionary. Returns the new board dictionary, the player's current column
and the player's current row
"""
def playRound(player,playerToken,board):
    print()
    print(player)

    pColumn = ""
    while pColumn != "A" and pColumn != "B" and pColumn != "C" and pColumn != "D" and pColumn != "E" and pColumn != "F":
        pColumn = input("Please enter a valid column selection: ")

        if pColumn == "A" or pColumn == "B" or pColumn == "C" or pColumn == "D" or pColumn == "E" or pColumn == "F":
            if not("*" in board[pColumn]):
                print("That column is full, try again!")
                pColumn = ""
                
    for i in range(5,-1,-1):
        if board[pColumn][i] == "*":
            board[pColumn][i] = playerToken
            break

    return board, pColumn, i

"""
Uses position of last piece placed to determine if the game has been won, or
if it is a tie game if the board is full. Parameters are the player's token, the current board's
dictionary, the column that was just played, and the row that was just played.
Returns True if board is full, or if a player has won, and False if not. Also
returns the list of the connection of the win, 0 if no win, and a tie game
message if the board is full
"""
def checkWin(playerToken,board,pColumn,pRow):
    full = 0

    for i in board:
        if not("*" in board[i]):
            full += 1
    if full == len(board):
        return True, "Board is full! Tie game!"

    #Checks if there is a vertical connection
    vSum = 1
    connection = [pColumn + str(pRow + 1)]
    #Loops through the last column played, starting at the row after the row just played
    for k in range(pRow+1,len(board[pColumn])):
        if board[pColumn][k] == playerToken:
            vSum += 1
            connectElement = pColumn + str(k+1)
            connection.append(connectElement)
        else:
            break
    if vSum >= 4:
        return True, connection
    else:
        gameOver = False

    #Checks if there is a horizontal connection
    hSum = 0
    connection = [""]
    #Loops through every column starting at "A", keeping the same row as the one just played
    for k in range(ord("A"),ord("F")+1):
        if board[chr(k)][pRow] == playerToken:
            hSum += 1
            connectElement = chr(k) + str(pRow + 1)
            connection.append(connectElement)
        else:
            if hSum >= 4:
                break
            #If the current spot being checked doesn't match the player's token
            #and a connection hasn't been found, it continues looping, resetting
            #the connect count
            else:
                hSum = 0
                connection = [""]
    if hSum >= 4:
        connection.remove("")
        return True, connection
    else:
        gameOver = False

    #Checks if there is a downward sloping diagonal connection
    downDSum = 1
    newpRow = pRow-1
    connection = [pColumn + str(pRow+1)]
    #Loops backwards and checks from last column played
    for i in range(ord(pColumn)-1,ord("A")-1,-1):
        if newpRow < 0:
            break
        if board[chr(i)][newpRow] == playerToken:
            downDSum += 1
            connectElement = chr(i) + str(newpRow+1)
            connection.append(connectElement)
        else:
            break
        newpRow = newpRow - 1
    newpRow = pRow
    #Loops fowards and checks from column last played
    for i in range(ord(pColumn)+1,ord("F")+1):        
        newpRow = newpRow + 1
        if newpRow > 5:
            break
        if board[chr(i)][newpRow] == playerToken:
            downDSum += 1
            connectElement = chr(i) + str(newpRow+1)
            connection.append(connectElement)
        else:
            break
    if downDSum >= 4:
        connection.sort()
        return True, connection
    else:
        gameOver = False

    #Checks if there is an upwards sloping diagonal connection
    upDSum = 1
    newpRow = pRow + 1
    connection = [pColumn + str(pRow+1)]
    #Loops backward and checks from last column played
    for i in range(ord(pColumn)-1,ord("A")-1,-1):
        if newpRow > 5:
            break
        if board[chr(i)][newpRow] == playerToken:
            upDSum += 1
            connectElement = chr(i) + str(newpRow+1)
            connection.append(connectElement)
        else:
            break
        newpRow = newpRow + 1
    newpRow = pRow
    #Loops forward and checks from last column played
    for i in range(ord(pColumn)+1,ord("F")+1):
        newpRow = newpRow - 1
        if newpRow < 0:
            break
        if board[chr(i)][newpRow] == playerToken:
            upDSum += 1
            connectElement = chr(i) + str(newpRow+1)
            connection.append(connectElement)
        else:
            break
    if upDSum >= 4:
        connection.sort()
        return True, connection
    else:
        gameOver = False
                
    return gameOver, 0

"""
First prints the board at the start of the game, then gets the player tokens,
then runs the game until either the board is full, or one player wins. It then
prints out a winner/tie game message
"""
def main():
    board = {"A":["*","*","*","*","*","*"],"B":["*","*","*","*","*","*"],"C":["*","*","*","*","*","*"],"D":["*","*","*","*","*","*"],"E":["*","*","*","*","*","*"],"F":["*","*","*","*","*","*"]}
    displayBoard(board)

    p1Token, p2Token = playerTokens()

    gameOver = False
    gameRound = 1
    
    while not(gameOver == True):
        if gameRound % 2 == 0:
            player = "Player 2"
            playerToken = p2Token
        else:
            player = "Player 1"
            playerToken = p1Token
        
        newBoard, pColumn, pRow = playRound(player,playerToken,board)
        displayBoard(newBoard)
        gameOver, connection = checkWin(playerToken,newBoard,pColumn,pRow)

        gameRound += 1

    if type(connection) == list:
        print(player + " is the winner with " + ", ".join(connection) + ". Congratulations!")
    else:
        print(connection)
main()
