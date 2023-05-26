# 컵라면
import sys
import heapq

input = sys.stdin.readline


def sol():
    N = int(input())
    count_deadline = [[] for _ in range(200002)]
    q = []
    answer = 0

    for _ in range(N):
        d, c = map(int, input().split())
        count_deadline[d].append(-c)

    for d in range(200001, 0, -1):
        for c in count_deadline[d]:
            heapq.heappush(q, c)

        if not q:
            continue
        answer -= q[0]
        heapq.heappop(q)

    print(answer)


sol()
