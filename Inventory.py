# System inventory

stock_laptops = 5
stock_earphones = 10
stock_Monitors = 3

# Iterators
total_to_pay = 0
subtotal = 0
total_items_buy = 0

while True:
    try:
        products = int(input("Enter the amount of products to buy for: "))
        if products > 0:
            print("Good job")
            break
        else:
            print("Insert a amount of products please: ")
            
    except ValueError:
        print("Please enter a valid number greater than 0.")
        
# Creating the menu

for i in range(products):   
    while True: 
        try:
            print("\n = = STOCK AVAILABLE = = ")
            print(f"1) Laptops ($ 800)  | {stock_laptops} available")
            print(f"2) Earphones ($ 50) | {stock_earphones} available")
            print(f"3) Monitors ($200)  | {stock_Monitors} available")
            print("4) Show Stock Available")
            choice = int(input("Enter your choice: (1-4): "))
            if choice in [1, 2, 3, 4]:
                match choice:
                    case 1:
                        units = int(input("How many laptops do you want to buy? "))
                        if units <= 0:
                            print("Please, enter a valid amount.")
                        elif units > stock_laptops: 
                            print("Not available.") 
                        else:
                            print("Amount available")
                            stock_laptops -= units
                            subtotal = units * 800
                            total_to_pay += subtotal
                            total_items_buy += units
                            print(f"You have bought {units} laptops. Total you paid: ${total_to_pay}")
                            break
                    case 2:
                        units = int(input("How many earphones do you want to buy? "))
                        if units <= 0:
                            print("Please, enter a valid amount ")
                        elif units > stock_earphones:
                            print("Not available")
                        else:
                            print("Amount available")
                            stock_earphones -= units
                            subtotal = units * 50
                            total_to_pay += subtotal
                            total_items_buy += units
                            print(f"You have bought {units} earphones. Total you paid: ${total_to_pay}")
                            break
                    case 3:
                        units = int(input("How many monitors do you want to buy? "))
                        if units <= 0:
                            print("Please enter a valid amount")
                        elif units > stock_Monitors:
                            print("Not available")
                        else:
                            stock_Monitors -= units
                            subtotal = units * 200
                            total_to_pay += subtotal
                            total_items_buy += units
                            print(f"You have bought {units} monitors. Total you pid: $ {total_to_pay}")
                            break
                    case 4:
                        print(" = S T O C K = ")
                        print("Laptops: ", stock_laptops)
                        print("Earphones: ", stock_earphones)
                        print("Monitors: ", stock_Monitors)
                        
                    case _:
                        print("Invalid option")         
            else:
                print("Enter a valid choice (1-4)")   
        except ValueError:
            print("Only numbers") 

# Final part
print()                   
            
print("Thank for your purchase :) ")  
print("Summary")
print(f"Total items bought: {total_items_buy} | Total paid: ${total_to_pay} | Inventory: Laptops: {stock_laptops} | Earphones: {stock_earphones} | Monitors: {stock_Monitors}")               
                                        
                            
                
                        
                
                            
                

