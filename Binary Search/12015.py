# 12015 가장 긴 증가하는 부분수열

import sys
input = sys.stdin.readline

def sol():
    N = int(input())
    numData = list(map(int,input().strip().split()))
    DP = [0]

    for i in range(N):
        start,end = 0,len(DP)-1

        while start<=end:
            mid = (start+end)//2
            if DP[mid] < numData[i]:
                start = mid + 1
            else:
                end = mid -1
        if start >= len(DP):
            DP.append(numData[i])
        else:
            DP[start] = numData[i]
    print(len(DP)-1)


sol()
