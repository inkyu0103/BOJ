# 15954 인형들
import sys
import math
input = sys.stdin.readline

def dis (mean,arr):
    result = 0
    for i in arr:
        result += (i - mean) ** 2
    return result / len(arr)

def sol():
    N,K = map(int,input().split())
    data = list(map(int,input().split()))
    min_value = 1e19

    for i in range(0,N-K+1):
        for j in range(N-K-i+2):
            tmp = data[i:K+i+j]
            mean = sum(tmp)/len(tmp)
            distribution = dis(mean,tmp)

            if min_value > distribution:
                min_value = distribution
    print(math.sqrt(min_value))

sol()
