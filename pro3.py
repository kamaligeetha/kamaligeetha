K,L=input().split()
CC=abs(len(L)-len(K))
for j in range(len(K)):
  if(len(L)==1 and L[j] in K):
    break
  if(K[j]!=L[j]):
    CC=CC+1
print(CC)
