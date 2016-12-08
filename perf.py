import math
from random import shuffle, random
from perf_framework import CallStackIncreaser, TrialSet
from sorting.quicksort import quicksort
from sorting.BubbleSort import bubble_sort
from sorting.InsertionSort import insertion_sort
from sorting.MergeSort import merge_sort
import matplotlib.pyplot as plt


def sorted_list(limit):
    return list(range(limit))


def random_no_unique(limit):
    l = sorted_list(limit)
    shuffle(l)
    return l


def reversed_list(limit):
    a = sorted_list(limit)
    a.reverse()
    return a


def random_few_unique(limit):
    return [int(limit / math.log(limit) * random()) for _ in range(0, limit)]


sorting_functions = [
    quicksort,
    bubble_sort,
    insertion_sort,
    merge_sort
]

generators = [
    sorted_list,
    random_few_unique,
    random_no_unique,
    reversed_list
]

max_limit = 10000
step = 10


def do_trial(func, gen, verbose=False):
    trials = []
    for limit in range(0, max_limit, step):
        trial = TrialSet()
        trial.create_trial(func, gen, limit)
        trials.append((limit, trial.average_time))
        if verbose:
            print('{gen},{algo},{time},{limit}'.format(gen=gen.__name__,
                                                       algo=func.__name__,
                                                       time=trial.average_time,
                                                       limit=trial.limit))
    return trials

with CallStackIncreaser(size=10 ** 9):
    all_trials = []
    for gen in generators:
        gen_trials = []
        for func in sorting_functions:
            gen_trials.append((do_trial(func, gen), func.__name__))
        all_trials.append((gen_trials, gen.__name__))

for gen_trial, gen_name in all_trials:
    for trial, func_name in gen_trial:
        x, y = zip(*trial)
        plt.plot(x, y, label=func_name)
        plt.xlim(xmax=x[-1])
    plt.xlim(xmin=0)
    plt.ylim(ymin=0)
    plt.legend(loc='upper left')
    plt.savefig('images/{}'.format(gen_name))
    plt.clf()
