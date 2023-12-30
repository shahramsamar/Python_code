from datetime import date
class birth :
    result = 0
    def __iniit__(self,age,today) :
       birth.result =int()
       self.age = list ()
       self.today = list()

    def calculate_today(self) :
         self.age =  [int(x) for x in input().split("/")] 
        #  print(self.age)
         today = date.today()
        #  print(today)
           
         if self.age[1] > 12  or self.age[2] > 31 or  self.age[0] > today.year :
              print("WRONG")

         elif self.age[1] >= 12 :
                birth.result += 1
                birth.result += (today.year - self.age[0])
                print(birth.result)
                
         elif self.age[0] < today.year and self.age[1] < 12 and self.age[2] < 31:
               birth.result += today.year - self.age[0] -((today.month,today.day)<(self.age[1],self.age[2]))
               print(birth.result)

birthday = birth()
birthday.calculate_today()