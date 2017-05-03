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
                if self.reward(st,self.ratData,action) == 1:
                    return st
                else:
                    return State('f3',state.trial+1,state.correctOutbound,state.correctInbound,state,newreward)
            if action == 'go_to_f1':
                st = State('f1',state.trial+1,state.correctOutbound+1,state.correctInbound,state,newreward+1)
                if self.reward(st,self.ratData,action) == 1:
                    return st
                else:
                    return State('f1',state.trial+1,state.correctOutbound,state.correctInbound,state,newreward)
        if state.location == 'f3':
            if action == 'go_to_f1':
                return State('f1',state.trial+1,state.correctOutbound,state.correctInbound,state,newreward)
            if action == 'go_to_f2':
                return State('f2',state.trial+1,state.correctOutbound,state.correctInbound+1,state,newreward+1)

    def reward(self,state,animalData,action):
        """
        This is the reward function. It returns the reward the agent experiences when in that state.
        The agent receives a reward if they visit the same feeder as the animal given in the arguments.
        """
        trialIndex = state.trial - 1
        feeder = action[7]

        if feeder == '1' and animalData[trialIndex] == 1:
            return 1
        if feeder == '2' and animalData[trialIndex] == 2:
            return 1
        if feeder == '3' and animalData[trialIndex] == 3:
            return 1
        return -1






