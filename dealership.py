# dealership.py
# This file contains the Dealership class
# The class manages cars, customers, sales and service bookings

from car import Car
from customer import Customer
from sale import Sale
from service import Service


class Dealership:
    def __init__(self, name: str):
        # basic dealership information
        self.name = name

        # lists for storing objects
        # Association
        self._cars = []
        self._customers = []
        self._sales = []
        self._service_bookings = []

    def add_car(self, car: Car):
        # adds a car object to the dealership
        self._cars.append(car)

    def add_customer(self, customer: Customer):
        # adds a customer to the dealership
        self._customers.append(customer)

    def get_cars(self):
        # returns all cars
        return self._cars

    def get_customers(self):
        # returns all customers
        return self._customers

    def get_sales(self):
        # returns all sales
        return self._sales

    def get_service_bookings(self):
        # returns all service bookings
        return self._service_bookings

    def show_all_cars(self):
        # shows all cars in the dealership
        if len(self._cars) == 0:
            print("No cars in the dealership.")
        else:
            print("All cars:")
            for car in self._cars:
                print(car.get_info())

    def show_available_cars(self):
        # shows only available cars
        found = False

        print("Available cars:")
        for car in self._cars:
            if car.is_available():
                print(car.get_info())
                found = True

        if not found:
            print("No available cars.")

    def show_sold_cars(self):
        # shows only sold cars
        found = False

        print("Sold cars:")
        for car in self._cars:
            if not car.is_available():
                print(car.get_info())
                found = True

        if not found:
            print("No sold cars.")

    def show_all_customers(self):
        # shows all customers
        if len(self._customers) == 0:
            print("No customers in the system.")
        else:
            print("\nCustomers:")
            for customer in self._customers:
                print(customer.get_info())

    def find_car_by_id(self, car_id: int):
        # searches for a car by id
        for car in self._cars:
            if car.car_id == car_id:
                return car
        return None

    def find_customer_by_id(self, customer_id: int):
        # searches for a customer by id
        for customer in self._customers:
            if customer.customer_id == customer_id:
                return customer
        return None

    def sell_car(self, customer_id: int, car_id: int, sale_date: str):
        # sells a car to a customer and creates a sale object
        customer = self.find_customer_by_id(customer_id)
        car = self.find_car_by_id(car_id)

        if customer is None:
            print("Customer not found.")
            return

        if car is None:
            print("Car not found.")
            return

        if not car.is_available():
            print("Car is already sold.")
            return

        customer.buy_car(car)
        sale = Sale(customer, car, sale_date)
        self._sales.append(sale)

        print("Car sold successfully.")

    def show_sales(self):
        # shows all sales
        if len(self._sales) == 0:
            print("No sales found.")
        else:
            print("Sales:")
            for sale in self._sales:
                print(sale.get_info())

    def add_service_booking(self, customer_id: int, car_id: int, service_type: str, date: str):
        # creates a service booking for a customer and a car
        customer = self.find_customer_by_id(customer_id)
        car = self.find_car_by_id(car_id)

        if customer is None:
            print("Customer not found.")
            return

        if car is None:
            print("Car not found.")
            return

        booking = Service(customer, car, service_type, date)
        self._service_bookings.append(booking)

        print("Service booking added successfully.")

    def show_service_bookings(self):
        # shows all service bookings
        if len(self._service_bookings) == 0:
            print("No service bookings found.")
        else:
            print("Service bookings:")
            for booking in self._service_bookings:
                print(booking.get_info())

    def search_cars_by_brand(self, brand: str):
        #search cars by brand name
        found = False

        print(f"Cars with brand {brand}:")
        for car in self._cars:
            if car.brand.lower() == brand.lower():
                print(car.get_info())
                found = True

        if not found:
            print("No cars found with that brand.")