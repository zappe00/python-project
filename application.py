from car import ElectricCar, GasCar
from customer import Customer
from dealership import Dealership


def test_data(dealership: Dealership):

    car1 = ElectricCar("Tesla", "Model 3", 2022, 37990, 25000, 75)
    car2 = GasCar("Toyota", "Corolla", 2020, 18990, 68000, "Petrol")
    car3 = GasCar("BMW", "320d", 2019, 24990, 92000, "Diesel")
    car4 = ElectricCar("Nissan", "Leaf", 2021, 21990, 41000, 40)

    customer1 = Customer("Jasper Uusitalo", "jasper@email.com", "0401234567")
    customer2 = Customer("julius virtanen", "anna@email.com", "0507654321")

    dealership.add_car(car1)
    dealership.add_car(car2)
    dealership.add_car(car3)
    dealership.add_car(car4)

    dealership.add_customer(customer1)
    dealership.add_customer(customer2)

    # Sell a car to demonstrate sales functionality
    dealership.sell_car(1, 1, "15.11.2025")

    # Add a service booking to demonstrate service functionality
    dealership.add_service_booking(1, 2, "Oil change", "20.11.2025")


def run_tests(dealership: Dealership):
    # Run assertions to test the functionality

    # Test cars
    assert len(dealership.get_cars()) == 4
    assert dealership.find_car_by_id(1).brand == "Tesla"
    assert dealership.find_car_by_id(1).is_available() == False  # Sold
    assert dealership.find_car_by_id(2).is_available() == True   # Available
    assert dealership.find_car_by_id(3).brand == "BMW"
    assert dealership.find_car_by_id(4).model == "Leaf"

    # Test customers
    assert len(dealership.get_customers()) == 2
    assert dealership.find_customer_by_id(1).name == "Jasper Uusitalo"
    assert dealership.find_customer_by_id(2).email == "anna@email.com"

    # Test sales
    assert len(dealership.get_sales()) == 1
    sale = dealership.get_sales()[0]
    assert sale.customer.name == "Jasper Uusitalo"
    assert sale.car.brand == "Tesla"
    assert sale.sale_date == "15.11.2025"

    # Test service bookings
    assert len(dealership.get_service_bookings()) == 1
    booking = dealership.get_service_bookings()[0]
    assert booking.customer.name == "Jasper Uusitalo"
    assert booking.car.brand == "Toyota"
    assert booking.service_type == "Oil change"
    assert booking.date == "20.11.2025"

    # Test customer owned cars
    customer1 = dealership.find_customer_by_id(1)
    assert len(customer1.get_owned_cars()) == 1
    assert customer1.get_owned_cars()[0].brand == "Tesla"

    print("All tests passed!")


def add_customer_menu(dealership: Dealership):
    # asks user for customer data and adds a new customer

    print("Add new customer")
    name = input("Name: ")
    email = input("Email: ")
    phone_number = input("Phone number: ")

    customer = Customer(name, email, phone_number)
    dealership.add_customer(customer)

    print("Customer added.")


def add_car_menu(dealership: Dealership):
    # asks user what type of car they want to add

    print("Add new car")
    print("1. Electric car")
    print("2. Gas car")

    choice = input("Choose car type: ")

    brand = input("Enter brand: ")
    model = input("Enter model: ")
    year = int(input("Enter year: "))
    price = float(input("Enter price: "))
    mileage = int(input("Enter mileage: "))

    if choice == "1":
        battery_capacity = int(input("Enter battery capacity: "))
        car = ElectricCar(brand, model, year, price, mileage, battery_capacity)
        dealership.add_car(car)
        print("Electric car added successfully.")

    elif choice == "2":
        fuel_type = input("Enter fuel type: ")
        car = GasCar(brand, model, year, price, mileage, fuel_type)
        dealership.add_car(car)
        print("Gas car added successfully.")

    else:
        print("Invalid input.")


def sell_car_menu(dealership: Dealership):
    # asks for customer id, car id and sale date

    print("Sell a car")
    dealership.show_all_customers()
    customer_id = int(input("Enter customer ID: "))

    dealership.show_available_cars()
    car_id = int(input("Enter car ID: "))

    sale_date = input("Enter sale date (15.11.2025): ")

    dealership.sell_car(customer_id, car_id, sale_date)


def add_service_booking_menu(dealership: Dealership):
    # asks for booking information and creates a service booking

    print("Add service booking")
    dealership.show_all_customers()
    customer_id = int(input("Enter customer ID: "))

    dealership.show_all_cars()
    car_id = int(input("Enter car ID: "))

    service_type = input("Enter service type: ")
    date = input("Enter service date (for example 20.11.2025): ")

    dealership.add_service_booking(customer_id, car_id, service_type, date)


def search_cars_by_brand_menu(dealership: Dealership):
    # asks user for a brand and searches matching cars

    print("Search cars by brand")
    brand = input("Enter brand name: ")
    dealership.search_cars_by_brand(brand)


def show_customer_cars_menu(dealership: Dealership):
    # shows cars owned by one customer

    print("Show customer's cars")
    dealership.show_all_customers()
    customer_id = int(input("Enter customer ID: "))

    customer = dealership.find_customer_by_id(customer_id)

    if customer is None:
        print("Customer not found.")
    else:
        customer.show_owned_cars()


def main():

    dealership = Dealership("yoyoyoy")

    test_data(dealership)
    run_tests(dealership)

    while True:
        print("1. Show all cars")
        print("2. Show available cars")
        print("3. Show sold cars")
        print("4. Show all customers")
        print("5. Add new customer")
        print("6. Add new car")
        print("7. Sell a car")
        print("8. Show all sales")
        print("9. Add service booking")
        print("10. Show service bookings")
        print("11. Search cars by brand")
        print("12. Show one customer's cars")
        print("0. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            dealership.show_all_cars()

        elif choice == "2":
            dealership.show_available_cars()

        elif choice == "3":
            dealership.show_sold_cars()

        elif choice == "4":
            dealership.show_all_customers()

        elif choice == "5":
            add_customer_menu(dealership)

        elif choice == "6":
            add_car_menu(dealership)

        elif choice == "7":
            sell_car_menu(dealership)

        elif choice == "8":
            dealership.show_sales()

        elif choice == "9":
            add_service_booking_menu(dealership)

        elif choice == "10":
            dealership.show_service_bookings()

        elif choice == "11":
            search_cars_by_brand_menu(dealership)

        elif choice == "12":
            show_customer_cars_menu(dealership)

        elif choice == "0":
            break

        else:
            print("Invalid choice")


main()