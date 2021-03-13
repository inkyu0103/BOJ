# 2805 나무 자르기
import sys
from collections import Counter
input = sys.stdin.readline

def cutWoods (woodarr,height):
    tmp = 0
    for wood,cnt in woodarr.items():
        if wood > height :
            tmp += (wood-height)*cnt
    return tmp

def sol():
    # M이 목표 나무 길이
    N,M = map(int,input().split())
    woods = Counter(map(int,input().split()))
    start, end = 1, max(woods)

    while(start<=end):
        mid = (start+end)//2
        check = cutWoods(woods,mid)

        if check >=M:
            start = mid + 1
        else:
            end = mid -1
    print(end)

sol()
