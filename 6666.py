itr=int(input())
if(itr>1):
    for k in range (2,itr):
        if(itr%k)==0:
            print("no")
            break
    else:
        print(yes)
else:
    print(no)
