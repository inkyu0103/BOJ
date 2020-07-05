#2748 피보나치 수 2

userInput = int(input())

Fibo = [0,1]

if userInput > 1:

    i=0
    while(1):
        Fibo.append(Fibo[i]+Fibo[i+1])

        if len(Fibo) == userInput+1:

            break
        else:

            i += 1

    print(Fibo[userInput])

else:
    print(Fibo[userInput])
