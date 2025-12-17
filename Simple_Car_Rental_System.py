 Simple Car Rental System 

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
    Rental.rental_cost = 0