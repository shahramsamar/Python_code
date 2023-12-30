big_1=0
big_2=0
age=0
while age !=-1:
  age=int(input()) 
  if age > big_1 :
      big_2=big_1
      big_1 = age   
  elif age>big_2:
         big_2=age
  
       
      
 
print(big_1,big_2)