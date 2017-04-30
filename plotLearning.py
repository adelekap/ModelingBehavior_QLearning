import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
import scipy
import numpy as np
from scipy.optimize import curve_fit


def prep_data(movAvg):
    """
    Calculates proportions for the trace.
    """
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
    with open('rat1027.txt', 'r') as old:
        lines = old.readlines()
        oldDecisions = lines.split(',')
    with open('rat10282.txt', 'r') as young:
        lines = young.readlines()
        youngDecisions = lines.split(',')
    return (youngDecisions,oldDecisions)


def plot_results(proportions,trialNum,movAvg):
    """
    Plots the performance of the agent to learn the W-track spatial alternation task.
    This is a simple 3 degree polynomial fit by first performing a least squares
    polynomial fit and the second calculates the new points.
    """
    trials = range(0,trialNum,movAvg)
    figureName = 'LearningCurve.png'
    plt.figure('Learning Curve')

    x = trials
    y = proportions

    z = np.polyfit(x, y, 3)
    f = np.poly1d(z)

    new_x = np.linspace(x[0], x[-1], 50)
    new_y = f(new_x)

    line = plt.plot(new_x,new_y,'-')
    plt.setp(line, linewidth=3, color='purple')
    plt.axis([1,trialNum,0,1.1])
    plt.title('Learning Curve')
    plt.xlabel("Cumulative Count of Trials")
    plt.ylabel("Proportion Correct")
    plt.savefig(figureName)
    plt.close()

def plot():
    props,trials = prep_data(1)
    plot_results(props,trials,1)


