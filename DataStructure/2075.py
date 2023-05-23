# 2075 N번째 큰 수

import heapq
import sys

input = sys.stdin.readline


def sol():
    heap = []
    n = int(input())

    for _ in range(n):
        numbers = map(int, input().split())
        for number in numbers:
            if len(heap) < n:
                heapq.heappush(heap, number)
            else:
                if heap[0] < number:
                    heapq.heappop(heap)
                    heapq.heappush(heap, number)
    print(heap[0])


sol()
