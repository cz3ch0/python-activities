coffee = True
milk = False

# and both conditions must be true
# or at least one condition must be true
# not negates the condition
if coffee and milk:
    print("You have both coffee and milk.")
elif coffee or milk:
    print("You have either coffee or milk.")
else:
    print("You have neither coffee nor milk.")
if not coffee:
    print("You do not have coffee.")
if not milk:
    print("You do not have milk.")

# Output:
# You have either coffee or milk.
