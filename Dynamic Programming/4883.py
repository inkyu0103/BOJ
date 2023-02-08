# 4883 삼각 그래프
import sys

input = sys.stdin.readline

tc = 1

while True:
    N = int(input())

    # 0을 받은 경우
    if not N:
        break

    arr = [list(map(int, input().split())) for _ in range(N)]
    dp = [[0] * 3 for _ in range(N)]
    # dp 기본값 설정
    dp[0][0], dp[0][1], dp[0][2] = arr[0][0], arr[0][1], arr[0][2] + arr[0][1]
    dp[1][0] = dp[0][1] + arr[1][0]
    dp[1][1] = min(dp[0][1], dp[0][2], dp[1][0]) + arr[1][1]
    dp[1][2] = min(dp[0][1], dp[0][2], dp[1][1]) + arr[1][2]

    # dp 돌리기
    for r in range(2, N):
        for c in range(3):
            if c == 0:
                dp[r][c] = min(dp[r - 1][c], dp[r - 1][c + 1]) + arr[r][c]

            elif c == 1:
                dp[r][c] = (
                    min(dp[r - 1][c - 1], dp[r - 1][c], dp[r - 1][c + 1], dp[r][c - 1])
                    + arr[r][c]
                )

            else:
                dp[r][c] = min(dp[r - 1][c], dp[r - 1][c - 1], dp[r][c - 1]) + arr[r][c]

    print(f"{tc}. {dp[N-1][1]}")

    # tc 개수 증가
    tc += 1
