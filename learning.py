"""
Theses are the learning functions that your
agent can utilize.
Returns the value of alpha.
"""

def constant(agent,state):
    return agent.alpha[8:]


def decreasingLinear(agent,state):
    return (1/(agent.episodesSoFar+state.trial))


def decreasingExponential(agent,state):
    return(0.5**(agent.episodesSoFar+state.trial))