import sys
input = sys.stdin.readline

def sol():
    tc = int(input())
    for i in range(tc):
        word = input().strip().split()
        word.reverse()
        print("Case #%d: %s"%(i+1," ".join(word)))
sol()
