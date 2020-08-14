#14002_1 바이토닉 수열 재도전

seqLength = int(input())
seq = list(map(int,input().split()))
rSeq = seq.copy()
rSeq.reverse()
Dp = [0]*seqLength
reverseDp = [0]*seqLength

'''
1 5 4 2 3 

3 2 4 5 1
'''

# 증가하는 가장 긴 수열
for i in range(seqLength):
    for j in range(i):
        if seq[i]>seq[j] and Dp[i] < Dp[j]:
            Dp[i]=Dp[j]
    Dp[i]+=1

for i in range(seqLength-1,-1,-1):
    for j in range(seqLength-1,i,-1):
        if seq[i]>seq[j] and reverseDp[i] < reverseDp[j]:
            reverseDp[i] = reverseDp[j]
    reverseDp[i] += 1

result = []
for i in range(seqLength):
    result.append(Dp[i]+reverseDp[i]-1)

print(max(result))
