from car import Car


class Customer:
    # class variable
    ID = 1

    def __init__(self, name: str, email: str, phone_number: str):
        # basic customer information
        self.customer_id = Customer.ID
        Customer.ID += 1

        self.name = name
        self.email = email
        self.phone_number = phone_number

        # encapsulated list of customer cars
        self._owned_cars = []

    def buy_car(self, car: Car):
        # adds a car to the customer's list if the car is available
        if car.is_available():
            self._owned_cars.append(car)
            car.sell()
        else:
            print("This car is not available.")

    def show_owned_cars(self):
        # prints all cars owned by the customer
        if len(self._owned_cars) == 0:
            print(f"{self.name} does not own any cars.")
        else:
            print(f"Cars owned by {self.name}:")
            for car in self._owned_cars:
                print(car.get_info())

    def get_owned_cars(self):
        # returns the list of owned cars
        return self._owned_cars

    def get_info(self):
        # returns customer information as a string
        return f"Customer ID: {self.customer_id} | Name: {self.name} | Email: {self.email} | Phone: {self.phone_number}"