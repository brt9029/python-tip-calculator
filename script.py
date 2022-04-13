print("Welcome to the tip calculator.")
print("What as the total bill?")
total = float(input())
print("What percentage tip would you like to give?")
tip = int(input()) / 100
total = total * (1 + tip)
print("How many people to split the bill?")
split = int(input())
total = total / split
total = "{:.2f}".format(total)
print(f"Each person should pay: ${total}")