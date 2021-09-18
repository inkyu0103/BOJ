#5568 카드 놓기(7시 41분 ~ 7시 48분)

from itertools import permutations
import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
num_list = []
combi = set()

for _ in range(n):
    val = input().rstrip()
    num_list.append(val)

for target in permutations(num_list,k):
    number = int("".join(list(target)))
    if number not in combi:
        combi.add(number)

print(len(combi))
