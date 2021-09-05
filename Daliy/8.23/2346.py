# 2346 풍선터뜨리기

import sys
from collections import deque
input = sys.stdin.readline
answer = []

stack = []
arr = deque([])
N = int(input())

for idx,ele in enumerate(map(int,input().split())):
    arr.append([idx+1,ele])
# 첫 번째 풍선

while arr:
    idx,ele = arr.popleft()
    answer.append(idx)

    if ele > 0:
        arr.rotate(-(ele-1))
    else:
        arr.rotate(-ele)


print(*answer)
