
#create menu_card using dictionary----

def add_function(menu_card,add_item,add_price):
    menu_card[add_item] = add_price
    return menu_card

def update_function(menu_card,update_item,update_price):
    if update_item in menu_card:
        menu_card[update_item] = update_price
    else:
        print(f"{update_item} not found in menu.")
    return menu_card

def delete_function(menu_card,remove_item):
    if remove_item in menu_card:
        del menu_card[remove_item]
    else:
        print(f"{remove_item} not found in menu.")
    return menu_card

def display_menu(menu_card):
    print("\nMenu Card:")
    for item, price in menu_card.items():
        print(f"{item}: {price}")

def main():
    menu_card = {'Paneer chukka': 120,'Pepper chicken': 100,'Non-veg Salad': 80,'American Fries': 90,'Double chicken Zinger Burger': 150
    }

    while True:
        print("\n\n1. Display menu card")
        print("2. Add item to menu card")
        print("3. Update item in menu card")
        print("4. Remove item from menu card")
        print("5. Exit")

        option = input("\nEnter your option (1-5):")

        if option == '1':
            display_menu(menu_card)
        elif option == '2':
            add_item = input("Enter the new item to add:")
            add_price = int(input(f"Enter the price for {add_item}: "))
            menu_card = add_function(menu_card, add_item, add_price)
        elif option == '3':
            update_item = input("Enter the item to update:")
            update_price = int(input(f"Enter the updated price for {update_item}: "))
            menu_card = update_function(menu_card, update_item, update_price)
        elif option == '4':
            remove_item = input("Enter the item to remove:")
            menu_card = delete_function(menu_card, remove_item)
        elif option == '5':
            print("\nExit.")
            break
        else:
            print("\nInvalid option.")

if __name__ == "__main__":
    main()