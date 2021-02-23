# 4889 안정적인 문자열
import sys


def sol():
    idx = 1
    while (1):
        count = 0
        string = sys.stdin.readline().strip()

        if string == "":
            print("{}. {}".format(idx, 0))
            idx += 1
            continue

        elif string[0] == '-':
            return

        else:
            stack = []


            for i in string:
                if i == "{":
                    stack.append("{")

                # }가 나온 경우
                else:
                    # 스택이 빈 경우
                    if not stack:
                        count += 1
                        stack.append("{")
                    # 안 빈경우
                    else:
                        # 문자열이 맞는 경우
                        if stack[-1] == "{":
                            stack.pop()
                        # }가 또 나온 경우 이게 문제일거 같은데
                        else:
                            stack.append(i)

            if stack:
                left,right = stack.count("{"),stack.count("}")
                mean = (left+right)//2
                count += max(left,right)-mean

            print("{}. {}".format(idx,count))
            idx += 1
sol()
