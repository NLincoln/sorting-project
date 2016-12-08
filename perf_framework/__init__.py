from typing import Callable, List, Any
import time
import sys


class Trial:
    time = None
    limit = None
    function_name = None
    generator_name = None

    @staticmethod
    def time_function(func: Callable[[List], Any], a: List):
        with Timer(verbose=False) as t:
            func(a)
        return t.msecs

    def do_trial(self, function: Callable[[List], Any], generator: Callable[[int], List], limit: int):
        self.function_name = function.__name__
        self.generator_name = generator.__name__
        self.limit = limit
        self.time = self.time_function(function, generator(limit))


class TrialSet:
    average_time = None
    limit = None
    function_name = None
    generator_name = None

    def __init__(self):
        self.trials = []

    def create_trial(self, func: Callable[[List], Any], generator: Callable[[int], List], limit: int):
        self.function_name = func.__name__
        self.generator_name = generator.__name__
        self.limit = limit

        num_trials = 10
        self.trials = [Trial() for _ in range(num_trials)]
        for trial in self.trials:
            trial.do_trial(func, generator, limit)

        self.average_time = sum([i.time for i in self.trials])


class GrowingSetPerf:
    trials = []

    def growing_size(self, function, generator):
        for i in range(10, 1000, 10):
            trial = TrialSet()
            trial.create_trial(func=function, generator=generator, limit=i)
            self.trials.append(trial)


class PerfForGenerator:
    trials = []

    def generator_perf(self, functions, generator):
        for function in functions:
            trial = GrowingSetPerf()
            trial.growing_size(function=function, generator=generator)
            self.trials.append(trial)


class CallStackIncreaser(object):
    old_size = None

    def __init__(self, size: int):
        self.size = size

    def __enter__(self):
        self.old_size = sys.getrecursionlimit()
        sys.setrecursionlimit(self.size)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.setrecursionlimit(self.old_size)



class Timer(object):
    def __init__(self, verbose=False):
        self.verbose = verbose

    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, *args):
        self.end = time.time()
        self.secs = self.end - self.start
        self.msecs = self.secs * 1000
        if self.verbose:
            print(u'elapsed time: {0:f} ms'.format(self.msecs))

