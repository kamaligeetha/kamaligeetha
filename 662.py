S=input()
FF=0
for k in S:
    if k!='0' and k!='1':
        print("no")
        FF=1
        break
if FF==0:
    print("yes")
