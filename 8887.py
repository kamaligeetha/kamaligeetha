NN=list(input())
AA=[]
for j in NN:
    if j not in AA:
        AA.append(j)
if(NN==AA):
    print("Yes")
else:
    print("No")
