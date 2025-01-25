#global item list
items = []
#function to add items to the cart
def addItemsToCart(item_name, item_price):
    items.append([item_name, item_price])
    return items
#function to view the items in the cart
def viewCartItems():
    print("Items in the cart are: ")
    for item in items:
        print(item[0], item[1])
#function to calculate the total price of the items in the cart
def CalculateTotalPrice(items):
    total_price = 0
    for item in items:
        total_price += item[1]
    return total_price
#main function
def main():
    while 1:
        print("Shopping Cart")
        print("1. Add Items to the cart")
        print("2. View Items in the cart")
        print("3. Calculate Total Price in the cart")
        print("4. Quit")
        choice = int(input("Enter your choice: "))
        print()
        if choice == 1:
            item_name = input("Enter the name of the item: ")
            item_price = float(input("Enter the price of the item: "))
            addItemsToCart(item_name, item_price)
            print()
            print(f"{item_name} has been added to your cart.")
            print()
        elif choice == 2:
            if(len(items) == 0):
                print("The cart is empty. First add some items to the cart.")
                print()
            else:
                viewCartItems()
        elif choice == 3:
            if(len(items) == 0):
                print("The cart is empty. First add some items to the cart.")
                print()
            else:
                print(f"Total price of the items in the cart is: {CalculateTotalPrice(items)}")
        elif choice == 4:
            break
        else:
            print("Invalid choice. Please try again.")
            print()
main()
        
    
