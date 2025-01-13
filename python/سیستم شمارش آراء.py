
tedad_kol_ara = int(input())
count = tedad_kol_ara
Dict={}
for i in range(count) :
     name_dic =  input().lower()
     Dict[name_dic] = Dict.get(name_dic, 0) + 1
for k,v in sorted(Dict.items()):
     print(k,v)
