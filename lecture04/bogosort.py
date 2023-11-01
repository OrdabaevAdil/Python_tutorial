import random


def is_sorted(arr):
    n = len(arr)
    for i in range(0, n-1):
        if arr[i+1] < arr[i]:
            return False
    return True


def bogo(arr):
    while not is_sorted(arr):
        random.shuffle(arr)
    return arr


a = [2, 9, 7, 1]
print(bogo(a))