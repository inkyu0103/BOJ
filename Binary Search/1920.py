# 1920 수 찾기
import sys
input = sys.stdin.readline

def bs (target,arr):
    left,right = 0, len(arr)-1

    while left <= right:
        mid = (left+right)//2
        if arr[mid] == target:
            return 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return 0


def sol ():
    target = input()
    arr1 = list(map(int,input().strip().split()))
    arr1.sort()

    target = input()
    arr2 = list(map(int,input().strip().split()))

    for i in arr2:
        print(bs(i ,arr1))

sol()

