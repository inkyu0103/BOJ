# 2504 괄호의 값


def sol():
    string = input()
    stack = []
    tmp = 1
    answer = 0
    # 이왕이면 인덱스로 접근하자
    # 언제 스택을 보고 언제 stirng을 보나?
    try:
        for i in range(len(string)):
            if string[i] == "(":
                stack.append(string[i])
                tmp *= 2

            elif string[i] == "[":
                stack.append(string[i])
                tmp *= 3

            elif string[i] == ")" :
                # 두개 다 봐야하나 ?
                if stack[-1] == "(" and string[i-1] == "(":
                    stack.pop()
                    answer +=  tmp
                    tmp /= 2

                elif string[i-1] == ")" or string[i-1] =="]":
                    stack.pop()
                    tmp /= 2

                elif len(stack) ==0 or stack[-1] != "(":
                    return 0

            elif string[i] == "]":
                if stack[-1] == "[" and string[i-1]=="[":
                    answer += tmp
                    tmp /= 3
                    stack.pop()

                elif string[i - 1] == ")" or string[i-1]=="]":
                    tmp /= 3
                    stack.pop()

                elif len(stack) == 0 or string[i - 1] != "[":
                    return 0

    except :
        return 0
    return int(answer)


print(sol())
