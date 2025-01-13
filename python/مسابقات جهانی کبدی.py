count=0
tedad_bazikon = input()
tedad_match = input().split()
for i in range(len(tedad_match)):
    tedad_match[i]=int(tedad_match[i])
    if tedad_match[i] <= 2 :
        count=count+1
       # print(i)
        #tedad_team = i // 3
#print("tedad_bazikon :",tedad_bazikon)
#print("tedad_match :",tedad_match)
#print("tedad_team :",tedad_team)
#print(tedad_team)
print(count//3)
#print("count :",count//3)
#print(count)