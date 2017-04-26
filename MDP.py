
class WMazeMDP():
    def __init__(self,noReward):
        self.actions = ['go_to_f1','go_to_f2','go_to_f3']
        self.penalty = noReward


    def nextState(self,state,action):
        newreward = state.cumReward + self.penalty
        if state.location == 'f1':
            if action == 'go_to_f2':
                return State('f2',state.trial + 1,state.correctOutbound,state.correctInbound+1,state,newreward+1)
            if action == 'go_to_f3':
                return State('f3',state.trial+1,state.correctOutbound,state.correctInbound,state,newreward)
        if state.location == 'f2':
            if action == 'go_to_f3':
                st = State('f3',state.trial+1,state.correctOutbound+1,state.correctInbound,state,newreward+1)
                if self.reward(st) == 1:
                    return st
                else:
                    return State('f3',state.trial+1,state.correctOutbound,state.correctInbound,state,newreward)
            if action == 'go_to_f1':
                st = State('f1',state.trial+1,state.correctOutbound+1,state.correctInbound,state,newreward+1)
                if self.reward(st) == 1:
                    return st
                else:
                    return State('f1',state.trial+1,state.correctOutbound,state.correctInbound,state,newreward)
        if state.location == 'f3':
            if action == 'go_to_f1':
                return State('f1',state.trial+1,state.correctOutbound,state.correctInbound,state,newreward)
            if action == 'go_to_f2':
                return State('f2',state.trial+1,state.correctOutbound,state.correctInbound+1,state,newreward+1)

    def transitionProb(self,state,action,newState):
        """
        This returns P(s'|s,a).
        If the agent goes to a certain feeder (a) and they end up at that feeder (s'), as long
        as they did not come from that feeder (s), the probability is 1.
        """
        if state.location == 'f1':
            if action == 'go_to_f2' and newState.location == 'f2' and newState.trial == state.trial+1:
                return 1
            if action == 'go_to_f3' and newState.location == 'f3' and newState.trial == state.trial+1:
                return 1
            else:
                return 0
        if state.location == 'f2':
            if action == 'go_to_f3' and newState.location == 'f3' and newState.trial == state.trial+1:
                return 1
            if action == 'go_to_f1' and newState.location == 'f1' and newState.trial == state.trial+1:
                return 1
            else:
                return 0
        if state.location == 'f3':
            if action == 'go_to_f1' and newState.location == 'f1' and newState.trial == state.trial+1:
                return 1
            if action == 'go_to_f2' and newState.location == 'f2' and newState.trial == state.trial+1:
                return 1
            else:
                return 0

    def reward(self,state):
        """
        This is the reward function. It returns the reward the agent experiences when in that state.
        The agent receives a reward if they visit a correct feeder in the sequence,
        otherwise they receive a negative timestep reward (self.penalty).
        """
        if state.previousState.previousState == None:
            return 1
        if state.location == 'f2' and (state.previousState.location == 'f1' or state.previousState.location == 'f3'):
            return 1

        if state.location == 'f3' and state.previousState.location == 'f2' and state.previousState.previousState.location == 'f1':
            return 1

        if state.location == 'f1' and state.previousState.location == 'f2' and state.previousState.previousState.location == 'f3':
            return 1

        else:
            return self.penalty

    def termination(self,state):
        """
        This returns whether or not the agent is in a terminal state.
        The only termination state is when the agent reaches 30 correct outbound decisions.
        """
        return state.correctOutbound == 5

class State():
    def __init__(self,location,trial,correctOutbound,correctInbound,previousState,cumReward):
        self.location = location
        self.trial = trial
        self.correctInbound = correctInbound
        self.correctOutbound = correctOutbound
        self.previousState = previousState
        self.cumReward = cumReward



