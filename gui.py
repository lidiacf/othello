# GUI

import tkinter
import game_logic 


class GameSettings:
    def __init__(self):
    
        self._settings_window = tkinter.Toplevel()
        self._settings_window.title('Othello Game Settings')

        #           ROW   SETTINGS
        
        self.row_settings_label = tkinter.Label(
            master = self._settings_window, text = 'Row Settings ',
            font = ('Times New Roman', 15))

        self.row_settings_label.grid(
            row = 0, column = 0, padx = 10, pady = 10) 

        self.row_settings_instructions = tkinter.Label(
            master = self._settings_window, text = 'Enter an even integer between 4 and 16:',
            font = ('Times New Roman', 15))

        self.row_settings_instructions.grid(
            row = 1, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W) 
        
        self.row_settings_entry = tkinter.Entry(
            master = self._settings_window, width = 20, font = ('Times New Roman', 10))
        
        self.row_settings_entry.grid(
            row = 2, column = 0, padx = 10, pady = 1,
            sticky = tkinter.W + tkinter.E)

        #          COLUMN   SETTINGS

        self.column_settings_label = tkinter.Label(
            master = self._settings_window, text = 'Column Settings ',
            font = ('Times New Roman', 15))

        self.column_settings_label.grid(
            row = 4, column = 0, padx = 10, pady = 10) 

        self.column_settings_instructions = tkinter.Label(
            master = self._settings_window, text = 'Enter an even integer between 4 and 16 (Must use the same number selected in Row Settings):',
            font = ('Times New Roman', 15))

        self.column_settings_instructions.grid(
            row = 6, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W) 
        
        self.column_settings_entry = tkinter.Entry(
            master = self._settings_window, width = 20, font = ('Times New Roman', 10))
        
        self.column_settings_entry.grid(
            row = 7, column = 0, padx = 10, pady = 1,
            sticky = tkinter.W + tkinter.E)

        #           FIRST MOVE SETTINGS

        self.first_move_settings_label = tkinter.Label(
            master = self._settings_window, text = 'First Move Settings ',
            font = ('Times New Roman', 15))

        self.first_move_settings_label.grid(
            row = 9, column = 0, padx = 10, pady = 10) 

        self.first_move_settings_instructions = tkinter.Label(
            master = self._settings_window, text = 'Enter either "BLACK" or "WHITE" for player who will have first move',
            font = ('Times New Roman', 15))

        self.first_move_settings_instructions.grid(
            row = 10, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W) 
        
        self.first_move_settings_entry = tkinter.Entry(
            master = self._settings_window, width = 20, font = ('Times New Roman', 10))
        
        self.first_move_settings_entry.grid(
            row = 11, column = 0, padx = 10, pady = 1,
            sticky = tkinter.W + tkinter.E)

        #         GRID ARRANGEMENT SETTINGS 

        self.grid_arrangement_settings_label = tkinter.Label(
            master = self._settings_window, text = 'Grid Arrangement Settings ',
            font = ('Times New Roman', 15))

        self.grid_arrangement_settings_label.grid(
            row = 12, column = 0, padx = 10, pady = 10) 

        self.grid_arrangement_settings_instructions = tkinter.Label(
            master = self._settings_window, text = 'Enter either "BLACK" or "WHITE" for player who will have TOP-LEFT position',
            font = ('Times New Roman', 15))

        self.grid_arrangement_settings_instructions.grid(
            row = 13, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W) 
        
        self.grid_arrangement_settings_entry = tkinter.Entry(
            master = self._settings_window, width = 20, font = ('Times New Roman', 10))
        
        self.grid_arrangement_settings_entry.grid(
            row = 14, column = 0, padx = 10, pady = 1,
            sticky = tkinter.W + tkinter.E)

        #          WINNER   SETTINGS
        
        self.winner_settings_label = tkinter.Label(
            master = self._settings_window, text = 'Winner Settings ',
            font = ('Times New Roman', 15))

        self.winner_settings_label.grid(
            row = 15, column = 0, padx = 10, pady = 10) 

        self.winner_settings_instructions = tkinter.Label(
            master = self._settings_window, text = 'Enter either ">" if player with greater discs wins or "<" if player with fewer discs wins:',
            font = ('Times New Roman', 15))

        self.winner_settings_instructions.grid(
            row = 16, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W) 
        
        self.winner_settings_entry = tkinter.Entry(
            master = self._settings_window, width = 20, font = ('Times New Roman', 10))
        
        self.winner_settings_entry.grid(
            row = 17, column = 0, padx = 10, pady = 1,
            sticky = tkinter.W + tkinter.E)
        
        #          BUTTON THAT LAUNCHES THE CANVAS

        button_command = tkinter.Frame(master = self._settings_window)

        button_command.grid(
            row = 20, column = 0, padx = 10, pady = 10,
            sticky = tkinter.S)

        enter_button = tkinter.Button(
            master = button_command, text = 'BEGIN GAME', font = ('Times New Roman', 15),
            command = self._enter_button_clicked)

        enter_button.grid(row = 20, column = 0, padx = 10, pady = 10)

        self._settings_window.rowconfigure(3, weight = 1)
        self._settings_window.columnconfigure(1, weight = 1)

    def show(self) -> None:
        self._settings_window.grab_set()
        self._settings_window.wait_window()

    def get_row_settings(self):
        return self.row_settings

    def get_column_settings(self):
        return self.column_settings

    def get_first_move_settings(self):
        return self.first_move_settings
    
    def get_grid_arrangement_settings(self):
        return self.grid_arrangement_settings

    def get_winner_settings(self):
        return self.winner_settings
        
    def _enter_button_clicked(self):
        self.row_settings = self.row_settings_entry.get()
        self.column_settings = self.column_settings_entry.get()
        self.first_move_settings = self.first_move_settings_entry.get()
        self.grid_arrangement_settings = self.grid_arrangement_settings_entry.get()
        self.winner_settings = self.winner_settings_entry.get() 
        self._settings_window.destroy()
        enter_button_action = GameLaunch( self.row_settings, self.column_settings, self.first_move_settings, self.grid_arrangement_settings, self.winner_settings)
        enter_button_action.start()

