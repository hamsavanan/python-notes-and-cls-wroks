def print_names(*args):
    for name in args:
        print(name)

def main():
    changepond = ['gokul','ajith','hamsa','karuppu','prasanth']
    print_names(*changepond)  

if __name__ == "__main__":
    main()
