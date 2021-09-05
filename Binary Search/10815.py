# 10815
import sys
input = sys.stdin.readline

def bin_search(target):
    l,r = 0,len(arr)-1
    answer = -1

    while l<=r:
        mid=(l+r)// 2


        if target == arr[mid]:
            answer = mid

        if target < arr[mid]:
            r = mid-1

        else:
            l = mid + 1

    return 1 if answer != -1 else 0





N = int(input())
arr = list(map(int,input().split()))
q = int(input())
q_arr= list(map(int,input().split()))
arr.sort()
answer =[]


for i in q_arr:
    answer.append(bin_search(i))

print(*answer)
