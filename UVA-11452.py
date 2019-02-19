def same(s, sz):
  for i in range(sz):
    if (s[i] != s[sz+i]):
      return False
      
  for i in (2*sz,len(s)-1):
    if i==len(s):
      return True
    if (s[i-(2*sz)] != s[i]):
      return False
  
  return True

a=int(input())
while a>0:
  a-=1
  b=input()
  n=len(b)//2
  while True:
    if same(b,n):
      break
    n-=1  
  cur = len(b) - (2 * n)
  for i in range(8):
    print(b[cur],end="")
    cur+=1
    if (cur == n):
        cur = 0
  print("...")
  
  

  
