menu = {
    'Pizza': 120,
    'Burger': 80,
    'Salad': 40,
    'Coffee': 25,
    'Sihab': 0.2,
}

print("Welcome to our Resturant, Here is our menu")
print('')
print("Pizza: 120\nBurger: 80\nSalad: 40\nCoffe: 25")

Order1 = input("What do you want to order? : ")

print("Your bill is: ", menu[Order1])
Order2 = input("Do you want to order more? : ")
if(Order1 != "Coffe" and Order2 == "No"):
    print("Your total bill is ", menu[Order1] )
    
elif(Order1 == "Coffe" and Order2 == "No"):
    print("Sorry sir, You Cant order just a coffe")
    print("Thank You")

else:
    total_bill = menu[Order1]+menu[Order2]
    Coupon = (input("Do you have a coupon Code, if yes then enter it? :"))
    if(Coupon == "Sihab"):
        disc_value = total_bill * menu[Coupon]
        print("Your bill after 20% Discount: ", total_bill - disc_value)
    else:
        print("Your total bill is: ", menu[Order1]+menu[Order2])
    
print("Thank you for ordering")