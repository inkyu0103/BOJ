# 9935 문자열 폭발

def sol():
    userInput = input()
    boomWord = input()

    boomWordLength = len(boomWord)
    lastWord = boomWord[-1]
    stack = []

    for c in userInput:
        if c != lastWord:
            stack.append(c)

        else:
            try:

                # 맞는 경우 --> pop 왜 boomWord가 None으로 취급되지?
                if "".join(stack[-boomWordLength:]) == boomWord[:-1]:
                    for i in range(boomWordLength):
                        stack.pop()
                # 다른 경우
                else:
                    stack.append(c)

            except:
                # 인덱스 에러
                stack.append(c)


    if len(stack) == 0:
        return "FRULA"
    else:
        return "".join(stack)


print(sol())
