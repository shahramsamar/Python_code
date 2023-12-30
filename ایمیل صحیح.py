import re
# regex = (r'([A-Za-z0-9])+@[a-z|A-Z]+(\.[a-z|A-Z])') 
regex = (r'\w+\@\w+\.\w+')
username = input()
if re.match(regex,username):
     print('OK')
else:
     print('WRONG')

