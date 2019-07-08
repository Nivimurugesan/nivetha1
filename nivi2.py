Xx=int(input())
tt=[]
for ii in range(0,Xx):
    for jj in range(ii,Xx):
        tt.append("1")
    print(*tt,sep=" ")
    tt=[]
