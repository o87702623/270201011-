def password_check():
  password = input("enter the password: ")
  if " " in password:
    print("level0")
  if len(password) < 8:
    print("level0")
    