# 10819
'''
N의 크기가 제한적이므로 (3<=N<=8), 모두 돌아봐도 될 것 같은데.

'''

import sys
import math
from itertools import permutations
input = sys.stdin.readline

def calculate(sequence):
    result = 0
    for i in range(len(sequence)-1):
        result += abs(sequence[i] - sequence[i+1])

    return result


def sol():
    N = int(input())
    sequence = map(int,input().split())
    answer = -math.inf

    for target in permutations(sequence,N):
        answer = max(calculate(target),answer)

    print(answer)
sol()
