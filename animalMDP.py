"""
This module contains information about how states are representated
 as well as defines the Markov Decision Process for learned to act like
 an animal in this task.
"""
import MDP
from MDP import State

class animalMDP(MDP.WMazeMDP):

    def __init__(self,ratData):
        self.ratData = ratData
        MDP.WMazeMDP.__init__(self)

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
                if self.reward(st,self.ratData) == 1:
                    return st
                else:
                    return State('f3',state.trial+1,state.correctOutbound,state.correctInbound,state,newreward)
            if action == 'go_to_f1':
                st = State('f1',state.trial+1,state.correctOutbound+1,state.correctInbound,state,newreward+1)
                if self.reward(st,self.ratData) == 1:
                    return st
                else:
                    return State('f1',state.trial+1,state.correctOutbound,state.correctInbound,state,newreward)
        if state.location == 'f3':
            if action == 'go_to_f1':
                return State('f1',state.trial+1,state.correctOutbound,state.correctInbound,state,newreward)
            if action == 'go_to_f2':
                return State('f2',state.trial+1,state.correctOutbound,state.correctInbound+1,state,newreward+1)

    def reward(self,state,animalData):
        """
        This is the reward function. It returns the reward the agent experiences when in that state.
        The agent receives a reward if they visit the same feeder as the animal given in the arguments.
        """
        trialIndex = state.trial - 1
        if len(animalData) <= trialIndex:
            print 'o'
        if state.previousState.previousState == None:
            return 1

        distant = state.previousState.previousState.location
        past = state.previousState.location
        current = state.location

        if current == 'f2' and (past == 'f1' or past == 'f3'):
            if state.previousState.previousState.previousState == None:
                if animalData[trialIndex] == 1:
                    return 1
                else: return -1
            farfar = state.previousState.previousState.previousState.location
            if (farfar == past):
                if animalData[trialIndex] == 0:
                    return -1
                else:
                    return 1

        if current == 'f3' and past == 'f2' and distant == 'f1':
            if animalData[trialIndex] == 1:
                return 1
            else:
                return -1

        if current == 'f1' and past == 'f2' and distant == 'f3':
            if animalData[trialIndex] == 1:
                return 1
            else:
                return -1
        return -1






