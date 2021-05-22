# 2470
import sys
input = sys.stdin.readline

def sol():
    num = int(input())
    arr = list(map(int,input().split()))
    arr.sort()
    left,right = 0,num-1
    answer = [sys.maxsize,sys.maxsize]
    while(left<right):
        val = arr[left]+ arr[right]
        if val==0:
            answer = [arr[left],arr[right]]
            break
        elif val< 0:
            if abs(sum(answer)) > abs(val):
                answer =  [arr[left],arr[right]]
            left += 1

        elif val > 0:
            if abs(sum(answer)) > abs(val):
                answer =  [arr[left],arr[right]]
            right -= 1

    answer.sort()
    print(*answer)

sol()
