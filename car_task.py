#Write a function that stores information about a car in a dictionary .The function should always receive a manufacturer and a model name. It should then accept an arbitary number of keyword arguments.



def car_info(manufacturer,model_name,**kwargs):
    car_dict = {
        'manufacturer': manufacturer,
        'model_name': model_name
    }
    
    for key, value in kwargs.items():
        car_dict[key] = value
    return car_dict

car = car_info('Toyota', 'Camry', color='blue', year=2022, sunroof=True)
print(car)



