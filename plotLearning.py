import matplotlib.pyplot as plt
import numpy as np


def prep_data(movAvg,ratData=None):
    """
    Calculates proportions for the trace.
    """
    if ratData:
        data = ratData
    else:
        with open('decisions.txt','r') as f:
            lines = f.readlines()
        data = [line.split(',') for line in lines][0]
    normalize = 0
    sum =0
    proportions = []
    for d in range(len(data)):
        normalize += 1
        if int(data[d]) == 11:
            sum += 2
        else:
            sum += int(data[d])
        if (normalize == movAvg) or (d == len(data)-1):
            avg = float(sum) / float(normalize)
            if avg > 1:
                proportions.append(1)
            else:
                proportions.append(float(sum)/float(normalize))
            normalize =0
            sum = 0
    return (proportions, len(data))

def raw_data():
    with open('decisions.txt','r') as f:
        lines = f.readlines()
    data = [line.split(',') for line in lines][0]
    return (data,range(1,len(data)+1))

def func(x, a, b, c):
    return a * np.exp(-b * x) + c

def rat_data():
    with open('rat10282.txt', 'r') as old:
        lines = old.readlines()
        oldDecisions = [line.split(',') for line in lines][0]
        old = [float(o) for o in oldDecisions]
    with open('rat10279.txt', 'r') as young:
        lines = young.readlines()
        youngDecisions = [line.split(',') for line in lines][0]
        young = [float(y) for y in youngDecisions]
    trials = min([len(oldDecisions),len(youngDecisions)])
    return (young[0:trials],old[0:trials])


def plot_results(proportions,trialNum,movAvg,alpha,epsilon,discount):
    """
    Plots the performance of the agent to learn the W-track spatial alternation task.
    This is a simple 3 degree polynomial fit by first performing a least squares
    polynomial fit and the second calculates the new points.
    """
    trials = range(0,trialNum,movAvg)
    figureName = 'LearningCurve.png'
    plt.figure('Learning Curve')

    #young rat
    youngY = rat_data()[0]
    youngX = trials[0:len(youngY)]
    youngZ = np.polyfit(youngX,youngY,4)
    youngf= np.poly1d(youngZ)
    newYoungX = np.linspace(youngX[0],youngX[-1],50)
    newYoungY = youngf(newYoungX)

    #old rat
    oldY = movAvg,rat_data()[1]
    oldX = trials[0:len(oldY)]
    oldZ = np.polyfit(oldX,oldY,4)
    oldf = np.poly1d(oldZ)
    newOldX = np.linspace(oldX[0],oldX[-1],50)
    newOldY = oldf(newOldX)

    # agent
    x = trials[0:len(oldY)]
    y = proportions[0:len(oldY)]
    z = np.polyfit(x, y,4)
    f = np.poly1d(z)
    new_x = np.linspace(x[0], x[-1], 50)
    new_y = f(new_x)

    agent = plt.plot(new_x,new_y,'-')
    young = plt.plot(newYoungX,newYoungY,'-')
    old = plt.plot(newOldX,newOldY,'-')
    plt.setp(agent, linewidth=3, color='purple',label='agent:\nalpha={0}\nepsilon={1}\ngamma={2}'.format(alpha,epsilon,discount))
    plt.setp(young, linewidth=3, color='green',label='young')
    plt.setp(old, linewidth=3, color='orange',label='old')
    plt.axis([1,len(oldX),0,1.1])


    plt.title('Learning Curve')
    plt.legend(loc=4)
    plt.xlabel("Cumulative Count of Trials")
    plt.ylabel("Proportion Correct")
    plt.savefig(figureName)
    plt.show()


def plot_avg(proportions,trialNum,movAvg,alpha,epsilon,discount):
    figureName = 'LearningCurveMovAvg.png'
    plt.figure('Learning Curve')

    #young
    youngY_raw = prep_data(movAvg,rat_data()[0])[0][0:1201]

    #old
    oldY_raw = prep_data(movAvg,rat_data()[1])[0][0:1201]

    #agent
    y_raw = proportions[0:len(oldY_raw)]

    minTrials = min([len(youngY_raw),len(oldY_raw),len(y_raw)])
    youngY = youngY_raw[0:minTrials]
    oldY = oldY_raw[0:minTrials]
    y = y_raw[0:minTrials]
    youngY[0] = 0.5
    oldY[0] = 0.5
    y[0] = 0.5
    trials = range(0, trialNum, movAvg)[0:len(oldY)]

    agent = plt.plot(trials, y, '-')
    young = plt.plot(trials, youngY, '-')
    old = plt.plot(trials, oldY, '-')
    plt.setp(agent, linewidth=3, color='purple',
             label='agent:(alpha={0}, epsilon={1}, gamma={2})'.format(alpha, epsilon, discount))
    plt.setp(young, linewidth=3, color='green', label='young')
    plt.setp(old, linewidth=3, color='orange', label='old')
    if minTrials < 100:
        plt.axis([1.0, 800.0, 0, 1.1])
    else:
        plt.axis([1.0, 1100.0, 0, 1.1])
    plt.legend(loc=3)
    plt.title('Learning Curve')
    plt.xlabel("Cumulative Count of Trials")
    plt.ylabel("Proportion Correct in " + str(movAvg) + "-trial moving window")
    plt.savefig(figureName)
    plt.show()


def plot(alpha,epsilon,discount):
    props,trials = prep_data(1)
    plot_results(props,trials,1,alpha,epsilon,discount)



def movAvg(alpha,epsilon,discount):
    props,trials = prep_data(50)
    plot_avg(props,1200,50,alpha,epsilon,discount)


