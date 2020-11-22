#roots

a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

discriminant = b**2 - 4*a*c

if discriminant < 0 :
  print("there are two complex roots")
elif discriminant == 0 :
  print("there is one real root")
else :
  print("there are two real roots")