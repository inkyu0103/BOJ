# 9081 두 번째 시도 with Dp

import sys
input = sys.stdin.readline

def sol():
    N = int(input())

    for _ in range(N):
        w1,w2,w3 = map(str,input().strip().split())

        length_w1 = len(w1)
        length_w2 = len(w2)

        # 빈 문자열은 항상 가능하다.
        dp = [[0] * (length_w2+1) for _ in range(length_w1+1)]
        dp[0][0] = 1

        for i in range(1,length_w2+1):
            dp[0][i] = dp[0][i-1] if w2[i-1] == w3[i-1] else 0

        for i in range(1,length_w1+1):
            dp[i][0] = dp[i-1][0] if w1[i-1] == w3[i-1] else 0

        for i in range(1,length_w1+1):
            for j in range(1,length_w2+1):
                if w1[i-1] != w3[i+j-1] and w2[j-1] != w3[i+j-1]:
                    dp[i][j] = 0

                elif w1[i-1] == w3[i+j-1] and w2[j-1] == w3[i+j-1]:
                    dp[i][j] = 1

                elif w1[i-1] == w3[i+j-1] and w2[j-1] != w3[i+j-1]:
                    dp[i][j] = dp[i-1][j]

                elif w1[i-1] != w3[i+j-1] and w2[j-1] == w3[i+j-1]:
                    dp[i][j] = dp[i][j-1]

        result = "yes" if dp[length_w1][length_w2] else "no"
        print("Data set {}: {}".format(_+1,result))

sol()