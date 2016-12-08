from generators import sorted_list, random_no_unique, reversed_list, random_few_unique
from sorting import sorting_functions
from perf_framework import CallStackIncreaser, TrialSet
import matplotlib.pyplot as plt
import sys


cmd_generator = sys.argv[1]

if cmd_generator == 'sorted_list':
    gen = sorted_list
elif cmd_generator == 'random_no_unique':
    gen = random_no_unique
elif cmd_generator == 'reversed_list':
    gen = reversed_list
elif cmd_generator == 'random_few_unique':
    gen = random_few_unique
else:
    raise ValueError('ayyy plz stahp')

max_limit = 10000
step = 10

print(gen.__name__)

def do_trial(func):
    trials = []
    for limit in range(0, max_limit, step):
        trial = TrialSet()
        trial.create_trial(func, gen, limit)
        trials.append((limit, trial.average_time))
    return trials

with CallStackIncreaser(size=10 ** 9):
    gen_trials = []
    for func in sorting_functions:
        gen_trials.append((do_trial(func), func.__name__))


for trial, func_name in gen_trials:
    x, y = zip(*trial)
    plt.plot(x, y, label=func_name)
    plt.xlim(xmax=x[-1])
plt.xlabel('List Length')
plt.ylabel('Running time (ms)')
plt.xlim(xmin=0)
plt.ylim(ymin=0)
plt.legend(loc='upper left')
plt.savefig('multi_images/{}'.format(gen.__name__))
plt.clf()
