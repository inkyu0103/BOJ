#11047 동전 0

import sys
input = sys.stdin.readline

def sol():
    num,total = map(int,input().split())
    coins = []
    count = 0

    for _ in range(num):
        coins.append(int(input()))

    coins.reverse()


    for coin in coins:
        if not total:
            break

        if coin > total:
            continue

        div = total // coin
        count += div
        total -= div * coin

    print(count)

sol()