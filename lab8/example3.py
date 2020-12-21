def get_evens(x):
  i = x.pop()
  if i % 2 == 0:
    print(i)
  get_evens(x)

get_evens([0,1,2,3,4,5])