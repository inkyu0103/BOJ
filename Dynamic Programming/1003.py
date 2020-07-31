# 피보나치 함수
'''
메모이제이션을 구현하면 되지 않을까
어떻게 기억해 놓을까
분할되는 값이 의존적인데 --> dynamic

f(5) -->f(4)+f(3) --> {f(3)+f(2)} + {f(2)+f(1)} -->[f(2)+f(1) + f(1)+f(0) + f(1)+f(0) + 1]

x번째 피보나치 수


1. 처음에 [1,0],[0,1] 을 기초로 40번째까지 구해 놓는다. 오 뭐야 맞았네
'''
import sys

testCase = int(input())
box = [[0,0] for i in range(41)]
box[0][0] = 1
box[1][1] = 1

# append 하는게 시간이 덜 걸리나?

for i in range(2,41):
    box[i][0]= box[i-1][0]+box[i-2][0]
    box[i][1]= box[i-1][1]+box[i-2][1]

for i in range(testCase):
    num = int(sys.stdin.readline())
    print(box[num][0],box[num][1])











