def maghsom(a) :
    for i in range(2,int(a /2)+1):
      if a % i == 0 :
       return False
    return True  


numbers = []
for i in range(10) :
  number = int (input())
  numbers.append(number)

# print(number)
max_number = 0
max_prime_divisors = 0

for number in numbers :
  prime_divisors = 0
  for i in range(2,number) :
      if number % i == 0 and maghsom(i) :
        prime_divisors+= 1
  if prime_divisors > max_prime_divisors :
   max_prime_divisors = prime_divisors
   max_number = number
  elif prime_divisors == max_prime_divisors and number > max_number :
       max_number = number    
        
print (max_number,max_prime_divisors)
  