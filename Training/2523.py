#2523 별 찍기 -13

u_input = int(input())
for i in range(u_input*2-1):
    if i<u_input:
        print("*"*(i+1))
    else:
        print("*"*(u_input*2-1 -i))