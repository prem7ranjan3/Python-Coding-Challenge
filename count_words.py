name = input("enter ur name")
#prem ranjan
#print(name.count('e'))
i=0
hold = ""
while i < len(name):
    if name[i] not in hold:
        hold += name[i]
        print(f"{name[i]}:{name.count(name[i])}")
    i += 1


