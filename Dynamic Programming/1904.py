# 1904 01타일
'''
만들 수 있는 2진 수열의 개수를 15746으로 나눈 값 출력
자연수 입력

1. 같은 것이 있는 순열로 푸나?

2. dp로 안풀고 그냥 수식으로도 풀리는 것 같더라. --> 아니더라 내 착각이네요 연속에서 있는 경우만 생각했네

3. 피보나치 수열이었던 것이다.

'''
import time
start = time.time()

fibo = [1,1]

for i in range(2,1000001):
    fibo.append((fibo[i-2]%15746 + fibo[i-1]%15746)%15746)


N = int(input())

if N == 0 :
    print(0)
else:
    print(fibo[N])


end = time.time()

print("time : {}".format(end-start))

