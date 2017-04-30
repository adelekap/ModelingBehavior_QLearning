import math
import util
import random


def greedyE(agent,state):
    """
    Implements greedy-epsilon exploration
    which returns a fixed exploration probability
    that the user can specify or the default is 0.1
    """
    return 0.1


def decreasingE(agent,state):
    """
    Implements the decreasing-epsilon method
    which starts with a high exploration rate (0.95)
    and then decreases linearly with time (~0)
    """
    episodes = float(agent.episodesSoFar)
    trials = float(state.trial)

    x = 100.0*episodes+trials
    m = -.0005
    b = 1-.0499
    return m*x+b


def softmax(agent,state):
    """
    Implements softmax exploration function which
     utilizes action-selection probabilities determined
     by ranking the value-function estimates using
     the Boltzmann distribution.

     T = temperature; a high temperature causes all actions
     to be nearly equiprobable. As the temperature is reduced,
     the highest-valued actions are more likely to be chosen and,
     in the limit as T-->0, the best action is always chosen.
     The value returned by using decreasing-epsilon is used for
     the temperature.
    """
    acts = util.Counter()
    T = decreasingE(agent,state)
    legalActions = agent.legalActions(state)

    for a in legalActions:
        q = agent.getQValue(state,a[6:8])

        numerator = math.e **(q/T)
        denominator = sum([(math.e**((agent.getQValue(state,action[6:8]))/T)) for action in legalActions])
        acts[a] = numerator/denominator

    maxVal = acts[acts.argMax()]
    actions = [act for act in legalActions if acts[act] == maxVal]
    return random.choice(actions)


