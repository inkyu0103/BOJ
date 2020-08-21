#LCS

firstL = input()
secondL = input()
countBox = []
count1 = 0
count2 = 0

def solve(first,firstStart,second,secondStart):
    global count1
    # 초과하는 경우
    if firstStart >= len(first) or secondStart >= len(second):
        return

    for i in range(firstStart,len(first)):
        for j in range(secondStart,len(second)):
            if first[i] == second[j]:
                count1 += 1
                return solve(first,i+1,second,j+1)



solve(firstL,0,secondL,0)
countBox.append(count1)
count1= 0
solve(secondL,0,firstL,0)
countBox.append(count1)
print(max(countBox))

