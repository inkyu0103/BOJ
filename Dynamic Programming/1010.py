#1010

import math
def nCr(n,r):
    f = math.factorial
    return int(int(f(n)) // int(f(r)) // int(f(n-r)))


tc = int(input())

for i in range(tc):
    r , n =map(int,input().split())
    print(nCr(n,r))
