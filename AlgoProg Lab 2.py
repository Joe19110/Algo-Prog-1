grocery_items = []
choice = 0
while choice != 4:
    print("[1] Add Item")
    print("[2] View Items")
    print("[3] Remove Item")
    print("[4] Exit")
    choice = int(input("Choice: "))
    if choice == 1: 
        grocery_items.append(input("Enter item name: "))
        print("Successfully added")
    elif choice == 2:
        for item in grocery_items:
            print("-", item)
    elif choice == 3:
        user_input = input("Enter item name to be removed: ")
        if user_input in grocery_items:
            grocery_items.remove(user_input)
            print("Item removed successfully")
        else:
            print("Item not found")
print("Program exited")
