zzz1=int(input())
nnn=list(map(int,input().split()))
xx=0
for j in range(zzz1):
    if sum(nnn[:j])==sum(nnn[j+1:]):
        xx=xx+1
if xx>0:
    print("yes")
else:
    print("no")
