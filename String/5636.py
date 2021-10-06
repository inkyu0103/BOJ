# 5636 발상을 반대로...!

import sys
input = sys.stdin.readline

def sol():
    li = [1] * (100001)
    for i in range(2, int(100000 ** 0.5) + 1):
        if li[i]:
            for j in range(i + i, 100001, i):
                li[j] = 0
    prime = [i for i in range(2, 100001) if li[i]]

    while 1:
        val = input().strip()
        if val == '0':
            break

        result = 2
        for target in prime:
            if str(target) in val:
                result = target
        print(result)




sol()