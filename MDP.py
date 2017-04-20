
class MDP():
    def __init__(self,states,actions,start,transition,reward,end):
        self.states = states
        self.actions = actions
        self.start = start
        self.transition = transition
        self.reward = reward
        self.end = end

class State():
    def __init__(self,location,trial,session):
        self.location = location
        self.trial = trial
        self.session = session

