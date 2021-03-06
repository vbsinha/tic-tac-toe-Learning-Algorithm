class TicTacToe(object):

    def __init__(self):
        self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        
    def is_playable(self, square):
        return self.board[square[0]][square[1]] == 0
        
    def play(self, player, square):
        assert((player == 1 or player == 2) and self.is_playable(square))
        self.board[square[0]][square[1]] = player
        
    def is_game_over(self):
        if (self.get_winner() == 1 or self.get_winner() == 2):
        	return True
        for i in self.board:
            for j in i:
                if j == 0:
                    return False
        return True
    
    def get_board(self):
    	return self.board
    
    '''
    Returns player number of winner if any, 0 otherwise
    '''
    def get_winner(self):
    	
    	for i in self.board:
    	    if (i[0] == i[1] == i[2] and i[0] != 0):
    	        return i[0]
        
        for i in xrange(3):
            if (self.board[0][i] == self.board[1][i] == self.board[2][i] and self.board[0][i] != 0):
                return self.board[0][i]
        
        if (self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] != 0):
            return self.board[0][0]
            
        if (self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] != 0):
            return self.board[1][1]
        
        return 0
        
    def get_playable_squares(self):
        return [(i,j) for i in xrange(3) for j in xrange(3) if self.board[i][j] == 0]
    
    def __str__(self):
        return str(self.board[0]) + '\n' +\
               str(self.board[1]) + '\n' +\
               str(self.board[2]) + '\n'
                     
# if __name__ == "__main__":
#     print "Tic Tac Toe Board"
