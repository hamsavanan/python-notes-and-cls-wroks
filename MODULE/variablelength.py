#variable length argument:
#allows a function to accept a variable number of arguments
#Two types
#1.Non-Keyworded Arguments(*args)
#2.Args-Keyworded Arguments(**kwargs)


#def sum_all(*args):

#    count = 0
#    for i in args:
#        count += i
 #       return count
    

#output = sum_all((1,2,3,4,5))
#print('addition:',output)


def print_names(*args):
    for name in args:
        print(name)

def main():
    changepond = ['gokul','ajith','hamsa','karuppu','prasanth']
    print_names(*changepond)  

if __name__ == "__main__":
    main()
