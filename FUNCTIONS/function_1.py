#def Addition():
#    print('Inside Addition') 
#Addition()


#def Addition(value_01,value_02):
#    print('Inside Addition')
#    print('Argument 1:',value_01) 
#    print('Argument 2:',value_02)
#    print(f'{value_01} and {value_02} adition is:',value_01+value_02)
#Addition(12,13)


def Addition(value_01,value_02):
    
    print('Inside Addition')
    print('Argument 1:',value_01) 
    print('Argument 2:',value_02)
    Add = value_01+value_02
    return Add
Result = Addition(12,13)
print('Result:',Result)




def Addition(value_01, value_02):
    print('Inside Addition')
    print('Argument 1:', value_01)
    print('Argument 2:', value_02)
    
    Add = value_01+value_02
    Sub = value_01-value_02
    
    print('Addition Result:',Add)
    print('Subtraction Result:',Sub)
    
    return Add,Sub

AdditionResult,SubtractionResult = Addition(12, 13)

print('Addition Result:', AdditionResult)
print('Subtraction Result:', SubtractionResult)
