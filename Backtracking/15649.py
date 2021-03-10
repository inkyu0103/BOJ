#15649 N과 M (1)

from itertools import permutations

def sol():
    N,M = map(int,input().split())
    arr = [i for i in range(1,N+1)]
    for i in permutations(arr,M):
        for j in i:
            print(j,end=" ")
        print()
sol()

