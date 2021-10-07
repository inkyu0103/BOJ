# 16916
import sys,re
input = sys.stdin.readline

# 길이가 100만인게 두렵다.
def sol():
    string=input().rstrip()
    sub_string = input().rstrip()

    pat = re.compile(sub_string)
    print(1 if re.search(pat,string) else 0)


sol()
