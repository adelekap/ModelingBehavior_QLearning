import MDP
import sys
import agent
import plotLearning as learn
import exploration as explore

"""
Main Module for Modeling W-Maze MDP with Q Learning
"""

args = sys.argv[1:]

def parseArgs(cl):
    args = {'r':-1,'e':0.1,'a':0.75,'i':20}
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
        if cl[n] == '-eGreedy':
            args['e'] = 'greedy'+cl[n+1]
        if cl[n] == '-eDecreasing':
            args['e'] = 'decreasing'
        if cl[n] == '-eSoftmax':
            args['e'] = 'softmax'
        if cl[n] == '-eGlie':
            args['e'] = 'glie'
        if cl[n] == '-aConstant': #alpha
            args['a'] = 'constant'+cl[n+1]
        if cl[n] == '-aLinear':
            args['a'] = 'linear'
        if cl[n] == '-aExponential':
            args['a'] = 'exponential'

    return args


def testRat(rat,state,sess,trial,sessionNum):
    if sess.termination(state):
        return state
    action = rat.getAction(state,rat)
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
        action = agent.getAction(state,agent)

        # END IF IN A TERMINAL STATE
        actions = agent.legalActions(state)
        if len(actions) == 0:
            print("EPISODE " + str(episode) + " COMPLETE: RETURN WAS " + str(returns) + "\n")
            f.write('1')
            rat.accumTrainRewards=returns
            return returns

        # GET ACTION (USUALLY FROM AGENT)
        if action == None:
            raise 'Error: Agent returned None action'

        # EXECUTE ACTION
        nextState = environment.nextState(state,action)
        reward = environment.reward(nextState)

        if reward == 1:
            f.write('1,')
        else:
            f.write('0,')

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
    fi.write('0,')

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

if parameters['e'] == 'decreasing':
    eps = 'Decreasing Linearly'
if parameters['e'] == 'softmax':
    eps = 'Softmax'
if parameters['e'] == 'glie':
    eps = 'GLIE'
else:
    eps = '{0} {1}'.format(parameters['e'][0:6],parameters['e'][6:])

if 'constant' in parameters['a']:
    alp = parameters['a'][8:]
if parameters['a'] == 'linear':
    alp = 'Decreasing Linearly'
if parameters['a'] == 'exponential':
    alp = 'Decreasing Exponentially'
learn.plot(alp,eps)