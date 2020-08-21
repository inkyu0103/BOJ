#11053_2
import bisect

seqLength = int(input())
seq = list(map(int,input().split()))
dp =[]
dp.append(seq[0])

for i in range(1,seqLength):
    if seq[i]> dp[len(dp)-1]:
        dp.append(seq[i])
    elif seq[i] < dp[len(dp)-1]:
        idxval = bisect.bisect_left(dp,seq[i],0,len(dp))
        dp[idxval] = seq[i]

print(len(dp))


