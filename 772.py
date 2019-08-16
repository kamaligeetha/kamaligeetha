KL=input()
FF=0
bd=list('aeiouAEIOU')
for j in KL:
    if j in bd:
        print("yes")
        FF=1
        break
if FF==0:
    print("no")
