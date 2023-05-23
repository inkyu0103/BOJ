# 1715 카드 정렬하기
import sys
import heapq

input = sys.stdin.readline


def sol():
    N = int(input())
    q = []
    answer = 0

    if N == 1:
        print(0)
        return

    for _ in range(N):
        heapq.heappush(q, int(input()))

    while True:
        first = heapq.heappop(q)
        second = heapq.heappop(q)
        _sum = first + second

        answer += _sum

        if not q:
            break

        heapq.heappush(q, _sum)

    print(answer)


sol()
