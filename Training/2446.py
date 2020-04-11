#2446 별찍기 -9 오... 알고랩에서 나온거네

in_ = int(input())

for i in range(2*in_-1):
    if i <in_:
        print(i*" "+"*"*(2*in_-1 -2*i))

    else:
        print((2*in_-1-i-1)*" "+"*"*(2*(i-in_)+3))
