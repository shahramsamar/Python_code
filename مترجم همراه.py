dict = {}
result =""
count = int(input())

for i in range(count) :
 vrordi = input().split()
 dict[vrordi[0].strip()] = vrordi[0]
 dict[vrordi[1].strip()] = vrordi[0]
 dict[vrordi[2].strip()] = vrordi[0]
 dict[vrordi[3].strip()] = vrordi[0]
# print(dict)

sentence = input().split()




for word in sentence :
#  print(word)
  result  +=dict.get(word,word)+" "
print(result)




# for this_one in sentence :
#   result +=dict.get(this_one,this_one) + " "
# print(result)

