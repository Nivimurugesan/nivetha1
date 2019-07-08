pp=int(input())
qq=list(map(int,input().split()))
cc=1
for i in qq:
    if qq.count(i)>cc:
        rr=i
        cc=qq.count(i)
print(rr)
