import math
from random import shuffle, random
from typing import List
from perf_framework import CallStackIncreaser, TrialSet
from sorting.quicksort import quicksort
from sorting.BubbleSort import bubble_sort
from sorting.InsertionSort import insertion_sort
from sorting.MergeSort import merge_sort


def generate_sorted(limit: int) -> List[int]:
    return list(range(limit))


def generate_random_no_unique(limit: int) -> List[int]:
    l = generate_sorted(limit)
    shuffle(l)
    return l


def generate_reversed_list(limit: int) -> List[int]:
    a = generate_sorted(limit)
    a.reverse()
    return a


def generate_random_few_unique(limit: int) -> List[int]:
    return [int(limit / math.log(limit) * random()) for _ in range(0, limit)]


sorting_functions = [
    quicksort,
    bubble_sort,
    insertion_sort,
    merge_sort
]

generators = [
    generate_sorted,
    generate_random_few_unique,
    generate_random_no_unique,
    generate_reversed_list
]

max_limit = 10000
step = 10

with CallStackIncreaser(size=10 ** 9):
    generator_perfs = []
    for gen in generators:
        for func in sorting_functions:
            for limit in range(0, max_limit, step):
                trial = TrialSet()
                trial.create_trial(func, gen, limit)
                print('{gen},{algo},{time},{limit}'.format(gen=gen.__name__,
                                                           algo=func.__name__,
                                                           time=trial.average_time,
                                                           limit=trial.limit))
