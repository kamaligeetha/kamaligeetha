L=input()
CC=0
for k in L:
  if (k.isdigit() or k.isalpha()):
    CC+=1
if CC!=0:
  print("Yes")
else:
  print("No")
