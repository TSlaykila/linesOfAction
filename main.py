class Checkers():
    def __init__(self, color):
        if color == "W":
            self.plyr = 1
        
        if color == "B":
            self.plyr = 2
        self.color = color
        self.row = None
        self.col = None

    def __repr__(self):
        return self.color
    
    def selectPiece(self, board, row, col):
        if board[row][col] == self:
            self.row = row
            self.col = col
            print("valid selection of piece")
        else: 
            print("Invalid Selection")
    
    def moveAxisQuantifier(self, board):
        if isinstance(board[self.row][self.col], Checkers):
            x_axis = 0
            y_axis = 0
            for i in range(8):
                if isinstance(board[self.row][i], Checkers):
                    x_axis += 1
                if isinstance(board[i][self.col], Checkers):
                    y_axis += 1
            
            #Calculate Diagonal LeftUp to RightDown maximun movement
            j = self.row
            k = self.col
            while k != 0 and j != 0:
                j -= 1
                k -= 1

            if k == 0:
                diagCal = j
            else: diagCal = k
            
            diagonalLeftUp = 0
            for i in range(8 - diagCal):
                if isinstance(board[j][k], Checkers):
                    diagonalLeftUp += 1
                j += 1
                k += 1

            #Calculate Diagonal LeftDown to RightUp maximun movement
            j = self.row
            k = self.col
            while k != 0:
                k -= 1
                j += 1
            
            diagonalRightDown = 0
            for i in range(j+1):
                if isinstance(board[j][k], Checkers):
                    diagonalRightDown += 1
                j -= 1
                k += 1

                
            return [x_axis, y_axis, diagonalLeftUp, diagonalRightDown]

        else:
            print("Please, Select a piece")

    def move(self, board, next_row, next_col): 
            """Callback function for movePiece"""
            if isinstance(board[next_row][next_col], Checkers) and board[next_row][next_col].color != self.color:
                board[next_row][next_col] = board[self.row][self.col]
                board[self.row][self.col] = ""
                print("Enemy Piece captured")
                #change turn

            elif isinstance(board[next_row][next_col], Checkers) and board[next_row][next_col].color == self.color:
                print("Illegal Move, capturing own piece, try a legal move")
                #dont change turn
            else:
                board[next_row][next_col], board[self.row][self.col] = board[self.row][self.col], board[next_row][next_col] #swaps positions
                print("Piece Succesfully moved")
                #change turn
    
    def movePiece(self, board, next_row, next_col):
        legal_options = self.moveAxisQuantifier(board)
        squaresAway = abs(next_row - self.row)+abs(next_col - self.col)
        #Vertical Move
        if (next_row == self.row and squaresAway <= legal_options[0]):
            self.move(board, next_row, next_col)

        #Horizontal Move
        if (next_col == self.col and squaresAway <= legal_options[1]):
            self.move(board, next_row, next_col)
        
        #Diagonal Move
        if (next_col != self.col and next_row != self.row):
            squaresAway = squaresAway / 2

        
            self.move(board, next_row, next_col)

        

        else: print("Illegal Move, try a legal one")
          
           



def main():
    """Setting up game enviroment: board, players, grid"""
    plyr_2 = Checkers("B")
    plyr_1 = Checkers("w")
    
    turn = 1

    board = [["" for _ in range(8)] for _ in range(8)]
    for i in range(6):
        board[0][i+1] = plyr_1
        board[-1][i+1] = plyr_1

        board[i+1][0] = plyr_2
        board[i+1][-1] = plyr_2  

    plyr_2.selectPiece(board,1,0)

    for row in board:
        print(row)

    plyr_2.movePiece(board,4,3)
 



    for row in board:
        print(row)

main()