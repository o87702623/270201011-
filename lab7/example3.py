import random 
def get_rand_list(b,e,N):
  lst = random.sample(range(b,e),N)
  return lst

def get_overlap():
  x = set(get_rand_list(0,10,5))
  y = set(get_rand_list(0,10,5))
  intersect = x.intersection(y)
  x = list(x)
  y = list(y)
  intersect = list(intersect)
  return x, y, intersect

print(get_overlap())
  
