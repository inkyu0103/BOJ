# 1660
import bisect
import sys
input = sys.stdin.readline

def sol():
    N = int(input())
    bullets = [0,1]
    total_bullets = [0]

    for i in range(2,N):
        bullets.append(bullets[i-1]+i)

    for i in range(1,N):
        total_bullets.append(total_bullets[i-1]+bullets[i])

    count = 0
    print(total_bullets)
    while 1:
        print(N)
        for i in range(len(total_bullets)):
            if N < total_bullets[i]:
                N -= total_bullets[i-1]
                count += 1
            elif N == total_bullets[i]:
                N -= total_bullets[i]
                count += 1

            if N == 1:
                count += 1
                print(count)
                return

            if N == 0:
                print(count)
                return







sol()