"""
Theses are the learning functions that your
agent can utilize.
"""

def constant(agent,state):
    return agent.alpha



def decreasingLinear(agent,state):
    return (1/(agent.episodesSoFar+state.trial))



def decreasingExponential(agent,state):
    return(0.5**(agent.episodesSoFar+state.trial))