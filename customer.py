
from car import Car

#customer class
#customer can own multiple cars.

class Customer:
    #Class variable
    ID = 1

    def __init__(self, name: str, email: str, customer_id: int):
        #basic customer information
        self.name = name
        self.email = email


        self.customer_id = Customer.next_id
        Customer.next_id += 1

        #list of cars owned by the customer
        self.owned_cars: list = []

    def buy_car(self, car: Car):
        #customer buys a car if available
        if car.available:
            self.owned_cars.append(car)
            car.sell_car()
        else:
            print("Car is not available.")

    def show_cars(self):
        #show all cars owned by the customer
        if not self.owned_cars:
            print(f"{self.name} has no cars.")
        else:
            print(f"{self.name}'s cars:")
            for car in self.owned_cars:
                print(car.get_info())

    def get_info(self):
        #return basic customer info
        return f"{self.customer_id}: {self.name} ({self.email})"