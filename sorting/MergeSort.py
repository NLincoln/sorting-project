def merge(left: list, right: list):
    result = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left[0])
            left.pop(0)
        else:
            result.append(right[0])
            right.pop(0)

    result += left
    result += right
    return result


def merge_sort(a):
    len_ = len(a)
    if len_ < 2:
        return a
    right = a[len_ // 2:]
    left = a[:len_ // 2]

    right = merge_sort(right)
    left = merge_sort(left)

    return merge(left, right)
