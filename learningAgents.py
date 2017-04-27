"""
This module is a modified version of learningAgents.py from Project 4 in UA's INFO 550 course:
http://w3.sista.arizona.edu/~clayton/courses/ai/projects/reinforcement/reinforcement.html
"""



class ReinforcementAgent():
    """
      Abstract Reinforcemnt Agent: A ValueEstimationAgent
        which estimates Q-Values (as well as policies) from experience
        rather than a model
        What you need to know:
            - The environment will call
              observeTransition(state,action,nextState,deltaReward),
              which will call update(state, action, nextState, deltaReward)
              which you should override.
        - Use self.getLegalActions(state) to know which actions
              are available in a state
    """



    def observeTransition(self, state, action, nextState, deltaReward):
        """
            Called by environment to inform agent that a transition has
            been observed. This will result in a call to self.update
            on the same arguments
            NOTE: Do *not* override or call this function
        """
        self.episodeRewards += deltaReward
        self.update(state, action, nextState, deltaReward)

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

    def __init__(self, alpha=1.0, epsilon=0.05, gamma=0.8, numTraining=10):
        """
        Sets options, which can be passed in via the Pacman command line using -a alpha=0.5,...
        alpha    - learning rate
        epsilon  - exploration rate
        gamma    - discount factor
        numTraining - number of training episodes, i.e. no learning after these many episodes
        """
        self.numTraining = int(numTraining)
        self.episodesSoFar = 0
        self.accumTrainRewards = 0.0
        self.accumTestRewards = 0.0
        self.numTraining = int(numTraining)
        self.epsilon = float(epsilon)
        self.alpha = float(alpha)
        self.discount = float(gamma)
