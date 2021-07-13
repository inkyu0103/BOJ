# 1165 가운데를 말해요
import sys
import heapq
input = sys.stdin.readline

def say_middle(q):
    if len(q) == 1:
        print(q[0])

    else:
        if len(q) % 2 != 0:
            print(q[len(q)//2])

        else:
            print(min(q[(len(q)-1)//2],q[((len(q)-1)//2)+1]))



def sol():
    N = int(input())
    q = []
    for _ in range(N):
        number = int(input())
        heapq.heappush(q,number)
        say_middle(q)

sol()