class school :
    
    def __init__(student) :
        student_count = int()
        student.school_age = list()
        student.school_height = list()
        student.school_weight = list()
        student.average_age = float()
        student.average_height = float()
        student.average_weight = float()

    def get_student_count(student):
         student_count = int(input())
  
    def get_school_age(student) :
         student.school_age = [int(x) for x in input().split()]
  
    def get_school_height(student) :
         student.school_height = [int(x) for x in input().split()]

    def get_school_weight(student) :
         student.school_weight = [int(x) for x in input().split()]
    
    def get_average_age_all(student) :
           student.average_age = float (sum(student.school_age) / len(student.school_age))
           print(student.average_age)

    def get_average_height_all(student) :
          student.average_height = float(sum(student.school_height) / len(student.school_height))
          print(student.average_height)

    def get_average_weight_all(student) :
         student.average_weight = float(sum(student.school_weight) / len(student.school_weight))
         print(student.average_weight)

    def compare():
          if A.average_height == B.average_height and A.average_weight == B.average_weight  :
               print("same")

          elif A.average_height == B.average_height and A.average_weight > B.average_weight :
                 print("B")

          elif A.average_height == B.average_height and A.average_weight < B.average_weight :
                 print("A")   

          elif A.average_height > B.average_height :
                print("A")
          elif A.average_height < B.average_height :
                print("B")


A = school()
B = school()

A.get_student_count()
A.get_school_age()  
A.get_school_height() 
A.get_school_weight()

B.get_student_count()
B.get_school_age()  
B.get_school_height() 
B.get_school_weight()

A.get_average_age_all()
A.get_average_height_all()
A.get_average_weight_all()

B.get_average_age_all()
B.get_average_height_all()
B.get_average_weight_all()
school.compare()