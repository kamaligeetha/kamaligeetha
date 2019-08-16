P=input()
N=len(P)
if N%2!=0:
    P=P[:int(N/2)]+'*'+P[int(N/2)+1:N]
else:
    P=P[:int(N/2)-1]+'**'+P[int(N/2)+1:N]
print(P)
