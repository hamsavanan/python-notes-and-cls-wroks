mixed_type = {'Shubham',25,124,True,124}
more_add = {'Rahul',24}

#add() method -> add element to the set
mixed_type.add('Trainer')
print('Add method:',mixed_type)

#update() method
mixed_type.update(more_add)
print('Update method:',mixed_type)

#discard() method -> removes particular element
mixed_type.discard('Trainer')
print('Discard:',mixed_type)

mixed_type.remove('Trainer')
print('Remove method:',mixed_type)


