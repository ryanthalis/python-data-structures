"""Sequential and binary search implementations."""


def sequential_search(lst, x):
    iterable = lst.__iter__()
    counter = 0


    for i in iterable:
        if i == x:
            return counter
        counter += 1

    return -1


def binary_search(lst, x):
    low = 0
    high = len(lst) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = lst.__getitem__(mid)

        if guess == x:
            return mid

        if guess > x:
            high = mid - 1
        else:
            low = mid + 1

    return -1
