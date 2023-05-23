# 13975 파일 합치기 3
import sys
import heapq

input = sys.stdin.readline


def sol():
    tc = int(input())
    for _ in range(tc):
        N = int(input())
        q = list(map(int, input().split()))
        heapq.heapify(q)

        answer = 0

        while True:
            _sum = heapq.heappop(q) + heapq.heappop(q)
            answer += _sum

            if not q:
                break
            heapq.heappush(q, _sum)

        print(answer)


sol()
