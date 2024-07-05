programming_academy = input("რომელ პროგრამირების აკადემიაში სწავლობთ? ")
if "GOA" in programming_academy:
 print("thats true")

else:
    print("You study at {programming_academy}.")


item_price = float(input("Enter the price of the item to be purchased: "))

budget = float(input("Enter your budget: "))

if budget >= item_price:
 print(f"You have {budget} Lari available.")

else:
    needed_amount = item_price - budget
    print(f"You need {needed_amount} Lari more to buy the item.")


number = float(input("Enter a number: "))

if number >= 5:
    product = number *  2
print(f"The product of {number} and 2 is {product}.")    


product = number * 4
print(f"The product of {number} and 4 is {product}.")


TICKET_PRICE = 10
DISCOUNT_PERCENTAGE = 0.3  # 30%

num_tickets = int(input("How many tickets do you want to buy? "))

if num_tickets < 5:
    total_price = num_tickets * TICKET_PRICE
    print("Total price for num_tickets tickets total_price GEL")

    print(f"Total price with 30% discount for num_tickets tickets total_price GEL")

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")


if operation == '+':
    result = add(num1, num2)
    print(f"{num1} + {num2} = {result}")
elif operation == '-':
    result = (num1, num2)
    print(f"{num1} - {num2} = {result}")
elif operation == '*':
    result = (num1, num2)
    print(f"{num1} * {num2} = {result}")
elif operation == '/':
    result = (num1, num2)
    print(f"{num1} / {num2} = {result}")



