
class WMazeMDP():
    def __init__(self):
        self.states = self.states()
        self.actions = ['go_to_f1','go_to_f2','go_to_f3']
        self.start = 'f2'

    def states(self):
        feeders = ['f1','f2','f3']
        trials = range(1,1501)
        allStates = [(feeder,trial) for feeder in feeders for trial in trials]
        return allStates

    def transitionProb(self,state,action,newState):
        if state[0] == 'f1':
            if action == 'go_to_f2' and newState == ('f2',state[1]+1):
                return 1
            if action == 'go_to_f3' and newState == ('f3',state[1]+1):
                return 1
            else:
                return 0
        if state[0] == 'f2':
            if action == 'go_to_f3' and newState == ('f3',state[1]+1):
                return 1
            if action == 'go_to_f1' and newState == ('f1',state[1]+1):
                return 1
            else:
                return 0
        if state[0] == 'f3':
            if action == 'go_to_f1' and newState == ('f1',state[1]+1):
                return 1
            if action == 'go_to_f2' and newState == ('f2',state[1]+1):
                return 1
            else:
                return 0

    def reward(self):
        pass

    def termination(self):
        pass



