# UI
# Run this Module to Begin Game

import game_logic

print('Commencing Game')

NONE = game_logic.NONE
BLACK = game_logic.BLACK
WHITE = game_logic.WHITE

def number_of_rows():
    '''Asks user for input and places it in a list called rows '''
    num_row = int(input())
    row_list = []

    if num_row not in [4, 6, 8, 10, 12, 14, 16]:
        print("ERROR")
        
    return num_row

def number_of_columns():
    '''Asks user for input and places it in a list called columns'''
    num_col = int(input())
    col_list = []
    if num_col in ['4', '6', '8', '10', '12', '14', '16']:
        col_list.append(num_col)
    return num_col
        
def first_move():
    '''Asks user for input, will return the assigned color according to the letter entered '''
    first_player = input('')
    if(first_player[0].upper() == 'B'):
        return BLACK
    else:
        return WHITE
            
def position_on_grid():
    '''Asks user for input and Returns color of which disk will be on top-left position'''
    top_left = input('')
    if (top_left[0].upper() == 'B'):
        return BLACK
    else:
        return WHITE

def who_wins():
    '''Asks user for input and returns true if greater than wins, returns false otherwise'''
    greater_or_less = input('')
    if greater_or_less[0] == '>': 
        return True
    return False

def current_players_move():
    '''Asks user for input and returns the input with assigned positions '''
    position = input('').split(' ')
    return (int(position[0])-1, int(position[1])-1)

def print_board(othello):
        '''prints board and whose turn it is'''
        othello.count()
        for row in range(othello.rows):
            new_column = []
            for column in range(othello.columns):
                if othello.board[column][row] == NONE:
                    new_column.append('.')
                elif othello.board[column][row] == BLACK:
                    new_column.append('B')
                elif othello.board[column][row] == WHITE:
                    new_column.append('W')
            print (' '.join(new_column))
        if othello.turn == BLACK:
            print('TURN: B')
        else:
            print('TURN: W')

def count_prints(othello):
    '''Counts the number of each color on board and prints it ''' 
    count_black, count_white = othello.count() 
    print ('B:', count_black, 'W:', count_white)

def winner(othello, win):
    '''Returns assigned winner depending on the specified symbol, < greater than or > less than'''
    count_black, count_white = othello.count()
    if othello.win == True:
        if count_black > count_white:
            print('WINNER: BLACK')
        elif count_black < count_white:
           print('WINNER: WHITE')
        elif count_black == count_white:
           print('WINNER: NONE')
    else: 
        if count_black < count_white:
           print('WINNER: BLACK')
        elif count_black > count_white:
           print('WINNER: WHITE')
        elif count_black == count_white:
          print('WINNER: NONE') 

def user_interface():
    '''This is the user interface it will call the functions and format the shell properly '''
    rows = number_of_rows()
    
    columns = number_of_columns()
    
    turn = first_move()
    
    rules = position_on_grid()
    
    win = who_wins()
    
    othello = three_othello_game_logic.othello(rows, columns, turn, rules, win)

    counter = count_prints(othello)
    prints = print_board(othello)
    
    while True:
        move = current_players_move()
        if len(othello.look_to_flip(move[0], move[1])) > 0:
            othello.make_move(move[0], move[1])
            #print(othello.board)
            print('VALID')
            count_prints(othello)
            print_board(othello)
            if othello.is_board_full() == True:
                #print('board is full')
                winner(othello, win)
                break
            if othello.no_more_valid_moves() == True:
                #print('no more valid')
                winner(othello, win)
                break
        else:
            print('INVALID')
        
            
if __name__ == '__main__':
    user_interface()
    

