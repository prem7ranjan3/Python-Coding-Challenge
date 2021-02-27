# num = input("enter the number more than 1 digit")
# sum = 0
# i = 0
# while i<len(num):
#     sum += int(num[i])
#     i += 1
# print(sum)

number = input("enter the number :")
sum = 0

for i in range(0, len(number)):
    sum += int(number[i])

print(sum)