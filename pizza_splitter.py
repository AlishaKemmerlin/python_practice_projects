# Pizza Splitter
# This script adds up three different restaurant orders and splits the total bill evenly.
# It prints the menu, shows each person's order with item names,
# calculates each person's total, and shows the split cost for everyone.

# Set up the menu and prices
menu = {
    "wings" : 6.99,
    "pizza" : 12.99,
    "drink" : 2.49,
    "salad" : 5.99
}

# List of items ordered by each person (names, not prices)
alishas_order = ["wings", "pizza", "drink", "salad"]
rickys_order = ["pizza", "salad", "drink"]
xaviers_order = ["wings", "wings", "drink"]

# Print menu in a clean way
print("MENU")
for item, cost in menu.items():
    print(f"{item}: ${cost}")

# Print each person's order (ussed .join() to remove make list 
# print with commas to make it easier to read)
print(
    "\nAlisha's order:", ", ".join(alishas_order),
    "\nRicky's order:", ", ".join(rickys_order),
    "\nXavier's order:", ", ".join(xaviers_order)
)

# Calculate and print each person's total cost
alishas_total = sum(menu[item] for item in alishas_order)
print(f"\nAlisha's order cost: ${round(alishas_total, 2)}")

rickys_total = sum(menu[item] for item in rickys_order)
print(f"Ricky's order cost: ${round(rickys_total, 2)}")

xaviers_total = sum(menu[item] for item in xaviers_order)
print(f"Xavier's order cost: ${round(xaviers_total, 2)}")

# Calculate and print the amount each person should pay when splitting the total
split_total = round((alishas_total + xaviers_total + rickys_total) / 3, 2)
print(f"\nEveryone pays ${split_total}")