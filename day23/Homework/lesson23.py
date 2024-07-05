for i in range(21):
    print(i)

for i in range(1, 11):
    print(i)

print("Even numbers:")
for i in range(0, 101, 2):
    print(i)

print("\nOdd numbers:")
for i in range(1, 101, 2):
    print(i)

number = int(input("Enter a number: "))
sum = 0
for i in range(1, number + 1):
    sum += i
print(f"The sum of numbers from 1 to {number} is {sum}")

for i in range(5, 51, 5):
    print(i)

i = 0
while i <= 20:
    if i % 2 == 0:
        print(i)
    i += 1


i = 1
sum = 0
while i <= 10:
    sum += i
    i += 1
print(f"The sum of numbers from 1 to 10 is {sum}")



correct_number = 7
guess = None
while guess != correct_number:
    guess = int(input("Guess a number between 1 and 10: "))
    if guess == correct_number:
        print("Correct! You've guessed the number.")
    else:
        print("Try again.")

numbers = [1, 2, 3, 4, 5]
index = 0
while index < len(numbers):
    numbers[index] = numbers[index] * 2
    index += 1
print("Doubled numbers:", numbers)


correct_password = "password123"
entered_password = ""
while entered_password != correct_password:
    entered_password = input("Enter the password: ")
    if entered_password == correct_password:
        print("Access granted.")
    else:
        print("Incorrect password, try again.")
