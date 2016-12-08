import math
from random import random, shuffle


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

generators = [
    sorted_list,
    random_few_unique,
    random_no_unique,
    reversed_list
]
