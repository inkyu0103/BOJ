# 3273

import sys
input = sys.stdin.readline

def sol( ):
    # 정렬을 해도 딱히 상관이 없는 듯 하다.
    length = int(input())
    arr = list(map(int,input().strip().split()))
    target = int(input())
    count,left,right  = 0,0,length-1
    arr.sort()

    while(left<right):
        if arr[left] + arr[right] == target:
            left += 1
            right -= 1
            count += 1
        elif arr[left] + arr[right] < target:
            left += 1

        else:
            right -=1

    print(count)

sol()
