# 14916 거스름 돈
n = int(input())

count = 0

while n > 0:
    if n % 5 == 0:
        print(n // 5 + count)
        break

    n -= 2
    count += 1

if n < 0:
    print('-1')