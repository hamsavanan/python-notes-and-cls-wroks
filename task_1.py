non_veg_starter = ['chicken 65','chilly mutton','fried crispy chciken']

def display_menu():
    print(non_veg_starter)

def add_starter():
    non_veg_starter.append(input("Enter item:"))

def update_starter():
    name = input("Enter item to update: ")
    if name in non_veg_starter:
        pos = non_veg_starter.index(name)
        non_veg_starter[pos] = input("Enter new item:")
    else:
        print("Item not found in the menu.")

def remove_starter():
    item_to_remove = input("Enter item to remove:")
    if item_to_remove in non_veg_starter:
        non_veg_starter.remove(item_to_remove)
    else:
        print("Item not found in the menu.")

def menu(choice):
    if choice == 1:
        display_menu()
    elif choice == 2:
        add_starter()
    elif choice == 3:
        update_starter()
    elif choice == 4:
        remove_starter()
    else:
        exit(0)

def main():
    while True:
        print("\n1 for display menu")
        print("2 to add starter menu")
        print("3 to update starter menu")
        print("4 to remove starter menu")
        choice = int(input("Enter the choice:"))
        menu(choice)

if __name__ == "__main__":
    main()