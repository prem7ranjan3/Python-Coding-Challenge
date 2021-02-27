name = input("enter the name")
for i in range(len(name)):
    print()
    print(f"{name[i]}:{name.count(name[i])}")