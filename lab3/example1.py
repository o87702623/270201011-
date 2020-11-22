#sum of digits

digit_list = list(input("enter an integer "))


for i in range(len(digit_list)) :
  digit_list[i] = int(digit_list[i])

if len(digit_list) > 1 :
  print(digit_list[-1] + digit_list[-2])

elif len(digit_list) == 1 :
  print(digit_list[0])
