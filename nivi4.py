sss=input()
ll=[]
for i in range(0,len(sss)):
    for j in range(i+2,len(ss)+1):
        aa=sss[i:j]
        if aa==aa[::-1]:
            ll.append(aa)
ll.sort()
for i in range(0,len(ll)):
    print(ll[i])
