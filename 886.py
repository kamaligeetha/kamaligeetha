N=list(input())
A=[]
for j in N:
    if j not in A:
        A.append(j)
if(N==A):
    print("Yes")
else:
    print("No")
