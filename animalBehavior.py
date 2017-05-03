import MDP
import sys
import agent
import plotLearning as learn
import args
import animalMDP


def youngData():
    with open('rat10279.txt','r') as yngData:
        yng = yngData.readlines()
    data = [d.split(',') for d in yng][0]
    return [int(num) for num in data]

def oldData():
    with open('rat10282.txt','r') as oldData:
        old = oldData.readlines()
    data = [d.split(',') for d in old][0]
    return [int(num) for num in data]


def runEpisode(agent, environment,episode,f,animalData):
    """
    Runs a single episode and documents the behavior of the
    agent in decisions.txt.
    """
    returns = 0
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
        reward = environment.reward(nextState,animalData)

        if reward == 1:
            f.write('1,')
        else:
            f.write('0,')

        # UPDATE LEARNER
        if 'observeTransition' in dir(agent):
            agent.observeTransition(environment,state, action, reward)


        returns += reward * totalDiscount
        gamma = agent.getGamma(agent,state)
        totalDiscount *= gamma
        environment.state = nextState


######################################################
#### This runs q-learning with specified arguments####
######################################################

parameters = args.parseArgs(sys.argv[1:])
if parameters['m'] == 'old':
    data = oldData()
if parameters['m'] == 'young':
    data = youngData()
environment = animalMDP.animalMDP(data)
rat = agent.ratAgent(environment,parameters['e'],parameters['a'],parameters['d'])
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
        returns += runEpisode(rat,environment,episode,fi,data)
        rat.episodesSoFar += 1
        if iterations > 0:
            print
            print "AVERAGE RETURNS FROM START STATE: "+str((returns+0.0) / iterations)
            print
            print


######################################################
###This plots results of the agent compared to rats###
######################################################

eps = args.eps(parameters)
alp = args.alp(parameters)
dis = args.dis(parameters)


# if parameters['p'] == 'polynomial':
#     learn.plot(alp,eps,dis)
if parameters['p'] == 'movAvg':
    learn.movAvg(alp,eps,dis)