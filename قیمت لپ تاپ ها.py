result = 0
item_laptop = int(input())
count = item_laptop
list1 = list()
for i in range(count):
    new_list = input().split()
    list1.append(new_list)
    #لسیت لپ تا ها رو میده
    #قیمت وکیفیت رو بررسی می کنه
for i in range(len(list1)): 
    for j in range(1,len(list1)):
        if int(list1[i][0]) < int(list1[j][0]) and  int (list1[i][1]) > int(list1[j][1])  :
         result+=1
         break
if result > 0:
   print("happy irsa") 
else:
  print("poor irsa")       

