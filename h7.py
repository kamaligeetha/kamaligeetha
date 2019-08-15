A=int(input())
B=list(map(int,input().split()))[:A]
T=[]
for j in range(0,A):
  if(B[j]%2==0 and j%2==1 or B[j]%2==1 and j%2==0):
    T.append(B[j])
print(*T,end="")