class GameSetup:
    def __init__(self):
##        self._state = three_othello_game_logic.othello

        self._window = tkinter.Tk()
        self._window.title('Othello')
        begin_button = tkinter.Button(
            master = self._window, text = 'Begin Game',
            font = ('Times New Roman', 15), command = self._button_clicked )
        begin_button.grid(
            row = 0, column = 0, padx = 60, pady = 60,
            sticky = tkinter.N + tkinter.E + tkinter.S + tkinter.W)
        self._window.rowconfigure(0, weight = 1)
        self._window.rowconfigure(1, weight = 1)
        self._window.columnconfigure(0, weight = 1)

    def start(self) -> None:
        self._window.mainloop()

    def _button_clicked(self) -> None:
        selected_button = GameSettings()
        selected_button.show()
        
class GameLaunch:
    def __init__(self, row: float, column: float, first_move: str, grid_arrangement: str, winner: str):
        self._grid_row = row
        self._grid_column = column
        self._grid_win = winner        
        self.row_click = 0
        self.column_click = 0
        if first_move == "WHITE":
            self._grid_first_move = 2
        elif first_move == "BLACK":
            self._grid_first_move = 1
        if grid_arrangement == "WHITE":
            self._grid_arrangement = 2
        elif grid_arrangement == "BLACK":
            self._grid_arrangement = 1
        self._othello_class = game_logic.othello(int(self._grid_row), int(self._grid_column), self._grid_first_move, self._grid_arrangement, self._grid_win)    
        self._canvas_window = tkinter.Tk()
        self._canvas_window.title('Othello Game Board')
        self.canvas_width = 600
        self.canvas_height = 600
        self._canvas = tkinter.Canvas(
            master = self._canvas_window, width = self.canvas_width, height = self.canvas_height,
            background = 'forest green')
        self._canvas.grid(
            row = 1, column = 0, columnspan = 3, padx = 10, pady = 10,
            sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)
        self._canvas.bind('<Configure>', self._on_canvas_resized)
        self._canvas.bind('<Button-1>', self._on_canvas_clicked)
        self._canvas_window.rowconfigure(1, weight = 1)
        self._canvas_window.columnconfigure(0, weight = 1)
        
        if self._othello_class.turn == 2:
            self.white_turns_label = tkinter.Label(master = self._canvas_window, text = 'TURN: WHITE', font = ('Times New Roman', 15))
            self.white_turns_label.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = tkinter.W + tkinter.E)
               
        if self._othello_class.turn == 1:
            self.black_turns_label = tkinter.Label(master = self._canvas_window, text = 'TURN: BLACK', font = ('Times New Roman', 15))
            self.black_turns_label.grid(row = 0, column = 0, padx = 10, pady = 10, stick = tkinter.W + tkinter.E)

            

    def start(self):
        self._canvas_window.mainloop()

    def _on_canvas_resized(self, event: tkinter.Event) -> None:
        self._canvas.delete(tkinter.ALL)
        self._canvas_window.update()
        self.canvas_width = self._canvas.winfo_width()
        self.canvas_height = self._canvas.winfo_height()        
        self.draw_row_lines()
        self.draw_column_lines()        
        self.redraw()
        for box in self._othello_class.board:
            print(box)
 
        print('the function _on_canvas_resized has been executed')

    def _on_canvas_clicked(self, event: tkinter.Event) -> None:
        self.column_click = int(event.x // (self.canvas_width / int(self._grid_column)))
        self.row_click = int(event.y // (self.canvas_height / int(self._grid_row)))
        self.make_a_move()

    def draw_column_lines(self):
        for i in range(int(self._grid_column)):
            count_row_num = (self.canvas_width/int(self._grid_column)) * i
            self._canvas.create_line(count_row_num, 0, count_row_num, self.canvas_width, fill = 'black')

    def draw_row_lines(self):
        for i in range(int(self._grid_row)):
            count_column_num = (self.canvas_width/int(self._grid_row)) * i
            self._canvas.create_line(0, count_column_num, self.canvas_width, count_column_num, fill = 'black')       
            
    def round2_pos_on_board(self):
        row_divided = (self.canvas_height / int(self._grid_row))       
        column_divided = (self.canvas_width / int(self._grid_column))
        if self._grid_arrangement == three_othello_game_logic.BLACK:
            self._othello_class._assign_board(self._grid_arrangement)           
        if self._grid_arrangement == three_othello_game_logic.WHITE:
            self._othello_class._assign_board(self._grid_arrangement)
        for i in range(len(self._othello_class.board)):
            for j in range(len(self._othello_class.board)):
                if self._othello_class.board[i][j] == 1:
                    self._canvas.create_oval((i * float(column_divided)), (j  * float(column_divided)), (( i+ 1) * float(column_divided)), ((j+ 1) * float(column_divided)), fill = 'Black', outline = '#000000')
                elif self._othello_class.board[i][j] == 2:
                    self._canvas.create_oval((i * float(column_divided)), (j  * float(column_divided)), ((i + 1) * float(column_divided)), ((j + 1) * float(column_divided)), fill = 'Black', outline = '#000000')
            color_count = self._othello_class.count()
            black_on_board, white_on_board = color_count           
            self.black_count_label = tkinter.Label(master = self._canvas_window, text = 'BLACK: {}'.format(black_on_board), font = ('Times New Roman', 15))
            self.black_count_label.grid(row = 0, column = 1, padx = 10, pady = 10, sticky = tkinter.W)           
            self.white_count_label = tkinter.Label(master = self._canvas_window, text = 'WHITE: {}'.format(white_on_board), font = ('Times New Roman', 15))
            self.white_count_label.grid(row = 0, column = 2, padx = 10, pady = 10, sticky = tkinter.E + tkinter.S)
        self._canvas.delete(tkinter.ALL)

       
    def make_a_move(self):
        row_divided = (self.canvas_height/ int(self._grid_row))
        column_divided = (self.canvas_width / int(self._grid_column))

        if len(self._othello_class.look_to_flip(self.row_click, self.column_click)) > 0:
            self._othello_class.make_move(self.row_click, self.column_click )
            
        for i in range(len(self._othello_class.board)):
            for j in range(len(self._othello_class.board)):
                if self._othello_class.board[i][j] == 1:
                    self._canvas.create_oval((i * float(column_divided)), (j  * float(column_divided)), (( i+ 1) * float(column_divided)), ((j+ 1) * float(column_divided)), fill = 'Black', outline = '#000000')
                elif self._othello_class.board[i][j] == 2:
                    self._canvas.create_oval((i * float(column_divided)), (j  * float(column_divided)), ((i + 1) * float(column_divided)), ((j + 1) * float(column_divided)), fill = 'White', outline = '#000000')
            color_count = self._othello_class.count()
            black_on_board, white_on_board = color_count
            
            self.black_count_label = tkinter.Label(master = self._canvas_window, text = 'BLACK: {}'.format(black_on_board), font = ('Times New Roman', 15))
            self.black_count_label.grid(row = 0, column = 1, padx = 10, pady = 10, sticky = tkinter.W + tkinter.E)
                
            self.white_count_label = tkinter.Label(master = self._canvas_window, text = 'WHITE: {}'.format(white_on_board), font = ('Times New Roman', 15))
            self.white_count_label.grid(row = 0, column = 2, padx = 10, pady = 10, sticky = tkinter.W + tkinter.E)

            if self._othello_class.turn == 2:
                self.white_turns_label = tkinter.Label(master = self._canvas_window, text = 'TURN: WHITE', font = ('Times New Roman', 15))
                self.white_turns_label.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = tkinter.W + tkinter.E)
                   
            if self._othello_class.turn == 1:
                self.black_turns_label = tkinter.Label(master = self._canvas_window, text = 'TURN: BLACK', font = ('Times New Roman', 15))
                self.black_turns_label.grid(row = 0, column = 0, padx = 10, pady = 10, stick = tkinter.W + tkinter.E)

            
            if self._othello_class.is_board_full() == True:
                
                if self._grid_win == '<': #player with fewest wins               
                    if black_on_board < white_on_board:
                       print('WINNER: BLACK')
                       self.winner_black_label = tkinter.Label(master = self._canvas_window, text = 'WINNER: BLACK', font = ('Times New Roman', 15))
                       self.winner_black_label.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = tkinter.W)
                    elif black_on_board > white_on_board:
                       print('WINNER: WHITE')
                       self.winner_white_label = tkinter.Label(master = self._canvas_window, text = 'WINNER: WHITE',font = ('Times New Roman', 15))
                       self.winner_white_label.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = tkinter.W)                      
                    elif black_on_board == white_on_board:
                        print('WINNER: NONE')
                        self.winner_none_label = tkinter.Label(master = self._canvas_window, text = 'WINNER: TIE!',font = ('Times New Roman', 15))
                        self.winner_none_label.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = tkinter.W)
     
                if self._grid_win == '>':                        
                    if black_on_board > white_on_board:
                        print('WINNER: BLACK')
                        self.winner_black_label = tkinter.Label(master = self._canvas_window, text = 'WINNER: BLACK',font = ('Times New Roman', 15))
                        self.winner_black_label.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = tkinter.W)                       
                    elif black_on_board < white_on_board:
                        print('WINNER: WHITE')
                        self.winner_white_label = tkinter.Label(master = self._canvas_window, text = 'WINNER: WHITE',font = ('Times New Roman', 15))
                        self.winner_white_label.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = tkinter.W)                      
                    elif black_on_board == white_on_board:
                        print('WINNER: NONE')
                        self.winner_none_label = tkinter.Label(master = self._canvas_window, text = 'WINNER: TIE!',font = ('Times New Roman', 15))
                        self.winner_none_label.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = tkinter.W)
                       
            if self._othello_class.no_more_valid_moves() == True:

                if self._grid_win == '<': #player with fewest wins               
                    if black_on_board < white_on_board:
                        print('WINNER: BLACK')
                        self.winner_black_label = tkinter.Label(master = self._canvas_window, text = 'WINNER: BLACK', font = ('Times New Roman', 15))
                        self.winner_black_label.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = tkinter.W)                        
                    elif black_on_board > white_on_board:
                        print('WINNER: WHITE')
                        self.winner_white_label = tkinter.Label(master = self._canvas_window, text = 'WINNER: WHITE', font = ('Times New Roman', 15))
                        self.winner_white_label.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = tkinter.W)
                    elif black_on_board == white_on_board:
                        print('WINNER: NONE')
                        self.winner_none_label = tkinter.Label(master = self._canvas_window, text = 'WINNER: TIE!', font = ('Times New Roman', 15))
                        self.winner_none_label.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = tkinter.W)
     
                if self._grid_win == '>':                        
                    if black_on_board > white_on_board:
                        print('WINNER: BLACK')
                        self.winner_black_label = tkinter.Label(master = self._canvas_window, text = 'WINNER: BLACK', font = ('Times New Roman', 15))
                        self.winner_black_label.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = tkinter.W)                       
                    elif black_on_board < white_on_board:
                        print('WINNER: WHITE')
                        self.winner_white_label = tkinter.Label(master = self._canvas_window, text = 'WINNER: WHITE',font = ('Times New Roman', 15))
                        self.winner_white_label.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = tkinter.W)                       
                    elif black_on_board == white_on_board:
                        print('WINNER: NONE')
                        self.winner_none_label = tkinter.Label(master = self._canvas_window, text = 'WINNER: TIE!', font = ('Times New Roman', 15))
                        self.winner_none_label.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = tkinter.W)

    def redraw(self):        
        row_divided = (self.canvas_height/ int(self._grid_row))
        column_divided = (self.canvas_width / int(self._grid_column))       
        for i in range(len(self._othello_class.board)):
            for j in range(len(self._othello_class.board)):
                if self._othello_class.board[i][j] == 1:
                    self._canvas.create_oval((i * float(column_divided)), (j  * float(column_divided)), (( i+ 1) * float(column_divided)), ((j+ 1) * float(column_divided)), fill = 'Black', outline = '#000000')
                elif self._othello_class.board[i][j] == 2:
                    self._canvas.create_oval((i * float(column_divided)), (j  * float(column_divided)), ((i + 1) * float(column_divided)), ((j + 1) * float(column_divided)), fill = 'White', outline = '#000000')
        
 
if __name__ == '__main__':
    GameSetup().start()
