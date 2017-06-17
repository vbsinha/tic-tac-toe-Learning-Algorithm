import cPickle as pkl

class optimlalBot(object):
	
    def __init__(self, policy_file, player_id, random_explore_prob, board):
		self.policy = self.load_policy(policy_file)
		self.player_id = player_id
		self.random_explore_prob = random_explore_prob
		assert(self.player_id == 1 or self.player_id == 2)
		assert(self.random_explore_prob >= 0 and self.random_explore_prob <= 1)
		
    def load_policy(policy_file):
        try
            fp = open(policy_file, 'r')
        except IOError:
            print "Error loading the policy file"
            return
            
        self.policy = pkl.load(fp)
        fp.close()
