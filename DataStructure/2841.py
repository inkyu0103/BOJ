# 2841

# 자기보다 낮은 음이 들어오면 계속 손을 뗴야 한다.
# 줄별로 스택을 따로 관리 해야겠다.
import sys


def sol():
    N, P = map(int, sys.stdin.readline().split())
    stack = [[] for i in range(N+1)]
    answer = 0
    while (1):
        try:
            line, plat = map(int,sys.stdin.readline().split())

            if len(stack[line]) == 0 :
                stack[line].append(plat)
                answer += 1
            else:
                # 스택이 안 비었으니 여기로 왔다.
                if stack[line][-1] > plat :
                    while stack[line] and stack[line][-1] > plat:
                        stack[line].pop()
                        answer += 1

                    # 스택이 빈 경우
                    if len(stack[line]) == 0 :
                        stack[line].append(plat)
                        answer += 1

                    elif stack[line][-1] < plat :
                        stack[line].append(plat)
                        answer += 1
                elif stack[line][-1] < plat:
                    stack[line].append(plat)
                    answer += 1

        except:
            print(answer)
            return
sol()
