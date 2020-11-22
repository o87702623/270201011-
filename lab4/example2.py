#percentage of evens

n = int(input("how many numbers?" ))

mylist = []
for i in range(n) :
  mylist.append(int(input("enter a number ")))


evens = []

for k in mylist :
  if k%2 ==0 :
    evens.append(k)

print(len(evens)/len(mylist)*100)