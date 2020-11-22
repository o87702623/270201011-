#password checker

password = "abc123"

guess = input("enter the password ")

while guess != password :
  print("wrong")
  guess = input("enter the password ")

  for i in password :
     if guess == "help" :
       print(i)


if guess == password :
  print("correct")

  
