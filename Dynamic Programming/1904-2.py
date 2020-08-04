# 반복적 동적 계획법 - 이렇게 하면 메모리 에러가 생긴다.
N = int(input())


def fibo(x):
    cache = [0 for _ in range(x+1)]
    cache[1] = 1

    for i in range(2,x+1):
        cache[i] = cache[i-2]+cache[i-1]

    return cache[x]


print(fibo(N+1))