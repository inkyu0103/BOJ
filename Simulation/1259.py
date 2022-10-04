# 1259

import sys
input = sys.stdin.readline

def sol():
    while True:
        input_string = input().strip()
        if input_string == '0':
            break

        if len(input_string) == 1:
            print('yes')
            continue

        if len(input_string) % 2 == 0 and input_string[:len(input_string)//2] == input_string[(len(input_string)//2):][::-1]:
            print('yes')
            continue

        if input_string[:len(input_string)//2] == input_string[(len(input_string)//2)+1:][::-1]:
            print('yes')
            continue

        print('no')

sol()
