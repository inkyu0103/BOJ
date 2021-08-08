# 숨바꼭질 4

from collections import deque
import sys
input = sys.stdin.readline
MAX = 100001

def sol():
    N,K =map(int,input().split())
    check = [-1] * MAX
    visit = [i for i in range(100001)]

    check[N] = 0
    q = deque()
    q.append(N)
    cnt = 0

    tmp = []

    while q:
        x = q.popleft()
        if x == K :
            cnt += 1

        for y in [x*2,x-1,x+1]:
            if 0<= y < MAX:
                if check[y] == -1 or check[y] == check[x] + 1:
                    check[y] = check[x] + 1
                    q.append(y)
                    visit[y] = x

    print(check[K])
    answer = [K]
    while (visit[K] != K):
        answer.append(visit[K])
        K = visit[K]

    answer.reverse()
    print(*answer)

sol()
