#task 5

def special_characters(s):
    special_character = set("!@#$%^&*()-_=+[]{}|;:'\",.<>?/~`")
    
    for char in s:
        if char in special_character:
            return True
        if char not in special_character:
            return False

string = input("Enter a string:")

if special_characters(string):
    print("String contains special characters.")
else:
    print("String doesn't contain special characters.")
