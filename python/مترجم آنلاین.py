
count = int(input())

dict = {}

for i in range(count) :
 vrordi = input().split()
 dict[vrordi[0]] = vrordi[1]

sentence = input().split()
result =""

for this_one in sentence :
#  if this_one in dict :
#   result += dict[this_one] +" "
#  else:
#   result += this_one +" "
  result +=dict.get(this_one,this_one) + " "
print(result)
#print(item)
