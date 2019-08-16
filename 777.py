itr=int(input())
if itr>1:
    for j in range(1,itr+1):
        if(itr%j)==0:
            print(j,end=" ")
