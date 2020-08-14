# 11053 가장 긴 증가하는 부분수열
import sys

seqLength = int(input())
seq = [int(i) for i in input().split()]

# 완전 탐색
def solve(arr):
    # 기저 사례 (하나도 없는 경우)
    if len(arr) == 0:
        return 0
    #기본으로 0으로 준 후에...
    length = 0
    for i in range(len(arr)):
        tmpArr = []
        for j in range(i+1,len(arr)):
            if arr[i] < arr[j] :
                tmpArr.append(arr[j])
        length = max(length, solve(arr)+1)
    return length

solve(seq)

