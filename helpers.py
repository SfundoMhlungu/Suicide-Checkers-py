# the functions below are helpers, the howmany left is for the minimax hearistic value
# the nbo possible moves checks which player has won
# virtual move original created for minimax to make a fake move on a board, until it minimax finds the most optimal one

#####################attempt translation to cpp###################################################
"""
translation to cpp


nothing is new in this file, 

howmany left function  uses the exact same for loops as the board creation function,
use it a reference, also the ValidBlack or red fuctions do the same


nopossible moves functions also there is nothing new
the interesing part is the returns, 1 if player has no moves == win else return 0

virtual move function, just makes a move in a boar, checks if it is an empty or a single 
jump then takes the coordinates and make a move


"""


def howmanyleft(board, player):
    #check how many pieces black has
    size = len(board[0])
    left = 0
    if player == 'Black':
        #how many pieces are left for black
        for z in range(0, size):
            
            for j in range(0, size):
                
                if board[z][j] == 'B':
                    left += 1
    else:
        for z in range(0, size):
            
            for j in range(0, size):
                
                if board[z][j] == 'R':
                    left += 1
    return left

def nopossibleMoves(board, player, moves):
    if player == 'Black':
        
        
        
        if len(moves) == 0:
            return 1
        else:
            return 0
    
    else:
        
        if len(moves) == 0:
            return 1
        else:
            return 0
        

def VirtualMove(board, player, Move):
    if player == 'Black':
        #single move
        if len(Move) == 3:
            board[Move['oldpos'][0]][Move['oldpos'][1]] = 'E'
            board[Move['enemy'][0]][Move['enemy'][1]] = 'E'
            board[Move['new'][0]][Move['new'][1]] = 'B'
################################################# NEW #######################################################################
        elif len(Move) == 4:
            print('Black double move: ', Move)
            board[Move['oldpos'][0]][Move['oldpos'][1]] = 'E'
            
            board[Move['enemy1'][0]][Move['enemy1'][1]] = 'E'
            board[Move['enemy2'][0]][Move['enemy2'][1]] = 'E'
            
            board[Move['new'][0]][Move['new'][1]] = 'B'
############################################################################################################################
            
            
            
        else:
            
            board[Move['oldpos'][0]][Move['oldpos'][1]] = 'E'
            board[Move['new'][0]][Move['new'][1]] = 'B'
    # for red player
    else:
        if len(Move) == 3:
            board[Move['oldpos'][0]][Move['oldpos'][1]] = 'E'
            board[Move['enemy'][0]][Move['enemy'][1]] = 'E'
            board[Move['new'][0]][Move['new'][1]] = 'R'
 #################################### NEW ##################################################################       
        elif len(Move) == 4:
            
            
            board[Move['oldpos'][0]][Move['oldpos'][1]] = 'E'
            
            board[Move['enemy1'][0]][Move['enemy1'][1]] = 'E'
            board[Move['enemy2'][0]][Move['enemy2'][1]] = 'E'
            
            board[Move['new'][0]][Move['new'][1]] = 'R'
###########################################################################################################
        else:
            board[Move['oldpos'][0]][Move['oldpos'][1]] = 'E'
            board[Move['new'][0]][Move['new'][1]] = 'R'
        
        
    
            
            

        
       
            
  
                
    