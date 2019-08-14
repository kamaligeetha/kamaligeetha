M1=int(input())
S1=list(map(int,input().split()))
T1=[]
for j in S1:
    if S1.count(j)==1:
        if j not in T1:
            T1.append(j)
print(*T1)
