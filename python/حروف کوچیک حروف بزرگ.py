count_lower = 0
count_upper = 0
string = input()
kochik = "abcdefghijklmnopqrstuvwxyz"
bozorg = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in string : 
    if i in bozorg :
         count_upper=count_upper+1
        # print("upper",count_upper)  
    elif i in kochik :
         count_lower=count_lower+1
        # print("lower",count_lower)

if count_upper > count_lower :
     print(string.upper())
elif count_lower > count_upper or count_upper==count_lower:
     print(string.lower())
