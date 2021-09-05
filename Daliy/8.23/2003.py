# 2003 수들의합
import sys
input = sys.stdin.readline

def sol():
    N,M = map(int,input().split())
    arr = list(map(int,input().split()))
    l,r = 0,1
    answer = 0
    tmp_sum = arr[l]

    while l < N :
        if tmp_sum == M:
            answer += 1
            tmp_sum-= arr[l]
            l+=1

        if r == N and tmp_sum<M:
            break
        elif tmp_sum <M:
            tmp_sum += arr[r]
            r+= 1
        elif tmp_sum > M:
            tmp_sum -= arr[l]
            l += 1

    print(answer)

sol()