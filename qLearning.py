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

parameters = parseArgs(sys.argv[1:])
session = MDP.WMazeMDP(parameters['r'])
rat = agent.ratAgent(session,parameters['e'],parameters['a'])
startState= MDP.State('f2',1,0,0,None,0)
iterations = parameters['i']


def testRat(rat,state,sess,trial,sessionNum):
    if sess.termination(state):
        return state
    action = rat.getAction(state)
    newState = sess.nextState(state,action)
    rat.update(sess,state,action,sess.reward(newState))
    finalstate = testRat(rat,newState,sess,trial+1,sessionNum)
    return finalstate

def testing(rat,sessionNum,start):
    performance = testRat(rat, start, session, 1, sessionNum)

    if sessionNum == iterations:
        print 'Session {0} Performance:{1}%'.format(sessionNum, ((float(performance.correctOutbound) +
                                                                  float(performance.correctInbound)) /
                                                                 float(performance.trial)) * 100)
    else:
        print 'Session {0} Performance:{1}%'.format(sessionNum, ((float(performance.correctOutbound) +
                                                                  float(performance.correctInbound)) /
                                                                 float(performance.trial)) * 100)
        testing(rat,sessionNum+1,MDP.State('f2',1,0,0,None,performance.cumReward))



testing(rat,1,startState)