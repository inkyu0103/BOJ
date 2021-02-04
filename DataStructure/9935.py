#9935 문자열 폭발

def sol():
    myStr = input()
    exploseStr = input()
    # 마지막 단어가 들어올 때 확인하는건데 마지막 단어만 들어오는 경우가 최악의 케이스
    checkStr = exploseStr[-1]
    exploseStr = exploseStr[:-1]


    stack = []

    for i in range(len(myStr)):
        if len(stack) == 0 :
            stack.append(myStr[i])
        else:
            flag = 0
            # 끝 문자이고, 스택의 길이가 더 길다면
            if myStr[i] == checkStr and len(exploseStr) <= len(stack):
                for i in range(len(exploseStr)):
                    if stack[len(stack)-i-1] == exploseStr[len(exploseStr)-i-1]:
                        continue
                    else:
                        # break를 표시하는 flag
                        # 만약에 안 맞으면 얘도 추가해야함
                        stack.append(checkStr)
                        flag = 1
                        break
                if flag == 0 :
                    for i in range(len(exploseStr)):
                        stack.pop()

            elif myStr[i] != checkStr:
                stack.append(myStr[i])

    if len(stack) == 0:
        return "FRULA"
    else:
        return "".join(stack)
print(sol())
