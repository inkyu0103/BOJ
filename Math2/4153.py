#4153 직각삼각형
import math
while(1):
    #각각의 변 길이
    a,b,c = map(int,input().split())
    # a,b,c =0 일때
    if(a==0 and b==0 and c== 0 ):
        break

    else:
        if pow(a,2)+pow(b,2)+pow(c,2)-2*pow(max(a,b,c),2) == 0:
            print("right")
        else:
            print("wrong")


