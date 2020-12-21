def reverse_list(x):
  if len(x) == 0:
    return []
  return [x.pop()] + reverse_list(x)

print(reverse_list([1,2,3,4]))

