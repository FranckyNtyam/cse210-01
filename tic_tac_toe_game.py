"""
FILE NAME: GAME.PY

AUTHOR: Ntyam Adjomo Francky Ludovic

Purpose: Create Tic-Tac-Toe game in which two players seek in alternate turns to complete a row, a column, or a diagonal with either three x's or three o's drawn in the spaces of a grid of nine squares.

"""
# Make a dictionary to keep the board in.
array_number = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'I':9}

def main():
    player = change_player("")
    list_key = list_keys()
    board_display(list_key)
    while not condition_game(list_key):
        move_function(player, list_key)
        player = change_player(player)
        board_display(list_key)
        if check_winner(list_key):
            print(f"{change_player(player)} is the winner")
            break
    print("Good game. Thanks for playing!")

#create a function that help us to get list of dictionary keys

def list_keys():
    list_key = list(array_number.values())
    return list_key

def board_display(list_key):
    
    print(f"{list_key[0]} | {list_key[1]} | {list_key[2]} ")
    print(f"{list_key[3]} | {list_key[4]} | {list_key[5]} ")
    print(f"{list_key[6]} | {list_key[7]} | {list_key[8]} ")

#create a function to check if the board is filled or not with the number between 1 and 9.

def move_function(player, list_key):
    # ask the user to enter a number between 1 and 9
    move = int(input(f"{player}'s turn to choose between 1 and 9: "))
    
    list_key[move - 1] = "\033[34m" + player +  "\033[0m" # Assign the player to the square
    
    # Check if the number is between 1 and 9
    if move in range(1, 10):
        return move
    
    else:
        print("Invalid number")
        move_function(player, list_key) # Call the function again

# create a function to check if the game is over.

def condition_game(list_key):
    for i in range(1, 10):
        if list_key[i - 1] != "x" and list_key[i - 1] != "o":
            return False
        return True  
# Create a function to check if the player has won.

def check_winner(list_key):
    
    return (list_key[0] == list_key[1] == list_key[2] or
            list_key[3] == list_key[4] == list_key[5] or
            list_key[6] == list_key[7] == list_key[8] or
            list_key[0] == list_key[3] == list_key[6] or
            list_key[1] == list_key[4] == list_key[7] or
            list_key[2] == list_key[5] == list_key[8] or
            list_key[0] == list_key[4] == list_key[8] or
            list_key[2] == list_key[4] == list_key[6] )
    
# Create a function to change the player.

def change_player(player):
    if player == "" or player == "o":
        player = "x"
    elif player == "x":
        player = "o"
    return player

if __name__ == "__main__":
    main()

