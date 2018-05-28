# OTHELLO GAME LOGIC

import collections

NONE = 0
BLACK = 1
WHITE = 2

class othello:
    def __init__(self, rows, columns, turn, rules, win):
        '''Assigns names to specific function names'''
        self.board = self._new_game_board(rows, columns)
        self.turn = turn
        self.rows = rows
        self.rules = rules
        self.columns = columns
        self._assign_board(rules)
        self.win = win
    
    def _new_game_board(self, rows, columns) -> [[int]]:
        '''Returns the format of the board '''
        board = []
        for column in range(columns):
            board.append([])
            for row in range(rows):
                board[-1].append(NONE)
        return board

    def _opposite_color(self, color) -> None:
        '''will return the opposite color of whose turn it is'''
        if(color == BLACK): 
            return WHITE;
        else:
            return BLACK;
        
    def _current_turn(self, color):
        return color;
        

    def _assign_board(self, rules) -> None:
        '''Assigns input to the top-left position'''
        self.board[int(self.columns / 2) - 1][int(self.rows / 2) - 1] = rules
        self.board[int(self.columns / 2)][int(self.rows / 2)] = rules
        self.board[int(self.columns / 2)][int(self.rows/2) - 1] = self._opposite_color(rules)
        self.board[int(self.columns / 2) - 1][int(self.rows/2)] = self._opposite_color(rules)
        
    def count(self):
        '''Counts all black and whites tiles '''
        count_black = 0
        count_white = 0
        for row in range(self.rows):
            for column in range(self.columns):
                if self.board[column][row] == NONE:
                    pass
                if self.board[column][row] == BLACK:
                    count_black += 1
                if self.board[column][row] == WHITE:
                    count_white += 1
                else:
                    pass
        return count_black, count_white

    def check_bounds(self, rows, columns):
        '''Returns true if the row and columns are within the bounds of the board'''
        if rows >= 0 and rows < self.rows and columns >= 0 and columns < self.columns:
            return True
        return False
        
    def make_move(self, rows, columns):
        '''Makes the specified moves within the board'''
        self.board[columns][rows] = self.turn
        add = self.look_to_flip(rows, columns)
        self.flip_over(add)
        self.turn = self._opposite_color(self.turn)

    def check_left_all(self, rows, columns):
        '''Checks the left side of a row and Returns a list of the all the positions that match the color of whose turn it is '''
        checkRow = rows 
        checkColumn = columns - 1
        tally = []
        while self.check_bounds(checkRow, checkColumn) == True:
            if self.board[checkColumn][checkRow] == self._opposite_color(self.turn):
                tally.append([checkColumn,checkRow])
            elif self.board[checkColumn][checkRow] == NONE:
                return []
            elif self.board[checkColumn][checkRow]  == self.turn:
                return tally
            checkColumn = checkColumn - 1
        return []

    def check_right_all(self, rows, columns):
        '''Checks the right side of a row and Returns a list of the all the positions that match the color of whose turn it is '''
        checkRow = rows 
        checkColumn = columns + 1
        tally = []
        while self.check_bounds(checkRow, checkColumn) == True:
            if self.board[checkColumn][checkRow]  == self._opposite_color(self.turn):
                tally.append([checkColumn, checkRow])
            elif self.board[checkColumn][checkRow] == NONE:
                return []
            elif self.board[checkColumn][checkRow]  == self.turn:
                return tally
            checkColumn = checkColumn + 1
        return []

    def check_up_all(self, rows, columns):
        '''Checks up a column and Returns a list of the all the positions that match the color of whose turn it is '''
        checkRow = rows - 1
        checkColumn = columns
        tally = []
        while self.check_bounds(checkRow, checkColumn) == True:
            if self.board[checkColumn][checkRow] == self._opposite_color(self.turn):
                tally.append([checkColumn, checkRow])
            elif self.board[checkColumn][checkRow] == NONE:
                return []
            elif self.board[checkColumn][checkRow]  == self.turn:
                return tally
            checkRow = checkRow - 1
        return []
    
    def check_down_all(self, rows, columns):
        '''Checks down a column and Returns a list of the all the positions that match the color of whose turn it is '''
        checkRow = rows + 1 
        checkColumn = columns
        tally = []
        while self.check_bounds(checkRow, checkColumn) == True:
            if self.board[checkColumn][checkRow]  == self._opposite_color(self.turn):
                tally.append([checkColumn, checkRow])
            elif self.board[checkColumn][checkRow] == NONE:
                return []
            elif self.board[checkColumn][checkRow]  == self.turn:
                return tally
            checkRow = checkRow + 1
        return []
    
    def check_left_diagonal_up(self, rows, columns):
        '''Checks upper left diagonal and Returns a list of the all the positions that match the color of whose turn it is '''
        checkRow = rows - 1 
        checkColumn = columns -1
        tally = []
        while self.check_bounds(checkRow, checkColumn) == True:
            if self.board[checkColumn][checkRow]  == self._opposite_color(self.turn):
                tally.append([checkColumn, checkRow])
            elif self.board[checkColumn][checkRow] == NONE:
                return []
            elif self.board[checkColumn][checkRow]  == self.turn:
                return tally
            checkColumn = checkColumn - 1
            checkRow = checkRow -1
        return []

    def check_left_diagonal_down(self, rows, columns):
        '''Checks lower left diagonal and Returns a list of the all the positions that match the color of whose turn it is '''
        checkRow = rows + 1 
        checkColumn = columns +1
        tally = []
        while self.check_bounds(checkRow, checkColumn) == True:
            if self.board[checkColumn][checkRow]  == self._opposite_color(self.turn):
                tally.append([checkColumn, checkRow])
            elif self.board[checkColumn][checkRow] == NONE:
                return []
            elif self.board[checkColumn][checkRow]  == self.turn:
                return tally
            checkColumn = checkColumn + 1
            checkRow = checkRow + 1
        return []

    def check_right_diagonal_up(self, rows, columns):
        '''Checks upper right diagonal and Returns a list of the all the positions that match the color of whose turn it is '''
        checkRow = rows +1 
        checkColumn = columns -1
        tally = []
        while self.check_bounds(checkRow, checkColumn) == True:
            if self.board[checkColumn][checkRow]  == self._opposite_color(self.turn):
                tally.append([checkColumn, checkRow])
            elif self.board[checkColumn][checkRow] == NONE:
                return []
            elif self.board[checkColumn][checkRow]  == self.turn:
                return tally
            checkColumn = checkColumn -1
            checkRow = checkRow +1
        return []

    def check_right_diagonal_down(self, rows, columns):
        '''Checks lower right diagonal and Returns a list of the all the positions that match the color of whose turn it is '''
        checkRow = rows - 1 
        checkColumn = columns +1
        tally = []
        while self.check_bounds(checkRow, checkColumn) == True:
            if self.board[checkColumn][checkRow]  == self._opposite_color(self.turn):
                tally.append([checkColumn, checkRow])
            elif self.board[checkColumn][checkRow] == NONE:
                return []
            elif self.board[checkColumn][checkRow]  == self.turn:
                return tally
            checkColumn = checkColumn + 1
            checkRow = checkRow - 1
        return []

    def look_to_flip(self, rows, columns):
        '''Returns a list of all the positions that should be flipped '''
        add_boxes = []
        add_boxes.extend(self.check_left_all(rows, columns))
        add_boxes.extend(self.check_right_all(rows, columns))
        add_boxes.extend(self.check_up_all(rows, columns))
        add_boxes.extend(self.check_down_all(rows, columns))
        add_boxes.extend(self.check_left_diagonal_up(rows, columns))
        add_boxes.extend(self.check_left_diagonal_down(rows, columns))
        add_boxes.extend(self.check_right_diagonal_up(rows, columns))
        add_boxes.extend(self.check_right_diagonal_down(rows, columns))
        
        return add_boxes

    def flip_over(self, add_boxes):
        '''Flips over all the positions that hold the opposite color of whose turn it is ''' 
        for box in add_boxes:
            self.board[box[0]][box[1]] = self._opposite_color(self.board[box[0]][box[1]])

    def no_more_valid_moves(self):
        for row in range(self.rows):
            for column in range(self.columns):
                if self.board[column][row] == NONE:
                    for box in self.look_to_flip(row, column):
                        if box != []:
                            return False 
        return True         
        
    def is_board_full(self):
        '''Returns false if the board is not completely full with colored titles, true otherwise ''' 
        for row in range(self.rows):
            for column in range(self.columns):
                if self.board[column][row] == NONE:
                    return False 
        return True 

