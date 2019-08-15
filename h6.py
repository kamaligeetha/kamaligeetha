san = input()
SS = list(map(int,input().split()))
TT = False
for k in SS:
    if SS.count(k) > 1:
        TT = True
        break
print(k if TT else "unique")
