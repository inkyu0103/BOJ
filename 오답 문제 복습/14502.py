'''
1. 벽을 세운다.
2. 바이러스를 퍼뜨린다.
3. 안전한 곳의 개수를 센다.
'''

import sys
import copy
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
ans = 0

def bfs():
    global ans
    w = copy.deepcopy(a)
    for i in range(n):
        for j in range(m):
            if w[i][j] == 2:
                q.append([i, j])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if w[nx][ny] == 0:
                    w[nx][ny] = 2
                    q.append([nx, ny])

    cnt = 0
    for i in w:
        cnt += i.count(0)
    ans = max(ans, cnt)

# 이 부분이 정말 좋은듯
def wall(x):
    if x == 3:
        bfs()
        return
    for i in range(n):
        for j in range(m):
            if a[i][j] == 0:
                a[i][j] = 1
                wall(x+1)
                a[i][j] = 0

n, m = map(int, sys.stdin.readline().split())
a = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
q = deque()
wall(0)
print(ans)


