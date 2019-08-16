from itertools import combinations
A,K=map(int,input().split())
B=len(str(A))
LL=list(combinations(str(A),B-K))
LL=sorted(LL)
print(*LL[0],sep='')
