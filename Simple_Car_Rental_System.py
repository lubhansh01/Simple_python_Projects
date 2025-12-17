# Simple Car Rental System 

from datetime import date
class Car:
    def __init__(self, make, model, year, rental_rate):
        self.make = make
        self.model = model
        self.year = year
        self.rental_rate = rental_rate
        self.availability = True

    def rent_car(self):
        if self.availability:
            self.availability = False
            return True
        else:
            print("Car is not available")
            return False

    def return_car(self):
        self.availability = True

    def display_info(self):
        status = "Available" if self.availability else "Rented"
        print(f"{self.year} {self.make} {self.model} | Rate: Rs{self.rental_rate}/day | Status: {status}")



class Rental:
    rental_counter = 1   # class variable

    def __init__(self, car, customer_name, rental_date, return_date):
        self.rental_id = Rental.rental_counter
        Rental.rental_counter += 1

        self.car = car
        self.customer_name = customer_name
        self.rental_date = rental_date
        self.return_date = return_date
        self.total_cost = 0

    def calculate_total_cost(self):
        days = (self.return_date - self.rental_date).days
        if days == 0:
            days = 1
        self.total_cost = days * self.car.rental_rate

    def display_rental_info(self):
        print(f"Rental ID: {self.rental_id}")
        print(f"Customer: {self.customer_name}")


# Managing Rental Records & Testing

# List to store rental records
rentals = []

# Create cars
car1 = Car("Toyota", "Innova", 2022, 2500)
car2 = Car("Honda", "City", 2021, 2000)

# Display cars
car1.display_info()
car2.display_info()

# Rent a car
if car1.rent_car():
    rental1 = Rental(car1, "Rahul Sharma", date(2024, 6, 1), date(2024, 6, 4))
    rental1.calculate_total_cost()
    rentals.append(rental1)

# Try renting the same car again
car1.rent_car()

# Return car
car1.return_car()

# Display rental info
for rental in rentals:
    rental.display_rental_info()

# Display car status after return
car1.display_info()
