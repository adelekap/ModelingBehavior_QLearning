import util
import random
import exploration as explore
import learning
import discount


class ratAgent():
    def __init__(self, mdp, epsilon, alpha, discount ,numTraining = 14):
        self.mdp = mdp
        self.discount = discount
        self.QValues = util.Counter()
        self.epsilon = epsilon
        self.alpha = alpha
        self.numTraining = int(numTraining)
        self.episodesSoFar = 0
        self.accumTrainRewards = 0.0
        self.accumTestRewards = 0.0

    def legalActions(self,state):
        """
        Returns all the possible legal actions the agent
        can take in a particular state.
        """
        # if state.correctOutbound == 30:
        #     return []
        if state.location == 'f1':
            return ['go_to_f2','go_to_f3']
        if state.location == 'f2':
            return ['go_to_f3','go_to_f1']
        if state.location == 'f3':
            return ['go_to_f1','go_to_f2']


    def getQValue(self,state,newLoc):
        """
        Returns the most recently updated q value
        """

        if state.previousState == None:
            if (None,state.location,newLoc) not in self.QValues: return 0
            return self.QValues[(None,state.location,newLoc)]
        else:
            if (state.previousState.location,state.location,newLoc) not in self.QValues: return 0
            return self.QValues[(state.previousState.location,state.location,newLoc)]


    def getValue(self,state):
        """
        Returns V - the max action value over all legal actions
        """
        legalActions = self.legalActions(state)
        if len(legalActions) == 0:
            return 0.0
        values = [self.getQValue(state,action[6:8]) for action in legalActions]

        return max(values)


    def getPolicy(self,state,legalActions,softmax=False,agent=None):
        """
        Returns the best action to take in a given state
        """
        if softmax:
            return explore.softmax(agent,state)

        Qs = util.Counter()

        for action in legalActions:
            Qs[action] = self.getQValue(state,action[6:8])

        maxVal = Qs[Qs.argMax()]
        actions = [action for action in legalActions if Qs[action] == maxVal]
        return random.choice(actions)


    def getAction(self,state,agent):
        """
        Computes the action to take in the current state, taking into account
        the exploration probability (or function)
        """
        legalActions = self.legalActions(state)
        action = None
        explorationProb = self.explorationProb(agent,state)


        if len(legalActions) != 0:
            if self.epsilon == 'softmax':
                action = self.getPolicy(state,legalActions,True,agent)
                return action
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

        current = state.location
        next = nextState.location
        alpha = float(self.getAlpha(self,state))
        discount = self.getGamma(self,state)

        if state.previousState == None:
            self.QValues[(None,current,next)] = self.getQValue(state, next) + (
                alpha * (reward + (discount * self.getValue(nextState)) - self.getQValue(state, next)))

        else:
            previous = state.previousState.location
            self.QValues[(previous,current,next)] = ((1-alpha)*self.getQValue(state,nextState.location))+ \
                                                    alpha*(reward+discount*self.getValue(nextState))
        mdp.state = state


    def observeTransition(self, environment,state, action, deltaReward):
        self.episodeRewards += deltaReward
        self.update(environment,state,action,deltaReward)


    def startEpisode(self):
        """
          Called by environment when new episode is starting
        """
        self.lastState = None
        self.lastAction = None
        self.episodeRewards = 0.0


    def stopEpisode(self):
        """
          Called by environment when episode is done
        """
        if self.episodesSoFar < self.numTraining:
            self.accumTrainRewards += self.episodeRewards
        else:
            self.accumTestRewards += self.episodeRewards
        self.episodesSoFar += 1
        if self.episodesSoFar >= self.numTraining:
            # Take off the training wheels
            self.epsilon = 0.0  # no exploration
            self.alpha = 0.0  # no learning


    def isInTraining(self):
        return self.episodesSoFar < self.numTraining


    def isInTesting(self):
        return not self.isInTraining()


    def explorationProb(self,agent,state):
        """
        Returns the epsilon value at the time step.
        """
        if self.epsilon == 'linear':
            return explore.decreasingE(agent,state)
        if self.epsilon == 'exponential':
            return explore.decExponential(agent,state)
        if self.epsilon == 'glie':
            return explore.GLIE(agent,state)
        else: return explore.greedyE(agent,state)


    def getAlpha(self,agent,state):
        """
        Returns the alpha value at that time step.
        """
        if self.alpha == 'linear':
            return learning.decreasingLinear(agent,state)
        if self.alpha == 'exponential':
            return learning.decreasingExponential(agent,state)
        if 'constant' in self.alpha:
            return learning.constant(agent,state)


    def getGamma(self,agent,state):
        """
        Returns the gamma (discount) value at that time step.
        """
        if self.discount == 'linear':
            return discount.increasingLinear(agent,state)
        if self.discount == 'quick':
            return discount.increasingQuickly(agent,state)
        if 'constant' in self.discount:
            return float(discount.constant(agent,state))