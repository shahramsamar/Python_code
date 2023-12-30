string = input().lower()
s = string.find("ab")
ss =string.find("ba") 
if s == -1 or ss == -1 :
    print("NO")
elif s < ss:
     string = string.replace("ab","X",1)
     if "ba" in string :
          print("YES")
     else:
          print("NO")
else:
     string= string.replace("ba","X",1) 
     if "ab" in string:
         print("YES")
     else:
          print("NO")

#print(string)
#print(s)
#print(ss)

