import util
import random
import MDP


class ratAgent():
    def __init__(self, mdp, epsilon, alpha, discount =0.8):
        self.mdp = mdp
        self.discount = discount
        self.QValues = util.Counter()
        self.epsilon = epsilon
        self.alpha = alpha

    def legalActions(self,state):
        if state.location == 'f1':
            return ['go_to_f2','go_to_f3']
        if state.location == 'f2':
            return ['go_to_f3','go_to_f1']
        if state.location == 'f3':
            return ['go_to_f1','go_to_f2']

    def getQValue(self,state,action):
        """
        Returns the most recently updated q value
        """

        if state.previousState == None:
            if (None,state.location,action,action[6:8]) not in self.QValues: return 0
            return self.QValues[(None,state.location,action,action[6:8])]
        else:
            if (state.previousState.location,state.location,action,action[6:8]) not in self.QValues: return 0
            return self.QValues[(state.previousState.location,state.location,action,action[6:8])]

    def getValue(self,state):
        """
        Returns V - the max action value over all legal actions
        """
        legalActions = self.legalActions(state)
        if len(legalActions) == 0:
            return 0.0
        values = [self.getQValue(state,action) for action in legalActions]

        return max(values)

    def getPolicy(self,state,legalActions):
        """
        Returns the best action to take in a given state
        """
        Qs = util.Counter()
        for action in legalActions:
            Qs[action] = self.getQValue(state,action)

        maxVal = Qs[Qs.argMax()]
        actions = [action for action in legalActions if Qs[action] == maxVal]
        return random.choice(actions)

    def getAction(self,state):
        """
        Computes the action to take in the current state, taking into account
        the exploration probability
        """
        legalActions = self.legalActions(state)
        action = None
        explorationProb = self.epsilon

        if len(legalActions) != 0:
            if util.flipCoin(explorationProb):
                action = random.choice(legalActions)
            else:
                action = self.getPolicy(state,legalActions)
        return action

    def update(self,mdp,state,action,reward):
        """
        Observes a (s,a,s',r) and updates Q-Value.
        """
        nextState = mdp.nextState(state,action)

        if state.previousState == None:
            self.QValues[(None,state.location,action,nextState.location)] = self.getQValue(state, action) + (
                self.alpha * (reward + (self.discount * self.getValue(nextState)) - self.getQValue(state, action)))
        else:
            self.QValues[(state.previousState.location, state.location,action,nextState.location)] = self.getQValue(state, action) + \
                                                                                                     (self.alpha * (reward + (self.discount * self.getValue(nextState)) - self.getQValue(state, action)))

