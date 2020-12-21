import time

def timer(n):
  if n == 0:
    print("end")
    return None
  print(n)
  time.sleep(1)
  return timer(n-1)

timer(5)
