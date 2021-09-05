#19939 re

def sol ():
    N, K = map(int,input().split())

    if N < K*(K+1)/2:
        return -1
    elif (N-K*(K+1)/2) % K == 0 :
        return K-1
    else:
        return K

print(sol())
