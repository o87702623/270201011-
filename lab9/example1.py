def mltp_of_3(n):
  if n == 1 :
    return 3
  else:
    return 3 + mltp_of_3(n-1)

print(mltp_of_3(10))

