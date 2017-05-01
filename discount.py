"""
Functions for discount factor.
"""

def constant(agent,state):
    """
    Returns the discount constant (either specified by
    user or default)
    """
    return agent.discount[8:]


def increasingLinear(agent,state):
    """
    Increases discount linearly with time
    """
    print (1.0 - (1.0 / (agent.episodesSoFar + state.trial)))
    return (1.0 - (1.0 / (agent.episodesSoFar + state.trial)))


def increasingQuickly(agent,state):
    """
    Increases by function (x/(1+x))
    """
    x = agent.episodesSoFar + state.trial
    return x/(1.0+x)
