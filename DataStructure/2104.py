# 2104 부분 배열 고르기
# 1트 메모리 초과
# 2트 메모리 초과
# 3트 메모리 초과

import sys

def sol():
    num = int(sys.stdin.readline())
    data = [int(i) for i in sys.stdin.readline().split()]
    dp = [[0]*(num-i) for i in range(num)] # 얘를 어떻게 줄여야하나...? 반을 못쓰니까 엥...? 여기서 더 줄여?
    answer = -1

    for i in range(num):
        dp[i][0] = data[i]


    for i in range(num):
        for j in range(1,num-i):
            dp[i][j] = dp[i][j-1] + data[i+j]


    for i in range(num):
        min_value = data[i]
        for j in range(num-i):
            if min_value > data[j+i]:
                min_value = data[j+i]

            if answer < dp[i][j]*min_value:
                answer = dp[i][j]*min_value

    print(answer)
sol()
