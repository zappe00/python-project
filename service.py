from customer import Customer
from car import Car


class Service:
    ID = 1

    def __init__(self, customer: Customer, car: Car, service_type: str, date: str):
        # basic booking information
        self.booking_id = Service.ID
        Service.ID += 1

        self.customer = customer
        self.car = car
        self.service_type = service_type
        self.date = date

    def get_info(self):
        # returns booking information as a string
        return (
            f"Booking ID: {self.booking_id} | "
            f"Customer: {self.customer.name} | "
            f"Car: {self.car.brand} {self.car.model} | "
            f"Service: {self.service_type} | "
            f"Date: {self.date}"
        )