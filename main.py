import unittest
from sorting.quicksort import quicksort
from sorting.BubbleSort import bubble_sort
from sorting.InsertionSort import insertion_sort


class TestSort(unittest.TestCase):
    def sort(self, a):
        return None

    def test_trivial_case(self):
        self.do_test([6, 4, 3, 2, 1])

    def do_test(self, array):
        sorted_  = self.sort(array)
        if not sorted_:
            return
        self.assertEqual(self.sort(array), sorted(array))


class TestQSort(TestSort):
    def sort(self, a):
        return quicksort(a)


class TestBSort(TestSort):
    def sort(self, a):
        return bubble_sort(a)


class TestISort(TestSort):
    def sort(self, a):
        return insertion_sort(a)

unittest.main()
