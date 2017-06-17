from tictactoe import TicTacToe

def get_coordinate():
    print "Enter the coordinates to play"
    i = input()
    j = input()
    assert(i == 0 or i == 1 or i == 2)  
    assert(j == 0 or j == 1 or j == 2) 
    return (i, j)
    
def play():    
    board = TicTacToe()
    while not board.is_game_over():
        print board
        sq = get_coordinate()
        board.play(1, sq)
        if not board.is_game_over():
            print board
            sq = get_coordinate()
            board.play(2, sq)
            
    print board
    print "Winner is player ", board.get_winner()
    
    
def play_against_computer():
    human_num = input("Enter the player number you want to be - 1/2")
    assert(human_num == 1 or human_num == 2)
    # Yet to be implemented 
    
def main():
    print "Select 1 to train 2 to play against computer and 3 for to play against each other "
    choice = input()
    
    assert(choice == 1 or choice == 2 or choice == 3)
    
    if choice == 1:
        print "Enter the number of matches to train"
        num_match = input()
        assert(type(num_match) == int)
        # train(num_match)
        
    elif choice == 2:
        play_against_computer()
        
    elif choice == 3:
        play()
   
if __name__ == "__main__":
    main()
    

