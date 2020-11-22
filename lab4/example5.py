#fibonacci

n = int(input("how many fibonacci numbers? "))

a = 1
b = 1
fibo = [a, b]

while len(fibo) < n :
  c = a + b
  fibo.append(c)
  a = b
  b = c

print(fibo)