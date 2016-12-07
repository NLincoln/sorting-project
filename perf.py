import time
from random import shuffle, random
import math


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


def time_function(func, a):
    with Timer(verbose=False) as t:
        func(a)
    return t.msecs


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

