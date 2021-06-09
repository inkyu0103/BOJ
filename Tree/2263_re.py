# 2263 retry

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def divide (i_start,i_end,p_start,p_end):
    if i_start > i_end or p_start > p_end:
        return

    parent = porder[p_end]
    print(parent, end=' ')

    left = arr[parent]-i_start
    right = i_end - arr[parent]

    divide(i_start,arr[parent]-1,p_start,p_start+left-1)
    divide(i_end-right+1,i_end,p_end-right,p_end-1)






if __name__ =="__main__":
    V = int(input())
    iorder = list(map(int,input().split()))
    porder = list(map(int,input().split()))
    # postorder에서 root를 찾는데 매번 index로 찾으면 멋이 안 살잖어~
    arr = [0]*(V+1)

    for i in range(V):
        arr[iorder[i]] = i


    divide(0,V-1,0,V-1)
