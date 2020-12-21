def is_prime(n):
  if n > 1:
    for i in range(2,n):
      if n % i != 0 :
        return True

def print_primes_between(x,y):
  for i in range(x,y):
    if is_prime(i):
      print(i)

first = int(input("enter the first number:"))
second = int(input("enter the second number:"))
print_primes_between(first, second)



