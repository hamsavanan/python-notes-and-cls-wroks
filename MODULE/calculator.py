import arithmatic


print('choose the operators')
print('1.Addition\n2.Subtraction\n3.Multiplication')

select = int(input('Select 1/2/3'))
def main():
    num_01 = int(input('Enter 1st Number'))
    num_02 = int(input('Enter 2nd Number'))

    if (select==1):
        Ans = arithmatic.Addition(num_01,num_02)
        print(f"Addition {num_01} and {num_02}:",Ans)
    elif (select==1):
        Ans = arithmatic.Subtraction(num_01,num_02)
        print(f"Subtraction {num_01} and {num_02}:",Ans)
    elif (select==1):
        Ans = arithmatic.Multiplication(num_01,num_02)
        print(f"Multiplication {num_01} and {num_02}:",Ans)

    else:
        print('choose 1/2/3')

if __name__ == "__main__":
    main()

    
