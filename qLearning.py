import MDP
import sys
import agent

"""
Main Module for Modeling W-Maze MDP with Q Learning
"""

args = sys.argv[1:]

def parseArgs(cl):
    args = {'r':-0.01,'e':.1,'a':0.9,'i':20}
    for n in range(len(cl)):
        if cl[n] == '-h':
            print ""   #### NEED TO HAVE HELP STATEMENTS
            sys.exit()
        if cl[n] == '-r': #living reward
            args['r'] = float(cl[n+1])
        if cl[n] == '-i': #iterations
            args['i'] = int(cl[n+1])
        if cl[n] == '-d': #discount
            args['d'] = float(cl[n+1])
        if cl[n] == '-e': #epsilon
            args['e'] = float(cl[n+1])
        if cl[n] == '-a': #alpha
            args['a'] == float(cl[n+1])
    return args


def testRat(rat,state,sess,trial,sessionNum):
    if sess.termination(state):
        return state
    action = rat.getAction(state)
    newState = sess.nextState(state,action)
    rat.update(sess,state,action,sess.reward(newState))
    finalstate = testRat(rat,newState,sess,trial+1,sessionNum)
    return finalstate

def testing(rat,sessionNum,start):
    performance = testRat(rat, start, environment, 1, sessionNum)

    if sessionNum == iterations:
        print 'Session {0} Performance:{1}%'.format(sessionNum, ((float(performance.correctOutbound) +
                                                                  float(performance.correctInbound)) /
                                                                 float(performance.trial)) * 100)
    else:
        print 'Session {0} Performance:{1}%'.format(sessionNum, ((float(performance.correctOutbound) +
                                                                  float(performance.correctInbound)) /
                                                                 float(performance.trial)) * 100)
        testing(rat,sessionNum+1,MDP.State('f2',1,0,0,None,performance.cumReward))



def runEpisode(agent, environment,episode,f):
    returns = 0
    discount = agent.discount
    totalDiscount = 1.0
    environment.reset()
    if 'startEpisode' in dir(agent): agent.startEpisode()
    print("BEGINNING EPISODE: " + str(episode) + "\n")
    while True:

        state = environment.state
        action = rat.getAction(state)

        # END IF IN A TERMINAL STATE
        actions = agent.legalActions(state)
        if len(actions) == 0:
            print("EPISODE " + str(episode) + " COMPLETE: RETURN WAS " + str(returns) + "\n")
            rat.accumTrainRewards=returns
            return returns

        # GET ACTION (USUALLY FROM AGENT)
        if action == None:
            raise 'Error: Agent returned None action'

        # EXECUTE ACTION
        nextState = environment.nextState(state,action)
        reward = environment.reward(nextState)

        if reward == 1:
            f.write('1')
        else:
            f.write('0')

        # UPDATE LEARNER
        if 'observeTransition' in dir(agent):
            agent.observeTransition(environment,state, action, reward)


        returns += reward * totalDiscount
        totalDiscount *= discount
        environment.state = nextState




parameters = parseArgs(sys.argv[1:])
environment = MDP.WMazeMDP(parameters['r'])
rat = agent.ratAgent(environment,parameters['e'],parameters['a'])
startState= MDP.State('f2',1,0,0,None,0)
iterations = parameters['i']

with open('decisions.txt','w') as fi:

    #testing(rat,1,startState)

    if iterations > 0:
        print
        print "RUNNING", iterations, "EPISODES"
        print
    returns = 0
    for episode in range(1, iterations+1):
        returns += runEpisode(rat,environment,episode,fi)
        rat.episodesSoFar += 1
        if iterations > 0:
            print
            print "AVERAGE RETURNS FROM START STATE: "+str((returns+0.0) / iterations)
            print
            print