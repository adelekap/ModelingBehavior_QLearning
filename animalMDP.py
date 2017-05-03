"""
This module contains information about how states are representated
 as well as defines the Markov Decision Process for learned to act like
 an animal in this task.
"""
import MDP


class animalMDP(MDP.WMazeMDP):


    def rewardFunction(self,state,animalData):
        """
        This is the reward function. It returns the reward the agent experiences when in that state.
        The agent receives a reward if they visit the same feeder as the animal given in the arguments.
        """
        trialIndex = state.trial - 1
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







