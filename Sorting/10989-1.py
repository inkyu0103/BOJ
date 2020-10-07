# 카운팅 정렬
# 입력 받는 숫자에 현혹되면 메모리 초과가 나기 십상이다.
# 최대 숫자가 10000까지밖에 나오지 않는다.
# 처음부터 모든 수를 배열에 넣을 필요가 없다.
# 나오는 수는 자연수임을 고려.

import sys

num = int(input())
if num <= 10000:
    B = [0]*(num+1)
else:
    B = [0]*10001

# stable 하지 않아도 되나?
for i in range(num):
    B[int(sys.stdin.readline())] += 1

for i in range(len(B)):
    if B[i] != 0 :
        for j in range(B[i]):
            print(i)











