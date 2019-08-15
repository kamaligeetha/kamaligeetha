N=list(map(str,input()))
SS=CC=0
for k in range(0,len(N)-1):
  Q=N[k]
  if int(Q)!=0:
   for i in range(k+1,k+2):
    Q=Q+N[i]
    if int(Q)<27 and int(Q)>0: SS=SS+1
    elif int(Q)==0: SS=SS-1
    else: break
if SS!=1: CC=SS%2
print(SS+CC+1)
