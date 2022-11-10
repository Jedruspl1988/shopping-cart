def menu():
    print("[1] Start New Shopping Cart.")
    print("[2] Add an item to Shopping Cart.")
    print("[3] Delete an item from Shopping Cart.")
    print("[4] Show current Shopping Cart.")
    print("[0] Pay &/or Exit.")
shopping = []    
menu()
selection = int(input("\nPlease select from the menu:\n"))
while selection != 0:
    if selection == 1:
        print("Selected: Start New Shopping Cart:") 
        added_items = input("What would you like to add?\n")
        shopping.append(added_items)
    elif selection == 2:
        print("Selected: Add an item to Shopping Cart.")
        added_item = input("What would you like to add?\n")
        added_items = input("Add items to the cart now:\n")
        shopping.append(added_items)
    elif selection == 3:
        print("Selected: Delete an item from Shopping Cart.\n")
        print(shopping)
        removed_item = input("Which item from your shopping cart would you like to remove?\n")
        print(removed_item + " was removed from your cart.")
        shopping.remove(removed_item)
        print(shopping)
    elif selection == 4:
        print(shopping)   
    else:
        print("\nInvalid selection. Please select an option form the menu.")      
    print()
    menu()
    selection = int(input("\nPlease select from the menu\n"))
print("Thanks for your business, we hope to see you again soon!")    