

def decreasingE(agent,state):
    """
    Implements the decreasing-epsilon method
    which starts with a relatively high exploration rate
    and then decreases with time.
    """
    episodes = float(agent.episodesSoFar)
    trials = float(state.trial)


    x = 100.0*episodes-100.0
    m = -.0005
    b = 1-.05
    return m*x+b


