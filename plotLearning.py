import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
import scipy
import numpy as np


def prep_data(movAvg):
    with open('decisions.txt','r') as f:
        lines = f.readlines()
    data = [line.split(',') for line in lines][0]
    normalize = 0
    sum =0
    proportions = []
    for d in data:
        normalize += 1
        sum += int(d)
        if (normalize == movAvg) or (d == data[len(data) - 1]):
            proportions.append(float(sum)/float(normalize))
            normalize =0
            sum = 0
    return (proportions, len(data))


def plot_results(proportions,trialNum,movAvg):
    trials = range(0,trialNum,movAvg)
    figureName = 'LearningCurve.png'
    plt.figure('Learning Curve')

    x = trials
    y = proportions

    points = zip(x, y)
    points = sorted(points, key=lambda point: point[0])
    x1, y1 = zip(*points)
    new_length = 25
    new_x = np.linspace(min(x1), max(x1), new_length)
    new_y = interp1d(x1, y1, kind='cubic')(new_x)

    plt.plot(new_x,new_y,'--')
    plt.axis([1,trialNum,0,1.1])
    plt.title('Learning Curve')
    plt.xlabel("Cumulative Count of Trials")
    plt.ylabel("Proportion Correct in " + str(movAvg) + "-trial moving window")
    plt.savefig(figureName)
    plt.close()

def plot():
    props,trials = prep_data(10)
    plot_results(props,trials,10)

