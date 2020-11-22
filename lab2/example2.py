#minimum value

num1 = int(input("enter 1st value: "))
num2 = int(input("enter 2nd value: "))
num3 = int(input("enter 3rd value: "))

if num1 < num2 and num3 :
  print(f"min value is {num1}")
elif num2 < num1 and num3 :
  print(f"min value is {num2}")
elif num3 < num1 and num2 :
  print(f"min value is {num3}")

