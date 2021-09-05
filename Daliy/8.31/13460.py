# 13460 구슬 탈출 - 과연 성공할 수 있을까?
# 4차원 배열 visit을 만드는 이유는... 거야 뭐 방문한 곳을 방문하지 않게하기 위해서지.

from collections import deque
import sys
input = sys.stdin.readline

def find_initial_info():
    R= (-1,-1)
    B= (-1,-1)
    F= (-1,-1)

    for r in range(N):
        for c in range(M):
            if graph[r][c] == "R":



# N,M크기가 작다.
N,M = map(int,input().split())
graph = [list(input().strip()) for _ in range(N)]


