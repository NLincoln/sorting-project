import unittest
from sorting.quicksort import quicksort
from sorting.BubbleSort import bubble_sort

class TestSort(unittest.TestCase):
    def sort(self, a):
        return a

    def do_test(self):
        array = [6, 4, 3, 2, 1]

        self.assertEqual(self.sort(array), sorted(array))


class TestQSort(TestSort):
    def sort(self, a):
        return quicksort(a)

    def test_qsort(self):
        self.do_test()


class TestBSort(TestSort):
    def sort(self, a):
        return bubble_sort(a)

    def test_qsort(self):
        self.do_test()

unittest.main()
