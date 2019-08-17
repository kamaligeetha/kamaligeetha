import math
XX,YY=map(int,input().split())
ZZ=math.gcd(XX,YY)
LL=(XX*YY)/ZZ
print(math.ceil(LL))
