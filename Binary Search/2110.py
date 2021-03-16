# 2110 공유기 설치

import sys
input = sys.stdin.readline

def counting(dist):
    global homeData,N,C

    count = 1
    cur = homeData[0]

    for i in range(1,N):
        if cur + dist <= homeData[i]:
            count += 1
            cur = homeData[i]
    return count

def sol():
    global homeData,N,C
    start,end = 1,homeData[-1]-homeData[0]
    answer = 0
    while(start<=end):
        mid = (start+end)//2

        if counting(mid) >= C:
            answer = mid
            start = mid + 1
        else:
            end = mid-1
    print(answer)

if __name__ == "__main__":
    N, C = map(int, input().split())
    homeData = [int(input()) for _ in range(N)]
    homeData.sort()
    sol()