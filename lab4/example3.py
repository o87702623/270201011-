#matching digits

number1 = input("enter a positive integer: ")
number2 = input("enter a positive integer: ")

matches = 0

for i in number1 :
  for j in number2 :
    if i==j :
      matches = matches + 1


print(matches)


