C1,C2=map(str,input().split())
YY=0
if len(C1)>len(C2):
  C1,C2=C2,C1
P=0
while P<len(C1):
  YY+=(ord(C2[P])-ord(C1[P]))
  P+=1
for P in range(P,len(C2)):
  YY+=ord(C2[P])-ord('A')+1
print(YY)
