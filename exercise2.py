name, alph = input("enter name and alphabet with comma separated ").split(",")
print("name size is ",len(name))
# print("entered char is ",name.count(alph))
print(f"entered char count is {name.lower().count(alph.lower())}")
