"""
This module contains information about how states are representated
 as well as defines the Markov Decision Process.
"""


class State():
    def __init__(self,location,trial,correctOutbound,correctInbound,previousState,cumReward):
        self.location = location
        self.trial = trial
        self.correctInbound = correctInbound
        self.correctOutbound = correctOutbound
        self.previousState = previousState
        self.cumReward = cumReward

startState = State('f2',1,0,0,None,0)  # The start state is always the same regardless of the episode

class WMazeMDP():
    def __init__(self,noReward=-1,state=startState):
        self.actions = ['go_to_f1','go_to_f2','go_to_f3']
        self.penalty = noReward
        self.state = state

    def nextState(self,state,action):
        """
        Returns what the next state will be given some state and an action.
        """
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

    def reward(self,state,animalData=None,action=None):
        """
        This is the reward function. It returns the reward the agent experiences when in that state.
        The agent receives a reward if they visit a correct feeder in the sequence,
        otherwise they receive a negative timestep reward (self.penalty).
        """

        if state.previousState.previousState == None:
            return 1

        distant = state.previousState.previousState.location
        past = state.previousState.location
        current = state.location

        if current == 'f2' and (past == 'f1' or past == 'f3'):
            if state.previousState.previousState.previousState == None:
                return 1
            farfar = state.previousState.previousState.previousState.location
            if (farfar == past):
                return -1
            else:
                return 1

        if current == 'f3' and past == 'f2' and distant == 'f1':
            return 1

        if current == 'f1' and past == 'f2' and distant == 'f3':
            return 1

        else:
            return self.penalty

    def termination(self,state,trials=None):
        """
        This returns whether or not the agent is in a terminal state.
        The only termination state is when the agent reaches 30 correct outbound decisions.
        """
        return state.correctOutbound == 30

    def reset(self):
        """
        This resets the state back to its original settings at the
        start of an episode.
        """
        self.state = startState





