# object orientation

import os

def clear_console():
    os.system('clear')
    print('< .... some OO stuff .... >')
    print()
    return

#class definition
class Car:
    def __init__(self, make, year, model, price, milage):
        self.make = make
        self.model = model
        self.year = year
        self.price = price
        self.milage = milage

    def display_info(self):
        print(f"{self.year} {self.make} {self.model} {self.milage}")

    def update_model(self, new_milage):
        self.milage = new_milage
#end class

def process_the_data(theData):
    #create the car object
    car_data = theData.split(',')
    myCar = Car(car_data[0], car_data[1], car_data[2], car_data[3], car_data[4])
    return myCar

def get_the_data():
    #read the test puzzle input 
    #theData = 'tesla, 2023, model y, 517000, 22500'
    theData = open('cars_input.txt', 'r')
    #move data into a list - read a line and remove lineshift
    data_list = []
    for car in theData:
        car = car.strip()
        data_list.append(car)

    return data_list

def start_the_engine():
    #get the data and read them into a list
    theData = get_the_data()
    
    cars = []
    #process the data
    for car in theData:
        myCar = process_the_data(car) 
        myCar.display_info()
        #keep the cars (ojects) in a list
        cars.append(myCar)
   
    print()
    #update the second car
    print('number of cars: ', len(cars), '\n')
    
    this_car = cars[1]
    this_car.update_model('99999')
    print('we have updated the milage on one of the cars')
    this_car.display_info()
    print()

    return 

#let's start
if __name__ == '__main__':
    clear_console()
    start_the_engine()