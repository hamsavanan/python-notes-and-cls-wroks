
#  Write a program which will check the number is greater and equal to 70 and less than and equal to 90

def Check_number(number):
    if number >= 70 and number <= 90:
        return number


def main():
    size = int(input('Enter the size : '))
    lst = []
    print('Enter value : ')
    for i in range(size):
        value = int(input())
        lst.append(value)
    print('User List ', lst)

    filter_list = list(filter(Check_number,lst))
    filter_list = list(filter(lambda x: x>=70 and x<=90 ,lst))
    print('Filter List : ',filter_list)
    
    
    add=lambda x,y: x+y
    print(add(2,3)) 
if __name__ == '__main__':
    main()




#------------------------------------------------------------------------------------



def calclulate_grade(mark):
    grade={90:"A",80:"B",70:"C",60:"D",40:"E"}

    print("Your grade is ",grade[mark])

def main(mark):

    if mark>=90:
        mark=90

    elif mark>=80:
        mark=80

    elif mark>=70:
        mark=70

    elif mark>=60:
        mark=60

    else: 
        mark=40  
    calclulate_grade(mark)

if __name__ == "__main__":
    main(int(input("Enter the mark:")))

