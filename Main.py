from is_valid import *
from helpers import *
import random
import time
from Minimax import *
import copy

E = 'E'
# 6, 8, 10, 12
six  =  [ [' ', 'R', ' ', 'R', ' ', 'R'],
['R', ' ', 'R', ' ', 'R', ' '],

[' ', 'E', ' ', 'E', ' ', 'E'],
['E', ' ', 'E', ' ', 'E', ' '],

[' ', 'B', ' ', 'B', ' ', 'B'],
['B', ' ', 'B', ' ', 'B', ' '],]

eight = [[' ',0,' ',0,' ',0,' ',0],
         [0,' ',0,' ',0,' ',0,' '],
         [' ',0,' ',0,' ',0,' ',0],
         [E,' ',E,' ',E,' ',E,' '],
         [' ',E,' ',E,' ',E,' ',E],
         [0,' ',0,' ',0,' ',0,' '],
         [' ',0,' ',0,' ',0,' ',0],
         [0,' ',0,' ',0,' ',0,' ']]
ten = [[' ',0,' ',0,' ',0,' ',0 , ' ', 0],
         [0,' ',0,' ',0,' ',0,' ', 0, ' '],
         [' ',0,' ',0,' ',0,' ',0, ' ', 0],
         [0,' ',0,' ',0,' ',0,' ', 0, ' '],
         [' ',E,' ',E, ' ',E, ' ', E, ' ', E],
         [E,' ',E, ' ', E, ' ',E, ' ', E, ' '],
         [' ',0,' ',0,' ',0,' ',0, ' ', 0],
         [0,' ',0,' ',0,' ',0,' ', 0, ' '],
         [' ',0,' ',0,' ',0,' ',0, ' ', 0],
         [0,' ',0,' ',0,' ',0,' ', 0, ' ']]

twelve = [[' ',0,' ',0,' ',0,' ',0 , ' ', 0, ' ', 0],
         [0,' ',0,' ',0,' ',0,' ', 0, ' ', 0 , ' '],
         [' ',0,' ',0,' ',0,' ',0, ' ', 0, ' ', 0],
        [0,' ',0,' ',0,' ',0,' ', 0, ' ', 0, ' '],
        [' ',0,' ',0,' ',0,' ',0, ' ', 0, ' ', 0],
      
         [E,' ',E,' ',E,' ',E,' ', E, ' ', E, ' '],
         [' ',E,' ',E,' ',E,' ',E, ' ', E, ' ', E],
     
         [0,' ',0,' ',0,' ',0,' ', 0, ' ', 0, ' '],
         [' ',0,' ',0,' ',0,' ',0, ' ', 0, ' ', 0],
         [0,' ',0,' ',0,' ',0,' ', 0, ' ', 0, ' '],
         [' ',0,' ',0,' ',0,' ',0, ' ', 0, ' ', 0],
         [0,' ',0,' ',0,' ',0,' ', 0, ' ', 0, ' ']]


valid_sizes = [6, 8, 10, 12]

size = 0
board = []
redlayout = []
topletters = 0
while True:
    size = int(input('choose board size eg : 8  '))
    
    if size in valid_sizes:
        column = int(size /2)
       
        row = column - 1
        
        if size == 6:
            currentboard = six
            topletters = ['A',  'B', 'C', 'D', 'E', 'F']
        elif size == 8:
            topletters = ['A',  'B', 'C', 'D', 'E', 'F', 'G', 'H']
            currentboard = eight
        elif size == 10:
            topletters = ['A',  'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
            currentboard = ten
        else:
            topletters = ['A',  'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L']
            currentboard = twelve
        
        loop = 0
        startCol = 1
        # loop red players
        for i in range(0, row):
            if i % 2 != 0 and loop > 0:
                loop = 0
                startCol = 0
            else:
                loop = 0
                startCol = 1
            for j in range(0, column):
                if loop > 0:
            
                    startCol = startCol + 2
                    
                    # print(i,' ' ,startCol) 
                    currentboard[i][startCol] = 'R'
                else:
                    # print(i,' ' ,startCol) 
                    currentboard[i][startCol] = 'R'
                    
                    
                    loop += 1
                   
        
        row = row + 2
        startCol = 0
        loop = 0
        for i in range(row, size):
            if i % 2 != 0:
                
                startCol = 0
            else:
                
                startCol = 1
            for j in range(0, column):
                
                
                # print(i,' ' ,startCol) 
                currentboard[i][startCol] = 'B'
                loop += 1
                startCol = startCol + 2
                    
                    
                
                

                
            
        board = currentboard    
        break
    else:
        print('valid sizes: 6, 8, 10, 12')
        continue



for i in redlayout:
    print(i)


for i in board:
    print(i)
    
# empytB = validBlack(board)
# empytR = validRed(board)

# print('Black')
# print(empytB)
# print('Red')
# print(empytR)


player = 'Black'
while True:
    if player == 'Black':
        moves = validBlack(board)
        
        # okay this is b=new it checks if black or red has won(using the no possible moves function from the helpers)
        haswon_or_not =  nopossibleMoves(board, player, moves)
        
        #if black has won break out of the loop and print black has won
        if haswon_or_not == 1:
            print('Black has no moves, Black Won By suicide')
            print()
            print(topletters)
            print()
            
            for i in board:
                
                print(i)
                
            break
        # else if red has won, print red has won and break out the while loop
        elif nopossibleMoves(board, 'Red', validRed(board)) == 1:
            print('Red has no moves, Red Won By suicide')
            print()
            print(topletters)
            print()
            
            for i in board:
                
                print( i)
                
            break
            
        # else call the minimax, and return the best move
        else:
            # first it is important to give minimax a copy of the board, not the real one cuase it will ruin it
            # it needs a board to make all possible moves on the side then tell black which is best
            # then balck makes the move on the real board, NB look for a way to copy the board, do not assign it to a new var, 
            # look for a way to copy arrays in cpp
            boardCopy = copy.deepcopy(board)
            # the minimax takes the copy of the board, depth(how long must the tree bee), then True meaning black is the maximizing player
            bestMove, Score =  minimax(boardCopy, 6, True)
            
            print('BestMove For Black:', bestMove)
            # the higher the score == close to random move for black, meaning it has no effect on winning, 30 = random move for black
            print('score', Score)
            # then this function from helper do the minimax return move on the real board not copy
            VirtualMove(board, 'Black', bestMove)
        
        
           
            
            player = 'Red'
            print()
            print(topletters)
            print()
            
            for i in board:
                print(i)
               
            time.sleep(5)
            print('Red player turn')
    # red player turn same as above difference is the algorithim
    else:
        moves = validRed(board)
        
        haswon_or_not = nopossibleMoves(board, 'Red', moves)
        
       
        
        if haswon_or_not == 1:
            print('Red has no moves, Red Won By suicide')
            print()
            print(topletters)
            print()
            
            for i in board:
                print(i)
                
            break
        elif nopossibleMoves(board, 'Black', validBlack(board)) == 1:
            print('Black has no moves, Black Won By suicide')
            print()
            print(topletters)
            print()
            
            for i in board:
                
                print(i)
              
            break
        else:
            
            #Red is using the random algorithm
            randmove = random.choice(moves)
            VirtualMove(board, 'Red', randmove)
            
        
        
        
            
            player = 'Black'
            print()
            print(topletters)
            print()
            
            for i in board:
                print(i)
               
            time.sleep(5)


# for i in board:
#     print(i)
        
            
            
            
          
        
        
    




