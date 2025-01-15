list = []
count = 0
found = False
string = input().split(".")
# print(string)
for i in string :
     for index,word in enumerate(i.strip().split(" ")) :
         count += 1
        # print(index,word)
         if str(word).istitle() and index != 0 :
             print(f"{count}:{word.replace(',','').replace(',','')}")
             found = True

if not found :
  print("None")  
