string =input().lower()
a=""
for i in string:
    a=i+a
#print(a)    
if string==a:
    print("palindrome")
else:
    print("not palindrome")
