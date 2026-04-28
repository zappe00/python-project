class Car:
    # class variable
    car_id = 1

    def __init__(self, brand: str, model: str, year: int, price: float, mileage: int):
        #car information
        self.car_id = Car.car_id
        Car.car_id += 1

        self.brand = brand
        self.model = model
        self.year = year
        self.price = price
        self.mileage = mileage

        # car is available when first added
        self._available = True

    def is_available(self):
        return self._available
    
    def sell(self):
        self._available = False

    def get_info(self):
        #basic information about the car
        if self._available:
            status = "Available"
        else: status = "Sold"
        return f"ID: {self.car_id} \n {self.brand} {self.model} \nYear: {self.year}\n Price: {self.price}€\n Mileage: {self.mileage} km\n Status: {status}"
# Inheritance: ElectricCar inherits from Car
class ElectricCar(Car):
    def __init__(self, brand: str, model: str, year: int, price: float, mileage: int, battery_capacity: int):
        # call the parent class constructor
        super().__init__(brand, model, year, price, mileage)

        # extra information only for electric cars
        self.battery_capacity = battery_capacity

    def get_info(self):
        # Polymorphism / overriding the get_info method
        status = "Available" if self._available else "Sold"
        return f"ID: {self.car_id} | {self.brand} {self.model} | Year: {self.year} | Price: {self.price}€ | Mileage: {self.mileage} km | Battery: {self.battery_capacity} kWh | Status: {status}"
class GasCar(Car):
    def __init__(self, brand: str, model: str, year: int, price: float, mileage: int, fuel_type: str):
        #parent class constructor
        super().__init__(brand, model, year, price, mileage)

        # extra information only for gas cars
        self.fuel_type = fuel_type

    def get_info(self):
        # overrides Car
        status = "Available" if self._available else "Sold"
        return f"ID: {self.car_id} | {self.brand} {self.model} | Year: {self.year} | Price: {self.price}€ | Mileage: {self.mileage} km | Fuel: {self.fuel_type} | Status: {status}"