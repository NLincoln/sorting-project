import unittest


def partition(a, p, r):
    x = a[r]
    i = p - 1
    for j in range(p, r):
        if a[j] <= x:
            i += 1
            a[i], a[j] = a[j], a[i]
    a[i + 1], a[r] = a[r], a[i + 1]
    return i + 1


def quicksort(a, p, r):
    if p < r:
        q = partition(a, p, r)
        quicksort(a, p, q - 1)
        quicksort(a, q + 1, r)

    return a


class TestQSort(unittest.TestCase):
    def test_quicksort(self):
        array = [6, 4, 3, 2, 1]
        sort = quicksort(array, 0, len(array) - 1)

        self.assertEqual(sort, sorted(array))


unittest.main()
