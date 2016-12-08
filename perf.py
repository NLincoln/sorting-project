import math
from random import shuffle, random
from typing import List
from perf_framework import PerfForGenerator, CallStackIncreaser
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
    # insertion_sort,
    # merge_sort
]

generators = [
    # generate_sorted,
    # generate_random_few_unique,
    # generate_random_no_unique,
    generate_reversed_list
]


with CallStackIncreaser(size=10 ** 9):
    generator_perfs = []
    for gen in generators:
        print('testing the performance of all sorting functions against generator {}'.format(gen.__name__))

        trial = PerfForGenerator()
        trial.generator_perf(sorting_functions, gen)
        for i in trial.trials:
            for j in i.trials:
                print('The sorting algorithm {algo} took {time:f}ms to run for {limit} elements'
                      ''.format(algo=j.function_name, time=j.average_time, limit=j.limit))

