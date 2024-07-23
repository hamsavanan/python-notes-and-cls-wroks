
watch_details = {
    'Titan':8000,
    'Fastrack':5000,
    'Omega':9000,
    'Cartier':8000
}
print('Length :',len(watch_details))
print('Type :',type(watch_details))
print('using key :',watch_details['Titan'])
print('using key :',watch_details['Cartier'])
print(watch_details)
watch_details['Omega'] = 4000
print('After modifying :',watch_details)
watch_details['IWC'] = 5000
print('After new watch :',watch_details)

#create a dictionary of fooditems and price (add,modify)


food = {
    'kesari':10,
    'cringy Vada':10,
    'samosa':25,
    'masala vada':15
}
 
food['samosa'] = 30
food['masala vada'] = 20
food['kesari'] = 35
 
print(food)


users = {
    'Leo':{
        'firstname': 'Dhanish',
        'lastname': 'Kumar',
        'Location': 'Grandline'
    },
    'pandu':{
        'firstname': 'Gokul',
        'lastname': 'Kannan',
        'Location': 'West Indies'
    },
    'karuppu':{
        'firstname': 'Karuppiah',
        'lastname': 'Saravanan',
        'Location': 'East Africa'
    }
}

for user, user_details in users.items():
    print(f"User: {user}")
    print(f"First Name: {user_details['firstname']}")
    print(f"Last Name: {user_details['lastname']}")
    print(f"Location: {user_details['Location']}")
   

    print('Length:',len(users))
