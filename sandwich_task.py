#Write a function that accepts a list of items a person wants on a sandwich.The function should have one parameter that collects as many items as the function call provides, should print sandwich that's being ordered

def make_sandwich(sandwich_type,*ingredients):
    print(f"\nYou have ordered a {sandwich_type} with the following ingredients:")
    for ingredient in ingredients:
        print(f"- {ingredient}")

def main():
    sandwich_types = ["corn sandwich", "veg sandwich", "non-veg sandwich", "cheese sandwich"]

    print("Available sandwiches are:")
    for index, sandwich in enumerate(sandwich_types,1):
        print(f"{index}. {sandwich}")

    while True:
        try:
            choice = int(input("Enter the number of the sandwich you want to order: "))
            if 1 <= choice <= len(sandwich_types):
                selected_sandwich = sandwich_types[choice - 1]
                break
            else:
                print("Invalid choice.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    print("\n\nEnter the ingredients you want on your sandwich one by one.")
    print("Type 'exit' when you are finished.")
    
    ingredients = []
    while True:
        ingredient = input("Enter an ingredient (or 'exit' to finish): ")
        if ingredient.lower() == 'exit':
            break
        ingredients.append(ingredient)
    
    make_sandwich(selected_sandwich,*ingredients)

if __name__ == "__main__":
    main()
