#task 3
#using function

def addition(a,b):
    return a+b

def subtraction(a,b):
    return a-b

def multiplication(a,b):
    return a*b

def division(a,b):
    if b == 0:
        return "Error."
    return a/b

def main():
    num1 = float(input("Enter the first number:"))
    num2 = float(input("Enter the second number:"))
    
    print("Choose an operation:")
    print("1: Addition")
    print("2: Subtraction")
    print("3: Multiplication")
    print("4: Division")
    
    choice = input("Enter the choice 1/2/3/4:")
    
    if choice == '1':
        print("Result:",addition(num1,num2))
    elif choice == '2':
        print("Result:",subtraction(num1,num2))
    elif choice == '3':
        print("Result:",multiplication(num1,num2))
    elif choice == '4':
        print("Result:",division(num1,num2))
    else:
        print("wrong choice")

if __name__ == "__main__":
    main()

