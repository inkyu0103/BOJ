#1339

import sys

case = int(input())
Alpha = [0]*26
answer = 0
count = 9
for i in range(case):
    data = sys.stdin.readline().rstrip()

    for j in range(len(data)):
        Alpha[ord(data[j])-65] += 10**(len(data)-(j+1))

Alpha.sort(reverse=True)
for i in Alpha:
    if i !=0 :
        answer += i*count
        count -= 1

print(answer)

#알파벳 정보가 딱히 필요없다는 점을 이용해서 시간 개선.