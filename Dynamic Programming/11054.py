#11054 바이토닉 수열

def findSmall(start,seqKind,dparr):
    if dparr[start] != -1:
        return dparr[start]

    baseVal = 1
    for next in range(start+1,seqLength):
        if seqKind[start]>seqKind[next]:
            baseVal = max(baseVal, findSmall(next,seqKind,dparr)+1)
        else:
            findSmall(next,seqKind,dparr)
    dparr[start] = baseVal
    return baseVal




if __name__ == "__main__":
    seqLength = int(input())
    seq = list(map(int, input().split()))

    if seqLength == 1 or seqLength == 2 :
        print(0)

    else:
        reverseSeq = seq.copy()
        reverseSeq.reverse()

        Dp = [-1] * seqLength
        reverseDp = [-1] * seqLength

        findSmall(0, seq, Dp)
        findSmall(0, reverseSeq, reverseDp)

        print(Dp)
        print(reverseDp)
        result= []
        for i in range(seqLength):
            result.append(Dp[i]+reverseDp[seqLength-1-i])

        print(max(result)-1)


'''


'''