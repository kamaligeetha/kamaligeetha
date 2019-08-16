itr=int(input())
PO=[]
DS=0
for k in range (0,itr+1):
    DS=abs((2**k)-itr)
    PO.append(DS)
KK=min(PO)
print(KK)
