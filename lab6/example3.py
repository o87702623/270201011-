employees = {}
n = 1
while n <= 5 :
  print(f"EMPLOYEE {n}")
  name = input("name: ")
  salary = int(input("salary: "))
  employees.update({name:salary})
  n += 1

print(employees)

