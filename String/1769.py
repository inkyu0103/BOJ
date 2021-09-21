# 1769 3의 배수

import sys
input = sys.stdin.readline

N = input().strip()
result = 0
cnt = 0

while 1:
    #합을 구한다.
    arr = list(map(int,N))

    if len(arr) == 1:
        result = sum(arr)
        break

    else:
        N = str(sum(arr))
        cnt += 1

print(cnt)
print("NO" if result%3 else "YES")

