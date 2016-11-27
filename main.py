import unittest
from sorting.quicksort import quicksort


class TestQSort(unittest.TestCase):
    def test_quicksort(self):
        array = [6, 4, 3, 2, 1]
        sort = quicksort(array, 0, len(array) - 1)

        self.assertEqual(sort, sorted(array))


unittest.main()
