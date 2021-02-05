# 1918 후위 표기식

def sol():
    priority = {"*":1,"/":1,"-":2,"+":2}
    stack =[]
    exp = input()
    answer =''
    for i in range(len(exp)):
        if 65<= ord(exp[i]) <=122:
            answer += exp[i]
        elif exp[i] == "(":
            stack.append(exp[i])
        elif exp[i] == ")":
            # 올바른 식만 나온다는 가정하
            while(stack[-1]!= "("):
                answer += stack.pop()
            # "(" 빼자
            stack.pop()
        else:
            if len(stack) == 0 :
                stack.append(exp[i])

            elif stack[-1] =="(" or priority[stack[-1]] >= priority[exp[i]]:
                stack.append(exp[i])

            elif priority[stack[-1]] < priority[exp[i]]:
                while(1):
                    answer += stack.pop()
                    if len(stack) == 0 or priority[stack[-1]] > priority[exp[i]]:
                        break
    while(stack):
        answer += stack.pop()
    return answer
print(sol())