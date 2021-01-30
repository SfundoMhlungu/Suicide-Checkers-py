# for black
def isSingleBlack(board, row, column, size):
    moves = []
    #look left first
    if column - 2 >= 0 and row - 2 >= 0 and board[row-1][column-1] == 'R' and board[row-2][column-2] == 'E':
        moves.append({'oldpos': [row, column], 'enemy': [row-1, column - 1], 'new': [row-2, column - 2]})
    #look right
    if column + 2 <= size-1 and row - 2 >= 0 and board[row-1][column+1] == 'R' and board[row-2][column+2] == 'E':
        moves.append({'oldpos': [row, column], 'enemy': [row-1, column+1], 'new': [row-2, column + 2]})
        
    if len(moves) != 0:
        return moves
    else:
        return False
######################################################  NEW ########################################################################################
def doubleBlack(board, row, column, size):
    #look left
    moves = []
    if column - 4 >= 0 and row - 4 >= 0 and board[row-1][column-1] == 'R' and board[row-2][column-2] == 'E' and board[row-3][column-3] == 'R' and board[row-4][column-4] == 'E' :
        moves.append({'oldpos': [row, column], 'enemy1': [row-1, column-1], 'enemy2': [row-3, column-3], 'new': [row-4, column-4] })
   
    #look right
    if column + 4 <= size-1 and row - 4 >= 0 and board[row-1][column+1] == 'R' and board[row-2][column+2] == 'E' and board[row-3][column+3] == 'R' and board[row-4][column+4] == 'E':
        moves.append({'oldpos': [row, column], 'enemy1': [row-1, column+1], 'enemy2': [row-3, column+3], 'new': [row-4, column+4] })
         
    if len(moves) != 0:
        return moves
    else:
        return False
###############################################################################################################################################
def isEmptyBlack(board, row, column, size):
    moves = []
    #look left
    if column - 1 >= 0 and row -1 >= 0 and board[row-1][column-1] == 'E':
        moves.append({'oldpos': [row, column], 'new' : [row-1, column-1]})
    #look right
    if  column + 1 <= size-1 and row - 1 >= 0 and board[row-1][column+1] == 'E':
        moves.append({'oldpos': [row, column], 'new' : [row-1, column+1]})
    
    if len(moves) != 0:
        return moves
    else:
        return False




    

def isSingleRed(board, row, column, size):
    moves = []
    #look left 
    if column + 2 <= size-1 and row + 2 <= size-1 and board[row + 1][column + 1] == 'B' and board[row+2][column+2] == 'E':
        moves.append({'oldpos': [row, column], 'enemy': [row+1, column+1 ], 'new' : [row + 2, column + 2]})
    
    #look right
    if column - 2 >= 0 and row + 2 <= size-1  and board[row + 1][column - 1] == 'B' and board[row+2][column-2] == 'E':
        moves.append({'oldpos': [row, column], 'enemy': [row+1, column - 1 ], 'new' : [row + 2, column - 2]})
    
    if len(moves) != 0:
        return moves
    else:
        return False
    
        

def isEmptyRed(board, row, column, size):
    moves = []
    #look left
    if column + 1 <= size-1 and row + 1 <= size-1 and board[row+1][column+1] == 'E':
        moves.append({'oldpos': [row, column], 'new': [row + 1, column + 1]})
    
    #look right
    if column - 1 >= 0 and row + 1 <= size-1 and board[row+1][column-1] == 'E':
        moves.append({'oldpos': [row, column], 'new':[row + 1, column - 1]})
    
    if len(moves) != 0:
        return moves
    else: 
        return False


##################################################  NEW   ########################################################################################
def doubleRed(board, row, column, size):
    moves = []
    if column + 4 <= size-1 and row + 4 <= size-1 and board[row + 1][column + 1] == 'B' and board[row+2][column+2] == 'E' and board[row+3][column+3] == 'B' and board[row+4][column+4]== 'E':
        moves.append({'oldpos': [row, column], 'enemy1': [row+1, column+1 ], 'enemy2' : [row + 3, column + 3], 'new': [row+4, column+4]})
   
    #look right
    if column - 4 >= 0 and row + 4 <= size-1  and board[row + 1][column - 1] == 'B' and board[row+2][column-2] == 'E' and board[row+3][column-3]== 'B' and board[row+4][column-4] == 'E':
        moves.append({'oldpos': [row, column], 'enemy1': [row+1, column-1 ], 'enemy2' : [row + 3, column - 3], 'new': [row+4, column - 4]})
    
    if len(moves) != 0:
        return moves
    else: 
        return False 
 ########################################################################################################################################   
   
    
    
    
    

def validBlack(board):
    size = len(board[0])
    overallBlackMoves = []
    for z in range(0, size):
        
        for j in range(0, size):
            
            if board[z][j] == 'B':
                #look for empty
                Empty = isEmptyBlack(board, z, j, size)
                if Empty:
                    for i in Empty:
                        overallBlackMoves.append(i)
                Single = isSingleBlack(board, z, j, size)
                # print(Single)
                if Single:
                    for i in Single:
                        overallBlackMoves.append(i)
                
                ################################## NEW ###########################################
                double = doubleBlack(board, z, j, size)
                if double:
                    for i in double:
                        overallBlackMoves.append(i)
                    
                
                
                ##################################################################################
                
    return overallBlackMoves


def validRed(board):
    size = len(board[0])
    
    overallRedMoves = []
    
    for z in range(0, size):
        
        for j in range(0, size):
            if board[z][j] == 'R':
                empty = isEmptyRed(board, z, j, size)
                if empty:
                    for i in empty:
                        overallRedMoves.append(i)
                single = isSingleRed(board, z, j, size) 
                # print(single)
                if single:
                    for i in single:
                        overallRedMoves.append(i)
                ########################################## New  ########################################################################
                double = doubleRed(board, z, j, size)
                if double:
                    for i in double:
                        overallRedMoves.append(i)
                
                ######################################################################################################################
                
    return overallRedMoves
                    
                
                