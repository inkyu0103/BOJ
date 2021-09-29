# 2078
from collections import deque
import sys
input = sys.stdin.readline

def sol():
    L,R = map(int,input().split())
    arr = [[1,1]]

    for idx,[v1,v2] in enumerate(arr):
        if [v1,v2] == [L,R]:
            print(idx)
            break

        arr.append([v1+v2,v2])
        arr.append([v1,v1+v2])

sol()
