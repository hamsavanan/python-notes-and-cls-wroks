#create simple calculator, get input from user adn performing operations using dictionary


def add(num1,num2):
    return num1+num2

def subtract(num1,num2):
    return num1-num2

def multiply(num1,num2):
    return num1*num2

def divide(num1,num2):
    if num2 != 0:
        return num1/num2
    else:
        return "Divided by zero"

def main():
    while True:
        print("\n\nSimple Calculator Menu:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        option = input("\nEnter your option (1-5):")

        if option == '5':
            print("\nExit")
            break
        
        if option.isdigit():
            option = int(option)
            if option < 1 or option > 5:
                print("Invalid option.")
                continue

            num1 = float(input("\nEnter the first number:"))
            num2 = float(input("Enter the second number:"))

            noice_operations = {
                1: ("Addition", add(num1,num2)),
                2: ("Subtraction", subtract(num1,num2)),
                3: ("Multiplication", multiply(num1,num2)),
                4: ("Division", divide(num1,num2))
            }

            operation_name,result = noice_operations[option]
            print(f"\n{operation_name} result: {result}")

        else:
            print("Invalid input.")

if __name__ == "__main__":
    main()
