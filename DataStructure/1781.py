# 컵라면
import sys
import heapq

input = sys.stdin.readline


def sol():
    N = int(input())
    data = []

    for _ in range(N):
        d, c = map(int, input().split())
        heapq.heappush(data, (d, -c))

    print(data)
    print(heapq.heappop(data))
    print(data)

    stack = []


sol()
