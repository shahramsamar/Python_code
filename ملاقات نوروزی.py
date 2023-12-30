vorodi=input().split()
for i in range(len(vorodi)):
    vorodi[i] = int(vorodi[i])
big = max(vorodi)
small = min(vorodi)
jam = big - small
#print(vorodi)
#print(vorodi[i])
#print("max :",big)
#print("min :",small)
print(jam)