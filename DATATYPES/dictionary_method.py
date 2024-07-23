watch_details={
    'Titan':5000,
    'Rolex':45000,
    'Jungle':3300
}

#keys() -> returns a list containing the dictionary's keys
key_method =  watch_details.keys()
print('key method:',key_method)

key_method = watch_details.keys()
print('Key method:',key_method)

value_method = watch_details.values()
print('value method:', value_method)

get_method = watch_details.get('Titan')
print('get method:', get_method)

item_method = watch_details.items()
print('item method:',item_method)

watch_details.update({'Noise':2600})
print('Update method:',watch_details)

watch_details.pop('Titan')
print('Pop method:',watch_details)

