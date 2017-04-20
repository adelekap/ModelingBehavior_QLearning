
class WMazeMDP():
    def __init__(self,noReward):
        self.states = self.states()
        self.actions = ['go_to_f1','go_to_f2','go_to_f3']
        self.start = 'f2'
        self.penalty = noReward

    def states(self):
        feeders = ['f1','f2','f3']
        trials = range(1,1501)
        correctNums = range(0,31)
        allStates = [State(feeder,trial,correct) for feeder in feeders for trial in trials for correct in correctNums]
        return allStates

    def transitionProb(self,state,action,newState):
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
        #The agent recevies a reward if they visit a correct feeder in the sequence, otherwise
        #they receive a negative timestep reward
        if state.location == 'f2' and (state.previousState.location == 'f1' or state.previousState.location == 'f3'):
            return 1

        if state.location == 'f3' and state.previousState.location == 'f2' and state.previousState.previousState.location == 'f1':
            return 1

        if state.location == 'f1' and state.previousState.location == 'f2' and state.previousState.previousState.location == 'f3':
            return 1

        else:
            return self.penalty

    def termination(self,state):
        #The only termination state is when the agent reaches 30 correct outbound decisions
        return state.correctOutbound == 30

class State():
    def __init__(self,location,trial,correctOutbound):
        self.location = location
        self.trial = trial
        self.correctOutbound = correctOutbound
        self.previousState



