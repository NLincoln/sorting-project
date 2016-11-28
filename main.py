import unittest
from sorting.quicksort import quicksort
from sorting.BubbleSort import bubble_sort
from sorting.InsertionSort import insertion_sort
from sorting.MergeSort import merge_sort
import random
import sys


class TestSort(unittest.TestCase):
    def sort(self, a):
        return

    def test_random(self):
        old_callstack = sys.getrecursionlimit()
        sys.setrecursionlimit(10000)
        self.do_test([int(100*random.random()) for _ in range(1000)])
        sys.setrecursionlimit(old_callstack)

    def test_duplicates(self):
        self.do_test([1, 1, 2, 1, 1, 2])

    def test_empty(self):
        self.do_test([])

    def test_reversed(self):
        self.do_test(list(range(10, 0, -1)))

    def test_pre_sorted(self):
        self.do_test(list(range(10)))

    def test_trivial_case(self):
        self.do_test([6, 4, 3, 2, 1])

    def do_test(self, array):
        sorted_ = self.sort(array)
        if not sorted_:
            return
        self.assertEqual(sorted_, sorted(array))


class TestQSort(TestSort):
    def sort(self, a):
        return quicksort(a)


class TestBSort(TestSort):
    def sort(self, a):
        return bubble_sort(a)


class TestISort(TestSort):
    def sort(self, a):
        return insertion_sort(a)


class TestMSort(TestSort):
    def sort(self, a):
        return merge_sort(a)

unittest.main()
