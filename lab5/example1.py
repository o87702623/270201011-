#e-mail

mail = input("what is your e-mail?: ")

while True :
  if mail == "ceng113@example.com" or "CENG113@EXAMPLE.com" :
    print(True)
    break

    for i in mail[:"@":] :
      if i == "." :
        i = " "
  else:
    print("False")

   
    


