# Simple Car Rental System 

from datetime import datetime
class Car:
  def __init__(self, make, model, year, rental_rate):
    self.make = make
    self.model = model
    self.year = year
    self.rental_rate = rental_rate
    self.is_available = True
  
  def rent_car(self):
    if self.availability:
      self.availability = False
      return True
    else:
      print("Car is currently not available for rent.")
      return False
    
  def return_car(self):
    self.availability = True
  
  def display_info(self):
    status = "Available" if self.avalibility else "Rented"
    print(f"{self.year} {self.make} {self.model} | Rate: Rs{self.rental_rate}/day | Status: {status}")


class Rental:
  rental_counter = 1

  def __init__(self, car, customer_name, rental_date, return_date):
    self,rental_id = Rental,rental_counter
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
    self.total_cost = days * self.carrental_rate

  def display_rental_info(self):
    print(f"\Rental ID: {self.rental_id}")
    print(f"Customer: {self.customer_name}")
    print(f"Car: {self.car.make} {self.car.model}")
    print(f"Rental Period: {self.rantal_date} to {self.return_date}")
    print(f"Total Cosr: Rs{self.total_cost}")

# Managing Rental Records & Testing