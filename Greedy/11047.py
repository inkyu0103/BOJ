# 11047 동전 0

import sys
input = sys.stdin.readline

<<<<<<< HEAD
Kinds, Cost = map(int, sys.stdin.readline().split())
coin = []
startPoint = 0
sum = 0
count = 0
for _ in range(Kinds):
    coin.append(int(sys.stdin.readline()))
coin.reverse()

for i in range(Kinds):
    if coin[i] < Cost:
        startPoint = i
        break

while 1:
    if sum == Cost:
        print(count)
        break

    else:
        if sum + coin[startPoint] > Cost:
            startPoint += 1
            continue
        else:
            sum += coin[startPoint]
            count += 1
=======
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
>>>>>>> 0d66d1a3a1007870ae778327019ad315588afd8e
