# 19947
import sys
input = sys.stdin.readline

def sol():
    H,Y = map(int,input().split())
    cash = [0] * (Y+1)
    cash[0] = H

    for i in range(Y+1):
        # 1년 후
        if i+1 < Y+1 :
            cash[i+1] = int(max(cash[i+1],cash[i]*1.05))
        # 3년 후
        if i+3 < Y+1:
            cash[i+3] = int(max(cash[i+3],cash[i]*1.2))
        # 5년 후
        if i+5 < Y+1:
            cash[i+5] = int(max(cash[i+5],cash[i]*1.35))

    print(cash[Y])

sol()