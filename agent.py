import util

class ratAgent():
    def __init__(self, mdp, discount =0.9, iterations = 100):
        self.mdp = mdp
        self.discount = discount
        self.iterations = iterations
        self.Qvalues = util.Counter()

        def legalActions(state):
            if state.location == 'f1':
                return ['f2','f3']
            if state.location == 'f2':
                return ['f3','f1']
            if state.location == 'f3':
                return ['f1','f2']

        def getQValue(self,state,action):
            """
            Returns the most recently updated q value
            """
            if (state,action) not in self.Qvalues:
                return 0.0
            return self.QValues[(state,action)]

        def getValue(self,state):
            """
            Returns V - the max action value over all legal actions
            """
