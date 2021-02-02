# 1918 후위 표기식
def sol():
    priority = {"*":1,"/":1,"+":2,"-":2,"(" : 3}
    operator = ["+","*","/","-","(",")"]
    stack = []
    answer = ""

    exp = input()

    for i in range(len(exp)):
        if exp[i] not in operator:
            answer += exp[i]
        # 연산자일 때
        elif exp[i] in operator:
            # 아무것도 들어있지 않다면 곧바로 넣는다. (잘못된 식이 없다고 가정하면)
            if len(stack) == 0 :
                stack.append(exp[i])

            elif exp[i] == "(":
                stack.append(exp[i])

            elif exp[i] == ")":
                while(stack and stack[-1] != "("):
                    answer += stack.pop()
                stack.pop()
        else:
            while stack and priority[exp[i]] >= priority[stack[-1]]:
                answer += stack.pop()
            stack.append(exp[i])

    while(stack):
        answer += stack.pop()



    return answer
print(sol())
