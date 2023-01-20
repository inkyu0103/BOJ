import sys

input = sys.stdin.readline

n, m = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
# print(numbers)

arr = [0] * m
is_used = set()
# print(is_used)


def func(k):
    if k == m:
        print(*arr)
        return

    std = arr[k] if k == 0 else arr[k - 1]

    for number in numbers:
        if k == 0 and number not in is_used:
            arr[k] = number
            is_used.add(number)
            func(k + 1)
            arr[k] = 0
            is_used.remove(number)

        if k != 0 and number not in is_used and number > std:
            arr[k] = number
            is_used.add(number)
            func(k + 1)
            arr[k] = 0
            is_used.remove(number)


func(0)
