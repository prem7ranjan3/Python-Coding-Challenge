#python -c 'print("I owe you $2000".encode("hex"))'
#python -c 'print("I owe you $3000".encode("hex"))’

str1 = "49206f776520796f75202432303030"
str2 = "49206f776520796f75202433303030"

print(str1.__contains__(str2))



