# 9935 문자열 폭발


def sol():
    userData = input()
    boom = input()
    textCheck = boom[-1]
    textCheckLength = len(textCheck)
    stack = []
    answer = ''

    for i in range(len(userData)):
        if userData[i] not in  boom:
            answer+=userData[i]
        # 마지막 단어일 때
        else:
            if userData[i] == textCheck:
                try:
                    # 정상적으로 다 있을 때
                    if stack[-textCheck:] == boom[:-1]:
                        for i in range(textCheckLength):
                            stack.pop()
                    # 같지 않을 때
                    else:
                        for i in range(textCheckLength):
                            answer += stack.pop()
                        answer += textCheck

                # stack의 범위가 문제가 있을 때.
                except:
                    stacklen = len(stack)
                    for i in range(stacklen):
                        answer += stack.pop()
                    answer += textCheck
            else:
                stack.append(userData[i])
    print(answer)
sol()
