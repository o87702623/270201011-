#ticket

age = int(input("enter your age: "))

if age <= 6 or age >= 60 :
  print("your ticket is free")
elif 6 < age < 18 :
  print("your ticket is %50 off") 
elif 18 < age < 60 :
  print("you need to pay 3 tl")

