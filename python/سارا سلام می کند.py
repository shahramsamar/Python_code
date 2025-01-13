string=input().lower()
count=0
if 'h'in string:
     string=string[string.find('h')+1:]

     count+=1
     #print('h','0')

if 'e'in string:
    string=string[string.find('e')+1:] 
    
    count+=1
    #print('e','1')

if 'l'in string:
    string=string[string.find('l')+1:] 

    count+=1
    #print('l','2')   
    
if 'l'in string:
     string=string[string.find('l')+1:] 

     count+=1
    #print('l','3')  
     
if 'o'in string:
    string=string[string.find('o')+1:] 
  
    count+=1 
    #print('o','4')

if count==5:
    print('YES' )
else:
    print('NO')

