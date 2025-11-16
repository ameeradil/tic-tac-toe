# function to display the board where you play
def display(board):

    print(board[1]+' | '+board[2]+' | '+board[3])
    print(board[4]+' | '+board[5]+' | '+board[6])
    print(board[7]+' | '+board[8]+' | '+board[9])


# function to ask player1 to choose X or O
def marker():
    player1=''
    player2=''

    while player1 not in ['X','O']:
        player1 = input("player1 choose X or O only")

    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'

    return (player1,player2)


# function to check wether the game is win or tie
def check_status(marker, board):
    if board[1] == board[2] == board[3] == marker or \
       board[4] == board[5] == board[6] == marker or \
       board[7] == board[8] == board[9] == marker or \
       board[1] == board[4] == board[7] == marker or \
       board[2] == board[5] == board[8] == marker or \
       board[3] == board[6] == board[9] == marker or \
       board[1] == board[5] == board[9] == marker or \
       board[3] == board[5] == board[7] == marker:
        print(f'{marker} you won the game congrats')
        return True
        #return True if some one won we can stop the game##################################################################
    
    return False



# function to ask player1 to choose a position, check if won, ask player2 to play
def player1_turn(player1, board):
    position = input('Player1 choose where you want to play: ')
    position = int(position)

    board[position] = player1

    display(board)
    check_status(player1, board)

    # return True/False instead of board##################################################################
    return check_status(player1, board) 


# function to ask player1 to choose a position, check if won, ask player2 to play
def player2_turn(player2, board):
    position = int(input('Player2 choose where you want to play: '))
    board[position] = player2

    display(board)
    check_status(player2, board)

    return check_status(player2, board)


# function to ask for replay or not

# Logic and fuctions order
board = [' ']*10

display(board)

(player1,player2) = marker()

# the game actual while loop ###############################################################3
while True:
    
    # Player1 turn
    if player1_turn(player1, board):
        break  # stop game if won

       # Player2 turn
    if player2_turn(player2, board):
        break  # stop game if won