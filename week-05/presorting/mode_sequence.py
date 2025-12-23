A = [3,3,3,1,2,0,0,0,0]
n = len(A)

i = 0
freqeuncy = 0

while i <= n -1:
    runlength = 1
    runvalue = A[i]
    while i+ runlength <= n-1 and A[i+runlength] == runvalue:
        runlength += 1
    if runlength > freqeuncy:
        freqeuncy = runlength
    i += runlength

print(freqeuncy)