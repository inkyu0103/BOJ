#11279

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
            print(heapq.heappop(q)[1])

    else:
        heapq.heappush(q,(-user,user))

