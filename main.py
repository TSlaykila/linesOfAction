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
            print("valid")
        else: 
            print("Invalid Selection")
    
    def movePiece(self, board, next_row, next_col):
        checkPossible = True



        if checkPossible == True:
            if isinstance(board[next_row][next_col], Checkers) and board[next_row][next_col].color != self.color:
                board[next_row][next_col] = board[self.row][self.col]
                board[self.row][self.col] = ""
                print("what")

            elif isinstance(board[next_row][next_col], Checkers) and board[next_row][next_col].color == self.color:
                print("Invalid Move")
            else:
                board[next_row][next_col], board[self.row][self.col] = board[self.row][self.col], board[next_row][next_col] #swaps positions



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

    plyr_1.selectPiece(board,0,2)
    plyr_2.selectPiece(board,0,2)
    for row in board:
        print(row)

    plyr_1.movePiece(board,2,5)


    for row in board:
        print(row)

main()