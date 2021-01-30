#there is no need to import these here, cause they are imported in the main file
# where trhe minimax is called
from helpers import *
from is_valid import *
import random


'''
there is no need to know how the below function works, just translate it, then have an abstract knoweldge on how it works

basically

it takes a copy of the board in it's current state
then it looks for all possible moves the current player can make, then make those moves one by one using the for eachMove in possible moves
after making the first possible moves, it calls itself to make the move for the other play, entlek what it is doing is given a depth, let'ss say
of 4, and current player is black

1) it will look for all's black possible moves, let's say their 5 black possible moves (maximizing player)
2) then the virtual move take the first of the 5 and make it on the board
3) then the minimax is called (now with false in maximizing) meaning it is minimizing players turn
5) then minizing player is white(will look for all whites possible move)
6) do number 2
3) then 3 but calling minimax with true, which means it blacks player turn

when it reaches a depth of 0 or a terminal state(black or white won)

it computes the heurist value( just checking how many black pieces are left)

and then tells the calling AI in main the best move is the one that will make us lose more pieces


# to understand this better, watch sabestain lague video on minimax(it is very short), write exactly what he says on ur report
cause the below minix works like that, but the mistake sebestain makes is calling board position, whenever he says position he means the current state of the board
like that guy from coding train explains


for translation the minimax uses the same for loops as other functions u wrote before

'''

#note this function is written in blacks perspective meaning black is the maximizing player, picking the move that will result in losing more pieces
# and red is minizing player maening take the move that will result in black losing less pieces


def minimax(board, depth, isMaximizing):
    #this is the thing that stops the minimax from calling itself, then calculate the howmany pieces left,
    #based on that tells the ai which move will result in losing more pieces thereby win
    if depth == 0 or nopossibleMoves(board, 'Black', validBlack(board)) == 1 or nopossibleMoves(board, 'Red',validRed(board) ) == 1:
        # if black in that board wins return 0 cause 0 pieces means win
        if nopossibleMoves(board, 'Black', validBlack(board)) == 1:
            return (None,0)
        # if red wins return 30 meaning black loses, and will have many pieces if take that move
        if nopossibleMoves(board, 'Red',validRed(board) ) == 1:
            return (None,30)
        else:
            #else take the move that will make black have less pieces, than the total pieces
            # eg if black initial has 30 pieces in 12x12 board, then calling the minmax predicts that taking the second move will resulting in having 
            # 26 pieces if red plays optimally then take that move 
            return (None,howmanyleft(board, 'Black'))
    
        
    # black player
    if isMaximizing:
        currentPossibleMovesB = validBlack(board)
        MaxEval = 30
        bestMoveB = random.choice(currentPossibleMovesB)
        
        for eachMove in currentPossibleMovesB:
            #make the virtualMove
            VirtualMove(board, 'Black', eachMove)
            # calling red player 
            eval = minimax(board, depth - 1, False)[1]
            if MaxEval > eval:     
                MaxEval = eval
                bestMoveB = eachMove
        return bestMoveB, MaxEval
         
            
     #red player        
    else:
        currentPossibleMoves = validRed(board)
        MinEval = 0
        bestMoveR = random.choice(currentPossibleMoves)
        
        for eachMove in currentPossibleMoves:
            VirtualMove(board, 'Red', eachMove)
            #calling black player
            eval = minimax(board, depth - 1, True)[1]
            if eval > MinEval:
                MinEval = eval
                bestMoveR = eachMove
        return bestMoveR, MinEval
        

# the eval var is the value returned by the terminal states( how may pieces left)
# eg in black Maxeval = 30 for black meaning having 30 pieces u lose, so if eval(how man pieces left ) is less than 30 take that move 

#for red it's vice versa, MinEval = 0 (which is a win for black, basically saying take the move that will not return 0 pieces for black but any number above that)

    
    
    