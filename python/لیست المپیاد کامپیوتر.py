list =[]
count =int(input())
for i in range(count) :
    name = input().split(".")
    list.append(name[0] + " " + name[1].capitalize() + " " + name[2])

# print(list)
list.sort()
for i in list :
    print(i)