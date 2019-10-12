test_str="occurances"
all_freq={}
for i in test_str:
  if i in all_freq:
      all_freq[i]+=1
  else:
      all_freq[i]=1
  print("output is :"+str(all_freq))
