
people = int(input())
cute =0
nocute = 0

for i in range(people):
    val = int(input())
    if val == 1:
        cute+=1
    elif val == 0 :
        nocute += 1
    else:
        pass

if cute > nocute:
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")