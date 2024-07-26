
def Outer():
    print('Inside Outer')

    def Inner():
        print('Inside Inner')
    print('Inner:',id(Inner))

    

Result = Outer()    




