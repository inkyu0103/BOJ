# 2531 회전초밥
import sys

input = sys.stdin.readline


def sol():
    N, d, k, c = map(int, input().split())
    sushis = [int(input()) for _ in range(N)]

    answer_candidates = []

    for i in range(N - 1):
        sushi_set = set()
        sushi_set.add(sushis[i])
        for j in range(i + 1, N):
            if sushis[j] in sushi_set:
                if len(sushi_set) < k:
                    answer_candidates.append(len(sushi_set))
                else:
                    sushi_set.add(c)
                    answer_candidates.append(len(sushi_set))
                break

            else:
                sushi_set.add(sushis[j])

    print(max(answer_candidates))


sol()
