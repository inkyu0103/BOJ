# 2504 괄호의 값


def sol():
    string = input()
    stack = []
    tmp = 1
    answer = 0
    box = ["(",")","[","]"]
    # 이왕이면 인덱스로 접근하자
    # 언제 스택을 보고 언제 stirng을 보나?

    for i in range(len(string)):
        if string[i] not in box:
            return 0

        if string[i]=="(" :
            tmp*=2
            stack.append(string[i])

        elif string[i]=="[":
            tmp*=3
            stack.append(string[i])

        elif string[i]==")":
            if len(stack)==0:
                return 0

            elif string[i-1] == "[" or stack[-1] == "[":
                return 0

            elif string[i-1] == ")" or string [i-1] == "]":
                stack.pop()
                tmp /= 2

            elif string[i-1] == "(" and stack[-1] == "(":
                stack.pop()
                answer += tmp
                tmp /= 2


        elif string[i] == "]":
            if len(stack) == 0:
                return 0
            elif string[i-1]=="(" or stack[-1] =="(":
                return 0
            elif string[i-1] == ")" or string[i-1] =="]":
                stack.pop()
                tmp /= 3
            elif string[i-1]=="[" and stack[-1] == "[":
                stack.pop()
                answer += tmp
                tmp /= 3


    if len(stack) != 0:
        return 0

    return int(answer)
print(sol())
