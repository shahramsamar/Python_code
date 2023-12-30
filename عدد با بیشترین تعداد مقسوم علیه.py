def maghsom(a):
    c=0
    for i in range(1,a+1):
     if a % i==0:
      c+=1
    return c
b=0
c=0
for i in range(20):
  a=int(input())
  maghsom(a)
  if maghsom(a)>c :
    c=maghsom(a)
    b=a 
  elif maghsom(a)==c and a>b:
    
    b=a
   
print(b,c)