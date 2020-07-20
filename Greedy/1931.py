#1931 회의실 배정

import sys
import heapq

conf = int(input())

count = 1
time = []
optimal = []
CHECK=(-1,-1)

for i in range(conf):
    st, ed = map(int,sys.stdin.readline().split())
    heapq.heappush(time,(ed,st))

CHECK = heapq.heappop(time)


while len(time) != 0:
    end , start  = heapq.heappop(time)

    if start >= CHECK[0]:
        count += 1
        CHECK = (end,start)



print(count)






