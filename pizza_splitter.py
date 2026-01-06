# Pizza Splitter
# This script adds up three different restaurant orders and splits the total bill evenly.
# It prints the menu, shows each person's order with item names,
# calculates each person's total, and shows the split cost for everyone.

# Introduced a pure function to simplify and reuse the total calculation.
def calculate_order_total(menu, order_list):
    """Given the menu and a list of ordered items, return the total cost"""
    order_total = sum(menu[item] for item in order_list)
    return order_total

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
alishas_total = calculate_order_total(menu, alishas_order)
print(f"\nAlisha's order cost: ${alishas_total:.2f}")

rickys_total = calculate_order_total(menu, rickys_order)
print(f"Ricky's order cost: ${rickys_total:.2f}")

xaviers_total = calculate_order_total(menu, xaviers_order)
print(f"Xavier's order cost: ${xaviers_total:.2f}")

# Calculate and print the amount each person should pay when splitting the total
totals = [alishas_total, rickys_total, xaviers_total]
split_total = round(sum(totals) / len(totals), 2)
print(f"\nEveryone pays ${split_total:.2f}")
