# 2596 비밀편지
import sys

input = sys.stdin.readline

_mapper = {
    "000000": "A",
    "001111": "B",
    "010011": "C",
    "011100": "D",
    "100110": "E",
    "101001": "F",
    "110101": "G",
    "111010": "H",
}


def sol():
    N = int(input())
    str = input().rstrip()
    answer = ""

    for i in range(N):
        target = str[i * 6 : i * 6 + 6]
        print(target)
        if target not in _mapper:
            print(i + 1)
            break

        answer += _mapper[target]

    if answer:
        print(answer)


sol()
