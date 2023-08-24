# 20303 할로윈의 양아치

import sys
from collections import deque
from itertools import combinations

input = sys.stdin.readline


def sol():
    # N : 아이들 수, M : 관계 수 , K : 우는 아이 수
    N, M, K = map(int, input().split())
    visit = [0] * (N + 1)
    candies = [0] + list(map(int, input().split()))
    adj = [[] for _ in range(N + 1)]
    groups = []
    t = [[]]
    answer = 0

    for _ in range(M):
        s, e = map(int, input().split())
        adj[s].append(e)
        adj[e].append(s)

    for i in range(1, N + 1):
        if not visit[i]:
            q = deque([i])
            visit[i] = 1
            temp_candy = candies[i]
            temp_friends = 1

            while q:
                cur = q.popleft()

                for n in adj[cur]:
                    if not visit[n]:
                        q.append(n)
                        visit[n] = 1
                        temp_friends += 1
                        temp_candy += candies[n]

            t.append([temp_friends, temp_candy])

    dp = [[0] * K for _ in range(len(t))]

    for r in range(1, len(t)):
        for c in range(1, K):
            if t[r][0] > c:
                dp[r][c] = dp[r - 1][c]

            else:
                dp[r][c] = max(dp[r - 1][c], dp[r - 1][c - t[r][0]] + t[r][1])

    print(dp[-1][-1])


sol()
