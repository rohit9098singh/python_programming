with open('mytext2.txt','r') as f:
 while True:
  line=f.readline()
  if not line:
   break
  print(line)
 