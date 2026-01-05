# exercise 2 Shopping Cart Program

item = input("What item would you like to buy?: ")
price = float(input("what is the price?:"))
quantity = int(input("How many would you like?:"))
total = price * quantity

print(f"You have purchased {quantity} {item}(s) at a price of {price} each.")
print(f"Your total is: {total}")