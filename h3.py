O=int(input())
P=list(map(int,input().split()))
M=[]
for j in range(O):
    if P[j]==j:
        M.append(str(P[j]))
        M.sort()
if len(M)==0:
    print("-1")
else:
    print(" ".join(M))
