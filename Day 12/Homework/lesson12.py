for num in range(11):
    if num % 2 != 0:
     print(num)
for num in range(1, 51):
    if num % 5 == 0:
        print(num)

num = int(input("Enter an integer: "))

for i in range(num + 1):
    print(i)

for num in range(51):
    print(num)

total_sum = sum(range(51))

print("The sum of numbers from 0 to 50 is:", total_sum)
