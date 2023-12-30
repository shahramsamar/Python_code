
# genre = [['Romance', 'History', 'action'], ['Adventure', 'action', 'History'],
#   ['horror', 'action', 'Comedy'], ['horror', 'Romance', 'Comedy']]
genre =[]
genres= {'Horror':0 ,'Romance':0,'Comedy':0,'History':0 ,'Adventure':0 ,'Action':0}
count = int(input())
for item in range(count) :
    name = input().split(" ")
    genre.append(name[1:])
# print(name) 
# print(genre)
for i in genre :
    # print(i)
    if 'horror'  in i or 'Horror'  in i  :
        genres['Horror'] += 1
    if  'Romance' in i or 'romance' in i  :
         genres['Romance'] += 1
    if  'Comedy' in i or 'comedy' in i :
         genres['Comedy'] += 1
    if  'History' in i  or 'history' in i:
         genres['History'] += 1
    if  'Adventure' in i or 'adventure' in i :
         genres['Adventure'] += 1
    if  'Action' in i  or 'action' in i :
         genres['Action'] += 1                
# print(genres)
for genre,count in sorted(genres.items(),key=lambda item:(-item[1],item[0])):
     print(f"{genre} : {count}")