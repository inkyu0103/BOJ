# 1980 점프 --> 메모리 초과 / O(N^2)인 DP로 해결
from collections import deque
import sys
input = sys.stdin.readline

def sol():
    N = int(input())
    q = deque()
    graph = [list(map(int,input().split())) for _ in range(N)]
    visit = [[0]*N for _ in range(N)]

    # step , r, c
    q.append([graph[0][0],0,0])
    answer = 0

    while q:
        cur_step,r,c=q.popleft()

        new_r,new_c = r+cur_step,c+cur_step

        if (new_r,c) == (N-1,N-1) or (r,new_c)== (N-1,N-1):
            answer += 1

        if 0<=new_r<N and graph[new_r][c]:
            q.append([graph[new_r][c],new_r,c])

        if 0<=new_c<N and graph[r][new_c]:
            q.append([graph[r][new_c],r,new_c])

    print(answer)

sol()