# Restaurant Menu
menu = {
    'Pizza': 120,
    'Burger': 80,
    'Salad': 40,
    'Coffee': 25
}

discount_code = "Sihab"  # Predefined coupon code
discount_rate = 0.2  # 20% discount

print("Welcome to our Restaurant! Here is our menu:\n")

# Displaying the menu dynamically
for item, price in menu.items():
    print(f"{item}: {price} INR")

# Function to validate menu items
def get_valid_order(prompt):
    while True:
        order = input(prompt).strip().capitalize()
        if order in menu:
            return order
        else:
            print("Invalid item. Please choose from the menu.")

# First order
order1 = get_valid_order("\nWhat would you like to order? ")

# Check if only Coffee is ordered
order2 = input("Do you want to order more? (Yes/No): ").strip().lower()

if order1 == "Coffee" and order2 == "no":
    print("\nSorry, you cannot order just Coffee. Please order another item.")
else:
    total_bill = menu[order1]

    if order2 == "yes":
        order2 = get_valid_order("\nWhat else would you like to order? ")
        total_bill += menu[order2]

    # Apply coupon discount
    coupon = input("\nDo you have a coupon code? If yes, enter it: ").strip()
    
    if coupon == discount_code:
        discount_value = total_bill * discount_rate
        total_bill -= discount_value
        print(f"\nYour bill after a 20% discount: {total_bill:.2f} INR")
    else:
        print(f"\nYour total bill is: {total_bill} INR")

print("\nThank you for ordering! Have a great day!")