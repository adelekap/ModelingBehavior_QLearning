import MDP
import sys
import agent

"""
Main Module for Modeling W-Maze MDP with Q Learning
"""

args = sys.argv[1:]

def parseArgs(cl):
    args = {'r':-0.01,'e':0.25,'a':0.4,'i':20}
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

experience ={}

def testRat(rat,state,sess,trial):
    if state.correctOutbound == 30:
        print 'Performance:{0}%'.format(((float(state.correctOutbound)+float(state.correctInbound))/float(trial))*100)
        return state
    experience[trial] = state
    action = rat.getAction(state)
    newState = sess.nextState(state,action)
    testRat(rat,newState,sess,trial+1)




testRat(rat,startState,session,1)