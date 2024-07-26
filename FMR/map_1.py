from functools import reduce
def main():
    size = int(input('Enter the size : '))
    lst = []
    for i in range(size):
        value = int(input())
        lst.append(value)
    print('User List ', lst)

    map_list = list(map(lambda num:num**3,lst))
    print('Map List ',map_list,'\n')

    reduce_list = reduce((lambda num1,num2 : num1+num2),map_list)
    print('Reduce Value ', reduce_list)


if _name_ == '__main__':
    main()

#---------------------------------------------------------------------------
    #course = ['','python' ,'java',',,','angu;lar','php']
#task 1

def main():
    course = ['','python','java',',,','angu;lar','php']
    filtered_courses = filter(lambda x: x.isalpha(),course)
    filtered_courses_list = list(filtered_courses)
    print('Filtered Courses:',filtered_courses_list)

if __name__ == '__main__':
    main()

#---------------------------------------------------------------------------
#product_id = ['HEM-234','HEM-123','HEM-566']
#task 2

def main():
    product_id = ['HEM-234','HEM-123','HEM-566']
    output = [int(item.split('-')[1]) for item in product_id]
    print(output)
 
if __name__ == "__main__":
    main()

#----------------------------------------------------------------------------
#task 3
##sort a dictionary by value in python (lambda function)
#[
#{'name':'shreya','age':15},
#{'name':'pratiksha','age':13},
#{'name':'prerna','age':15}
#]

persons=[
{'name':'shreya','age':15},
{'name':'pratiksha','age':13},
{'name':'prerna','age':15}
 
]
sorted_list = sorted(persons, key=lambda val: val['age'] )
print(sorted_list)
    