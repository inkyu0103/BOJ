# 1918 후위표기식
import sys
input = sys.stdin.readline

exp = input().strip()
stack = []
operator = {
    '+':0,
    '-':0,
    '*':1,
    '/':1,
    '(':2,
    ')':2
}
answer =''

for c in exp:
    # c가 연산자인 경우
    if c in operator:
        # 스택이 비어있는 경우
        if not stack or c == '(':
            stack.append(c)

        # ( stack and c!='c' + a) 자신이 들어오는 경우가 더 높은 경우
        elif  operator[stack[-1]] < operator[c]:
            stack.append(c)

        # 자신이 들어오는 경우와 같거나 더 작은 경우
        elif operator[stack[-1]] >= operator[c]:
            while stack and





    # 문자열인 경우
    else:
        answer += c


print(answer)
