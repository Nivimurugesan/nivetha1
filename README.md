aa1,bb1=input().split()
aa1=int(aa1)
bb1=int(bb1)
ss2=''
uu1=2
if(aa1+bb1<=3):
    for i in range(0,aa1+bb1):
        if(i%2!=0):
            ss2=ss2+'0'
        else:
            ss2=ss2+'1'
else:    
    for i in range(0,aa1+bb1):
        if(i==uu1):
            ss2=ss2+'0'
            if(uu1==bb1):
                uu1=uu1+2
            else:
                uu1=uu1+3
        else:
            ss2=ss2+'1'
xx1=len(ss2)-1
if(int(ss2[xx1])==0):
    print('-1')
elif aa1==1 and bb1==2: print("011")
else:
    print(ss2)
