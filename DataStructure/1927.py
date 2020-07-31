# 1927 최소 힙

import sys
import heapq

N = int(input())
q=[]
for x in range(N):
    user = int(sys.stdin.readline())
    if user == 0 :
        if len(q) == 0:
            print(0)
        else:
            print(heapq.heappop(q))
    else:
        heapq.heappush(q,user)