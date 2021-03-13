# 랜선 자르기 (시간 초과 예상 - 적중)
'''
import sys
input = sys.stdin.readline

def sol ():
    K,N = map(int,input().split())
    lengthData = [int(input()) for _ in range(K)]
    startPoint = sum(lengthData) // N

    while(1):
        target = 0
        for i in lengthData:
            target += (i // startPoint)

        if target == N:
            print(startPoint)
            return
        else:
            startPoint -=1
sol()

여기서는 전부 다 돌 필요가 없다는 이야기?
가장 작은게 하나 더 늘어나면 되는건가?

최대한 덜 줄이는 방향으로 움직여야함
나머지가 적은 순으로 배치해야하나?
802 , 743 , 457, 539
 3     3     1    2
109   50    226   77
200   185   228   179
'''

import sys
input = sys.stdin.readline

def sol ():
    K, N = map(int, input().split())
    lengthData = [int(input()) for _ in range(K)]

    start, end = 1,max(lengthData)

    while(start<=end):
        mid = (start+end) // 2
        lines = 0

        for i in lengthData:
            lines += i // mid

        if lines >= N:
            start = mid + 1
        else:
            end = mid-1
    print(end)

sol()
