#11399 ATM
import sys

case = int(input())
sum = 0
a = list(map(int,sys.stdin.readline().split()))
a.sort()

for i in range(0,len(a)):
    sum+=a[i]*(len(a)-i)

print(sum)