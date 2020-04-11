#10996
in_ = int(input())

for i in range(2*in_):
    result = ""
    for j in range(in_):
        if i % 2 == 0 :
            if j % 2 == 0 :
                result += "*"
            else:
                result += " "

        else:
            if j % 2 == 0 :
                result += " "

            else :
                result += "*"
    print(result)