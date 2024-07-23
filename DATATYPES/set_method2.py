company = {'Infosys','ICICI Bank','TCS','Bajaj'}

add_company = {'SBI','TATA Consultancy','Infosys','TCS'}

union_method = company.union(add_company)
print('Union method will return:',union_method)
print()

union_method = company | add_company
print('Union method will return:',union_method)
print()

intersection_method = company.intersection(add_company)
print('Intersection method will return commmon elements:',intersection_method)

intersection_method = company & add_company
print('Intersection method will return commmon elements:',intersection_method)

#difference method -> returns the different element presented in the two sets

difference_method = company.difference(add_company)
print('Difference method:',difference_method)

symm_difference = company.symmetric_difference(add_company)
print('Symmetric difference:',symm_difference)

#using for loop to iterate the set
for element in company:
    print(element)