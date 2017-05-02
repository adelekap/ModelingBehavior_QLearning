import sys

def parseArgs(cl):
    args = {'r':-1,'e':'greedy0.1','a':'constant0.5','i':15,'d':'constant0.7','p':'movAvg'}
    for n in range(len(cl)):
        if cl[n] == '-h':
            print ""   #### NEED TO HAVE HELP STATEMENTS
            sys.exit()
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
        if cl[n] == '-polynomial':
            args['p'] = 'polynomial'

    return args


def eps(parameters):
    if parameters['e'] == 'linear':
        return 'Decreasing Linearly'
    if parameters['e'] == 'exponential':
        return 'Decreasing Exponentially'
    if parameters['e'] == 'softmax':
        return 'Softmax'
    if parameters['e'] == 'glie':
        return 'GLIE'
    else:
        return '{0} {1}'.format(parameters['e'][0:6], parameters['e'][6:])

def alp(parameters):
    if 'constant' in parameters['a']:
        return parameters['a'][8:]
    if parameters['a'] == 'linear':
        return 'Decreasing Linearly'
    if parameters['a'] == 'exponential':
        return 'Decreasing Exponentially'

def dis(parameters):
    if parameters['d'] == 'linear':
        return 'Decreasing Linearly'
    if parameters['d'] == 'quick':
        return 'Decreasing x/(x+1)'
    if 'constant' in parameters['d']:
        return parameters['d'][8:]