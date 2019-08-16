itr=int(input())
if itr>1:
    for j in range(2,itr):
        if(itr%j)==0:
            print("yes")
            break
    else:
        print("no")
