class Car:
    """
    Basic car class.

    This class stores common information about a car.
    """

    def __init__(self, brand: str, model: str, price: float):
        
        #Car object

        #brand
        #model
        #price
    
        self.brand = brand
        self.model = model
        self.price = price
        self.available = True  #Car is available by default

    def get_info(self):
        
        #Return car information as a string
        
        return f"{self.brand} {self.model} - {self.price}€"

    def sell_car(self):
        """
        Mark the car as sold.
        """
        self.available = False


class ElectricCar(Car):
    
    #inherits from Car
    #adds battery capacity
    

    def __init__(self, brand: str, model: str, price: float, battery_capacity: int):
        """
        Create a new electric car.

        Args:
            battery_capacity (int): Battery size in kWh
        """
        super().__init__(brand, model, price)
        self.battery_capacity: int = battery_capacity

    def get_info(self) -> str:
        """
        Return electric car information.
        Overrides the base class method.
        """
        return f"{self.brand} {self.model} - {self.price}€ - Battery: {self.battery_capacity} kWh"


class GasCar(Car):
    """
    GasCar inherits from Car.

    This class adds fuel type.
    """

    def __init__(self, brand: str, model: str, price: float, fuel_type: str):
        """
        Create a new gas car.

        Args:
            fuel_type (str): For example petrol or diesel
        """
        super().__init__(brand, model, price)
        self.fuel_type: str = fuel_type

    def get_info(self):
        """
        Return gas car information.
        Overrides the base class method.
        """
        return f"{self.brand} {self.model} - {self.price}€ - Fuel: {self.fuel_type}"