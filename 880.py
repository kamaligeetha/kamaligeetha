Y=input()
TT=[]
for k in range(0,len(Y)):
        if(int(Y[k])%2==1):
           TT.append(Y[k])
print(*TT,end="")
