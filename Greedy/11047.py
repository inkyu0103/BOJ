# 11047 동전 0

import sys

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
