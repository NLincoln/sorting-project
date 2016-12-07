import time
from random import shuffle, random
import math
from typing import Callable, List, Any


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
        self.trials = [Trial().do_trial(func, generator, limit) for _ in range(num_trials)]

        self.average_time = sum([i.time for i in self.trials])


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



def generate_sorted(limit):
    return list(range(0, limit))


def generate_random_no_unique(limit):
    return shuffle(generate_sorted(limit))


def generate_reversed_list(limit):
    return generate_sorted(limit).reverse()


def generate_random_few_unique(limit):
    return [int(limit / math.log(limit) * random()) for _ in range(0, limit)]

generator_functions = [
    generate_sorted,
    generate_random_few_unique,
    generate_random_no_unique,
    generate_reversed_list
]

generators = [{"name": g.__name__, "func": g} for g in generator_functions]
