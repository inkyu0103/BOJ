# 2304 창고 다각형

import sys

def sol():
    tc = int(input())
    data = [0]*1001
    for i in range(tc):
        point,height = map(int,sys.stdin.readline().split())
        data[point]=height

    max_val = max(data)
    max_idx = data.index(max_val)

    # 오른쪽
    for i in range(0,max_idx-1):
        if data[i] > data[i+1]:
            data[i+1] = data[i]
    # 왼쪽
    for i in range(1000,max_idx,-1):
        if data[i] > data[i-1]:
            data[i-1] = data[i]

    print(sum(data))













sol()

