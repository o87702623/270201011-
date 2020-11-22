#grad cond

gpa = float(input("enter your GPA: "))
lecture_number = int(input("enter your number of lectures: "))

if gpa < 2.0 :
  if lecture_number < 47 :
    print("not enough GPA and number of lectures")
  else:
    print("not enough GPA")

else:
  if lecture_number < 47 :
    print("not enough number of lectures")
  else:
    print("GRADUATED")