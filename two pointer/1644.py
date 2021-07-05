# 1644 소수의 연속합

import sys
import math
input = sys.stdin.readline

def isPrime(target):
    if target <=1:
        return False
    if target % 2 == 0:
        return True if target == 2 else False
    for i in range(3,int(math.sqrt(target))+1,2):
        if target % i == 0:
            return False
    return True


def sol():
    N = int(input())
    if N == 1:
        print(0)
        return

    answer = 0
    # 자기 자신이 소수일 경우
    prime_arr = []
    for target in range(N+1):
        if isPrime(target):
            prime_arr.append(target)

    # left index,  right index, 누적 합
    left,right= 0, 0
    acc_sum = prime_arr[left]

    # 먼저 right가 증가하고 acc_sum[right]에 들어가면 idx error 을 겪는 경우 존재.
    while left <= right:
        if acc_sum < N:
            right += 1
            if right < len(prime_arr):
                acc_sum += prime_arr[right]
            else:
                break
        elif acc_sum > N :
            acc_sum -= prime_arr[left]
            left += 1
        else:
            answer += 1
            acc_sum -= prime_arr[left]
            left += 1


    print(answer)
sol()
