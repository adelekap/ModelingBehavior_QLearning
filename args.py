import sys

def parseArgs(cl):
    args = {'r':-1,'e':'greedy0.1','a':'constant0.5','i':15,'d':'constant0.7','p':'movAvg'}
    for n in range(len(cl)):
        if cl[n] == '-h':
            print ""
            sys.exit()
        ### ITERATIONS ###################
        if cl[n] == '-i':
            args['i'] = int(cl[n+1])
        ### GAMMA / DISCOUNT #############
        if cl[n] == '-dConstant':
            args['d'] = 'constant' + cl[n+1]
        if cl[n] == '-dLinear':
            args['d'] = 'linear'
        if cl[n] == '-dQuick':
            args['d'] = 'quick'
        ### EPSILON ######################
        if cl[n] == '-eGreedy':
            args['e'] = 'greedy'+cl[n+1]
        if cl[n] == '-eLinear':
            args['e'] = 'linear'
        if cl[n] == '-eExponential':
            args['e'] = 'exponential'
        if cl[n] == '-eSoftmax':
            args['e'] = 'softmax'
        if cl[n] == '-eGlie':
            args['e'] = 'glie'
        ### ALPHA #########################
        if cl[n] == '-aConstant':
            args['a'] = 'constant'+cl[n+1]
        if cl[n] == '-aLinear':
            args['a'] = 'linear'
        if cl[n] == '-aExponential':
            args['a'] = 'exponential'
        ### PLOT OPTION ###################
        if cl[n] == '-movAvg':
            args['p'] = 'movAvg'
        if cl[n] == '-polynomial':
            args['p'] = 'polynomial'

    return args


def eps(parameters):
    if parameters['e'] == 'linear':
        return '-Linear'
    if parameters['e'] == 'exponential':
        return '-Exponential'
    if parameters['e'] == 'softmax':
        return 'Softmax'
    if parameters['e'] == 'glie':
        return 'GLIE'
    else:
        return parameters['e'][6:]

def alp(parameters):
    if 'constant' in parameters['a']:
        return parameters['a'][8:]
    if parameters['a'] == 'linear':
        return '-Linear'
    if parameters['a'] == 'exponential':
        return '-Exponential'

def dis(parameters):
    if parameters['d'] == 'linear':
        return '-Linear'
    if parameters['d'] == 'quick':
        return 'x/(x+1)'
    if 'constant' in parameters['d']:
        return parameters['d'][8:]