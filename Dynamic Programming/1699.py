# 1699 제곱수의 합

import sys
input = sys.stdin.readline

def sol():
    N = int(input())
    if N % 2 == 1:
        print("SK")
    else:
        print("CY")

sol()
