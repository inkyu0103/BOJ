# 15903
import sys
import heapq

input = sys.stdin.readline


def sol():
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    q = []

    for v in arr:
        heapq.heappush(q, v)

    for _ in range(m):
        v1, v2 = heapq.heappop(q), heapq.heappop(q)

        _sum = v1 + v2

        heapq.heappush(q, _sum)
        heapq.heappush(q, _sum)

    print(sum(q))


sol()
