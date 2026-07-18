print("Print all numbers between 30 and 80 that are divisible by 4")
print("")

for num in range(30, 81):
    if num % 4 == 0:
        print(num)
print("")
print("")

print("Print the first 8 odd numbers starting from 15")
print("")

count = 0
num = 15
while count < 8:
    if num % 2 != 0:
        print(num)
        count += 1
    num += 1
print(num)
print("")
print("")
