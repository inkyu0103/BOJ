# 13699
import sys
input = sys.stdin.readline

def sol():
    N = int(input())
    t = [0] * 36
    t[0],t[1] = 1,1
    for i in range(2,36):
        tmp = 0
        for j in range(i):
            tmp += t[j]*t[i-j-1]
        t[i] = tmp

    print(t[N])
sol()
