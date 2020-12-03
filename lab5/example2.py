#average grade

students = int(input("how many students: "))

average_grades = [] 

for student in range(1,students+1) :
  print(f"student {student}")
  mid1 = int(input("enter your midterm1 grade: "))
  mid2 = int(input("enter your midterm2 grade: "))
  final = int(input("enter your final grade: "))

  average_grade = []
  p1 = mid1*30/100
  p2 = mid2*30/100
  p3 = final*40/100
  average_grade.append(p1)
  average_grade.append(p2)
  average_grade.append(p3)

  average_grades.append(average_grade)

print(average_grades)