menu = {
    "Pizza": 189,
    "ChickenBurger": 150,
    "Pasta": 80,
    "GreenTea": 50,
    "Coffee": 40,
    "Icecream": 50
}

print("Welcome to my restaurant!")
print("\nHere is the menu:\n")
for item, price in menu.items():
    print(f"{item} : ₹{price}")

total_order = 0
order_list = []

while True:
    item = input("\nEnter the name of the item you want: ").strip().lower()

    # Find matching menu item regardless of case
    found_item = None
    for menu_item in menu.keys():
        if menu_item.lower() == item:
            found_item = menu_item
            break

    if found_item:
        total_order += menu[found_item]
        order_list.append(found_item)
        print(f" Your order '{found_item}' will be served shortly!")
    else:
        print(f" Sorry! '{item}' is not available in our restaurant. Please choose something else.")

    another = input("Do you want to order something else? (yes/no): ").strip().lower()
    if another != "yes":
        break

print("\n----- ORDER SUMMARY -----")
print("Items Ordered:", ", ".join(order_list))
print(f"Total Amount to Pay: ₹{total_order}")

# Add rating based on total amount
if total_order >= 300:
    grade = "Excellent Customer!"
elif total_order >= 200:
    grade = "Great Choice!"
elif total_order >= 100:
    grade = "Good Taste!"
else:
    grade = "Thanks for Visiting!"

print(f"\n{grade}")
print("Thank you for visiting our restaurant! Have a great day! 🍽️")
