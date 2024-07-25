
#task 2

def list():
    size = int(input("Enter the number of elements in the list: "))
    lol_list = []
    for i in range(size):
        element = int(input(f"Enter element {i+1}: "))
        lol_list.append(element)
    return lol_list

def add_list(lst):
    total = 0
    for num in lst:
        total += num
    return total

def max_list(lst):
    max_value = lst[0]
    for num in lst:
        if num > max_value:
            max_value = num
    return max_value

def main():
    lol_list = list()
    print("List entered:", lol_list)
    print("Addition of the list:", add_list(lol_list))
    print("Maximum of the list:", max_list(lol_list))

if __name__ == "__main__":
    main()
