import cPickle as pkl
import random

class OptimalBot(object):
	
    def __init__(self, policy_file, player_id, board, random_explore_prob=0.1, reward={'W' : 10, 'L' : -10, 'D' : -2}):
		self.policy_file = policy_file
		self.player_id = player_id
		self.game = board
		self.random_explore_prob = random_explore_prob
		self.moves = []
		self.reward = reward
		assert(self.player_id == 1 or self.player_id == 2)
		assert(self.random_explore_prob >= 0 and self.random_explore_prob <= 1)
		
    def load_policy(self, policy_file):
        try:
            # print policy_file
            fp = open(policy_file, 'r')
        except IOError:
            print "Error loading the policy file"
            return
            
        policy = pkl.load(fp)
        fp.close()
        
        return policy
        
    def play(self, train=False):
        status = self.get_current_status()
        playable_squares = self.game.get_playable_squares()
        policy = self.load_policy(self.policy_file)
        
        # print policy
        
        if((random.random() <= self.random_explore_prob and train == True) or (policy is not None and status not in policy) or (train == True and status in policy and all(value <=0 for value in policy[status].values()))):
            move = playable_squares[random.randrange(0, len(playable_squares))]
            
        else:
            known_moves = policy[status]
            move = max(known_moves, key=known_moves.get)
        
        self.game.play(self.player_id, move)
        self.moves.append((status,move))
        
    def update(self):
        position = self.get_position(self.game.get_winner())
        reward_points = self.reward[position]
        policy = self.load_policy(self.policy_file)
        
        for move in self.moves:
            status = move[0]
            action = move[1]
            if status in policy:
                if action in policy[status]:
                    old_reward = policy[status][action]
                    policy[status].pop(policy[status][action], None)
                else:
                    old_reward = 0            
            else:
                old_reward = 0
                policy[status] = {}
        
            final_reward = old_reward + 0.9 * (reward_points - old_reward) # Implement ??
        
            policy[status][action] = final_reward
        
        fp = open(self.policy_file, 'w')
        pkl.dump(policy, fp)
        fp.close()    
        self.moves = []    
        
    def get_position(self, winner):
        if winner == self.player_id:
            return 'W'
        elif winner == 0:
            return 'D'
        else:
            return 'L'        
        
    def get_current_status(self):
        status = ""
        for i in self.game.get_board():
            for j in i:
                status += str(j)
        return status
