from customer import Customer
from car import Car


class Sale:
    ID = 1

    def __init__(self, customer: Customer, car: Car, sale_date: str):
        # basic sale information
        self.sale_id = Sale.ID
        Sale.ID += 1

        self.customer = customer
        self.car = car
        self.sale_date = sale_date
        self.sale_price = car.price

    def get_info(self):
        # returns sale information as a string
        return (
            f"Sale ID: {self.sale_id} | "
            f"Customer: {self.customer.name} | "
            f"Car: {self.car.brand} {self.car.model} | "
            f"Date: {self.sale_date} | "
            f"Price: {self.sale_price}€"
        )