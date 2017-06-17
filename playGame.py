from tictactoe import TicTacToe
from computer_play import ComputerPlayer

def input_coordinate():
    print "Enter the coordinates to play"
    i = input()
    j = input()
    assert(i == 0 or i == 1 or i == 2)  
    assert(j == 0 or j == 1 or j == 2) 
    return (i, j)
    
def human2human_play():    
    board = TicTacToe()
    while not board.is_game_over():
        print board
        sq = input_coordinate()
        board.play(1, sq)
        if not board.is_game_over():
            print board
            sq = input_coordinate()
            board.play(2, sq)
            
    print board
    print "Winner is player ", board.get_winner()
    
def humancomputer_play(computer):
	board = TicTacToe()
    while not board.is_game_over():
        print board
        if (computer.get_id() == 1):
        	sq = computer.play(board)
        else:
        	sq = input_coordinate()
        board.play(1, sq)
        if not board.is_game_over():
            print board
            if (computer.get_id() == 2):
        		sq = computer.play(board)
       	 	else:
        		sq = input_coordinate()
            board.play(2, sq)
            
    print board
    print "Winner is player ", board.get_winner()
    
    
def play_against_computer():
    human_num = input("Enter the player number you want to be - 1/2")
    assert(human_num == 1 or human_num == 2)
    if human_num == 1:
    	computer_num == 2
    else:
    	computer_num == 3
    file_path = input("Enter the path of the file containing the computer's data : ")
    prob = input("Enter the probability of random explorations : ")
    alpha = input("Enter the value of alpha : ")
    computer_player = ComputerPlayer(file_path,computer_num,prob,alpha)
    
    # Yet to be implemented 
    
def main():
    print "Select an option:"
    print "1. Train by allowing the computer to play against itself"
    print "2. Play a game against the computer and help it learn to play you"
    print "3. Two humans play each other"
    print "4. Exit"
    choice = input()
    
    assert(choice == 1 or choice == 2 or choice == 3 or choice == 4)
    
    if choice == 1:
        print "Enter the number of matches to train"
        num_match = input()
        assert(type(num_match) == int)
        # train(num_match)
        
    elif choice == 2:
        play_against_computer()
        
    elif choice == 3:
        human2human_play()
   
if __name__ == "__main__":
    main()
    

