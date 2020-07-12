#1697 숨바꼭질

import sys
from collections import deque
# N: 수빈 ,  M : 동생
N ,M = map(int,sys.stdin.readline().split())
Max = 100001
time =[0]*Max

def bfs():
    queue = deque()
    queue.append(N)

    while queue:
        start = queue.popleft()

        if start == M:
            print(time[start])
            return

        for next in (start-1,start+1,start*2):
            if 0<= next < Max and not time[next]:
                time[next] = time[start]+1
                queue.append(next)


bfs()
