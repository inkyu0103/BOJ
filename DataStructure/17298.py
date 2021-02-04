# 17298 오큰수
import sys

'''
일반적으로 풀었을 때 : 최악의 경우 O(N^2)의 상황
3 5 2 7 
      3     5    2     7
    ㅡㅡㅡ ㅡㅡㅡ ㅡㅡㅡ ㅡㅡㅡ
3 |   x     5     5    5          4 5 6 7 
5 |   x     x                     5 6 7 -1
2 |   x     x     x                  
7 |   x     x     x    x 

자신보다 큰 수가 나오면 pop / 그리고 그 값 넣기

2493 탑을 거꾸로 한거랑 똑같네?
같은 경우는 우째?
'''


def sol():
    case = int(input())
    data = list(map(int,sys.stdin.readline().split()))[::-1]
    stack = []
    answer = [0]*case
    answer[0] = -1

    for i in range(case):
        if i==0:
            stack.append(data[i])


        elif stack and stack[-1] <= data[i]:
            while 1:
                stack.pop()
                if stack and stack[-1] <= data[i]:
                    continue
                else:
                    break

            if not stack:
                answer[i] = -1
            else:
                answer[i] = stack[-1]
            stack.append(data[i])

        elif stack and stack[-1] > data[i]:
            answer[i] = stack[-1]
            stack.append(data[i])

    for i in range(len(answer)-1,-1,-1):
        print(answer[i],end=" ")

sol()