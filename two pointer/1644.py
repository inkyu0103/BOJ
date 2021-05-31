# 1644 소수의 연속합

import sys
import math
input = sys.stdin.readline

def sol():
    N = int(input())

    if N == 1 or N == 2:
        print(0)
        return

    left,right = 0,0

    # 소수 배열 만들기
    prime = [2,3,5,7]
    for i in range(11,int(math.sqrt(N))+2):
        print(prime)
        flag = 0
        if i % 2 == 0:
            continue
        for j in range(3,int(math.sqrt(i))+2):
            if i % j == 0:
                flag = 1
                break
        if flag == 0:
            prime.append(i)

    tmp = prime[0]

    count = 0
    while 1:
        if tmp >= N :
            if tmp == N:
                count += 1
            tmp -= prime[left]
            left += 1

        elif right == len(prime)-1:
            break

        elif tmp < N :
            right += 1
            tmp += prime[right]
    print(count)

sol()
