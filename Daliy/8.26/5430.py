from collections import deque
import sys
input = sys.stdin.readline


def sol():
    tc = int(input())
    for _ in range(tc):
        command = input().strip()
        num = int(input())
        user_input_arr = input().strip()

        # [] 인 경우
        if not num:
            if "D" in command:
                print("error")
            else:
                print("[]")
            continue

        else:
            # remove bracket
            user_input_arr = deque(list(user_input_arr[1:-1].split(",")))
            command_idx = 0
            # 0이면 앞에서 , 1이면 뒤에서
            direction = True
            error_flag = 0


            while(command_idx<len(command)):
                if command[command_idx] == "R":
                    direction = not direction


                else:
                    if not user_input_arr:
                        error_flag = 1
                        print("error")
                        break

                    if direction:
                        user_input_arr.popleft()

                    else:
                        user_input_arr.pop()


                command_idx += 1

            result = list(user_input_arr)

            if not direction:
                result.reverse()

            if not error_flag:
                print("[" + ",".join(result)+"]")

sol()