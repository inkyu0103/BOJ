#9081
from itertools import permutations
import sys
input = sys.stdin.readline

def sol():
    N = int(input())
    arr = [input().rstrip() for _ in range(N)]
    for c in arr:
        box = set()
        for t in permutations(c, len(c)):
            box.add("".join(t))

        list_box = list(box)
        list_box.sort()

        if list_box.index(c) == len(list_box)-1:
            print(c)
        else:
            print(list_box[list_box.index(c)+1])

sol()
