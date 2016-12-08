import math
from random import shuffle, random
from typing import List
from perf_framework import PerfForGenerator, CallStackIncreaser, GrowingSetPerf
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


with CallStackIncreaser(size=10 ** 9):
    generator_perfs = []
    for gen in generators:
        for func in sorting_functions:
            print('testing the performance of {} functions against generator {}'.format(func.__name__, gen.__name__))
            trials = GrowingSetPerf()
            trials.growing_size(func, gen)

            for trial in trials.trials:
                print('The sorting algorithm {algo} took {time:f}ms to run for {limit} elements'
                      ''.format(algo=func.__name__, time=trial.average_time, limit=trial.limit))

