#creating a list:
#creating same data type

course=['python','java','php'] #string
rollno= [123,124,124] #integer


#creating mixed type

mixed_type=['ketan',123,True,12.33]

print('Heterogenus:',mixed_type)
print('length:',len(mixed_type))

print('access value of keten :',mixed_type[0])
print('access value of 123 :',mixed_type[1])
print('access value of True :',mixed_type[2])
print('access value of 12.33 :',mixed_type[3])

#slicing :[start:stop(excluded)]

print('slicing:',mixed_type[1:3])

#[keten,123,true]

print('slicing:',mixed_type[0:3])

#negative slicing

print('slicing:',mixed_type[-4:-1])

#mutable (can change ,add and delete)

fruits=['mango','apple','grapes','kiwi','watermelon']
fruits[1]='kiwi'
print('using index replacing banana with kiwi:',fruits)











