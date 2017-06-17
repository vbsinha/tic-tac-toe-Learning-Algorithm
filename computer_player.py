import random
import pickle
import copy

class ComputerPlayer():
	
	def __init__(self,json_file,player_id,random_explore_prob,alpha):
		self.json_file = json_file
		self.player_id = player_id
		self.random_explore_prob = random_explore_prob
		self.alpha = alpha
		assert(self.player_id == 1 or self.player_id == 2)
		assert(self.random_explore_prob >= 0 and self.random_explore_prob <= 1)
	
	def play(self,board):
		move = self.find_best_move(board)
		self.update_probs(board,move)
		return move
		
	def get_id(self):
		return self.player_id
		
	def find_best_move(self,board):
		best_move_probability = 0.5
		best_move = (-1,-1)
		wont_explore = random.randint(0,int(1./self.random_explore_prob))
		playable_moves = board.get_playable_squares()
		if wont_explore == 0:			
			move_id = random.randint(0,len(playable_moves))
			return playable_moves[move_id]
		for available_move in playable_moves:
			curr_prob = self.check_and_get_prob(board,available_move)
			if curr_prob >= best_move_probability:
				best_move_probability = curr_prob
				best_move = available_move
		return best_move
	
	def check_and_get_prob(self,board,move_candidate):
		board_copy = copy.copy(board)
		board_copy.play(player_id,move_candidate)
		prob = self.prob_of_state(board_copy)
		return prob
	
	def update_probs(self,board,move):
		board_copy = copy.copy(board)
		board_copy.play(player_id,move)
		v_s = prob_of_state(board)
		v_prime_s = prob_of_state(board_copy)
		new_v_s = v_s + self.alpha * (v_prime_s - v_s)
		self.set_prob_of_state(board,new_v_s)
				
	def prob_of_state(self,board):
		
	def set_prob_of_state(self,board,prob):
		
