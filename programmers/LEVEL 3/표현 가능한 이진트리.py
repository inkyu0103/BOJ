from math import log2, ceil

import sys

sys.setrecursionlimit(100000000)


def check_tree(start, end, is_parent, string):
    if start == end:
        return False if not is_parent and string[start] == "1" else True

    mid = (start + end) // 2
    parent = True if string[mid] == "1" else False

    if not is_parent and string[mid] == "1":
        return False

    else:
        return check_tree(start, mid - 1, parent, string) and check_tree(
            mid + 1, end, parent, string
        )


def transform_binary(number):
    binary_num = bin(number)[2:]
    additional_zeros = 2 ** ceil(log2(len(binary_num))) - 1
    result = binary_num.zfill(additional_zeros)

    return result


def solution(numbers):
    answer = []

    for n in numbers:
        string = transform_binary(n)

        mid = (len(string) - 1) // 2

        if string[mid] == "0":
            answer.append(0)
            continue

        if check_tree(0, len(string) - 1, True, string):
            answer.append(1)
        else:
            answer.append(0)

    return answer


solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
