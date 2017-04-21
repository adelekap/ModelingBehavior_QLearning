import MDP
import sys

"""
Main Module for Modeling W-Maze MDP with Q Learning
"""

args = sys.argv[1:]

def parseArgs(cl):
    args = {}
    for n in range(len(cl)):
        if cl[n] == '-h':
            print ""   #### NEED TO HAVE HELP STATEMENTS
            sys.exit()
        if cl[n] == '-r': #living reward
            args['r'] = cl[n+1]
        if cl[n] == '-i': #iterations
            args['i'] = cl[n+1]
        if cl[n] == '-d': #discount
            args['d'] = cl[n+1]
        if cl[n] == '-e': #epsilon
            args['e'] = cl[n+1]
        if cl[n] == '-a': #alpha
            args['a'] == cl[n+1]
    return args

livingReward = parseArgs(args)['r']
session = MDP.WMazeMDP(livingReward)

