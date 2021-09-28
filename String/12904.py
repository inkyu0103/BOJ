# 12904
from collections import deque
import sys
input = sys.stdin.readline

def sol():
    S = list(input().strip())
    T = list(input().strip())

    while len(S) != len(T):
        if T[-1] == 'A':
            T.pop()
        elif T[-1] == 'B':
            T.pop()
            T = T[::-1]

    if S == T:
        print(1)
    else:
        print(0)
sol()