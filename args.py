import sys

def parseArgs(cl):
    args = {'r':-1,'e':'greedy0.1','a':'constant0.5','i':15,'d':'constant0.7','p':'polynomial'}
    for n in range(len(cl)):
        if cl[n] == '-h':
            print ""   #### NEED TO HAVE HELP STATEMENTS
            sys.exit()
        if cl[n] == '-r': #living reward
            args['r'] = float(cl[n+1])
        if cl[n] == '-i': #iterations
            args['i'] = int(cl[n+1])
        if cl[n] == '-dConstant': #discount
            args['d'] = 'constant' + cl[n+1]
        if cl[n] == '-dLinear':
            args['d'] = 'linear'
        if cl[n] == '-dQuick':
            args['d'] = 'quick'
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
        if cl[n] == '-aConstant': #alpha
            args['a'] = 'constant'+cl[n+1]
        if cl[n] == '-aLinear':
            args['a'] = 'linear'
        if cl[n] == '-aExponential':
            args['a'] = 'exponential'
        if cl[n] == '-movAvg':
            args['p'] = 'movAvg'

    return args


def eps(parameters):
    if parameters['e'] == 'linear':
        eps = 'Decreasing Linearly'
    if parameters['e'] == 'exponential':
        eps = 'Decreasing Exponentially'
    if parameters['e'] == 'softmax':
        eps = 'Softmax'
    if parameters['e'] == 'glie':
        eps = 'GLIE'
    else:
        eps = '{0} {1}'.format(parameters['e'][0:6], parameters['e'][6:])
    return eps

def alp(parameters):
    if 'constant' in parameters['a']:
        alp = parameters['a'][8:]
    if parameters['a'] == 'linear':
        alp = 'Decreasing Linearly'
    if parameters['a'] == 'exponential':
        alp = 'Decreasing Exponentially'
    return alp

def dis(parameters):
    if parameters['d'] == 'linear':
        dis = 'Decreasing Linearly'
    if parameters['d'] == 'quick':
        dis = 'Decreasing x/(x+1)'
    if 'constant' in parameters['d']:
        dis = parameters['d'][8:]
    return dis