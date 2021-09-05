# 11728 배열 합치기
# 합친 다음 정렬
# 가장 navie 한 방법은 정말 다 더한 다음에 합치면 됨.
# 문제의 의도가 무엇일까.
# 각각을 미리 정렬해놓고, 하나씩 추가하는 것이 맞지 않을까?
import sys
input = sys.stdin.readline

N,M = map(int,input().split())
first_arr = list(map(int,input().split()))
flen = len(first_arr)
second_arr = list(map(int,input().split()))
slen = len(second_arr)

f,s = 0,0
first_arr.sort()
second_arr.sort()

answer = []

while f<flen and s<slen:
    if first_arr[f] <= second_arr[s]:
        answer.append(first_arr[f])
        f += 1
    else:
        answer.append(second_arr[s])
        s+=1

while f<flen:
    answer.append(first_arr[f])
    f+=1

while s<slen:
    answer.append(second_arr[s])
    s+=1

print(*answer)










