# 16719 ZOAC
import sys
input = sys.stdin.readline

data = list(enumerate(list(input().strip())))
length = len(data)
data.sort(key=lambda x:ord(x[1]))

initial = ['']*length

for idx,target in data:
    initial[idx] = target
    print("".join(initial))



