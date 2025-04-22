a=input("enter a password:")
special_character= ("@" in a or "#" in a or "$" in a or "%" in a or "&" in a)
print("valid password:", special_character)
print(a.isspace())
