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

