numbers1 = [2, 3, 4, 20, 5, 5, 15]
numbers2 = [10, 20, 20, 15, 30, 40]

set1 = set(numbers1)
set2 = set(numbers2)

intersection = set()
for x in set1 :
  for y in set2 :
    if x == y :
      intersection.add(x)
      
print(intersection)

for i in set1 :
  if i not in set2 :
    set2.add(i)

print(set2)  # union
