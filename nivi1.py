sst2,sst3= input().split()
for j in range(0,len(sst2)-len(sst3)+1):
  if sst2[j:len(sst3)+j] == sst3:
    print('yes')
    break
else:
  print('no')
