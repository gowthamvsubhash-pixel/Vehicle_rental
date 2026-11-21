from abc import ABC, abstractmethod   # Defines an abstract class named vehicle that inherits from ABC.

class vehicle(ABC):
    def __init__(self,name,price_per_day):   # Constructor that initializes the vehicle's name and daily rental price.
        self.name = name  # Stores the vehicle's name as a public attribute.
        self.__price_per_day = price_per_day  # Stores the rental price as a private attribute using double underscores.




    def get_rental_price(self):  # Defines a getter method to access the private rental price.
        return self.__price_per_day   # Returns the daily rental price.

    def display_vehicle_details(self):    # Defines a method to display the vehicle's details.
        print(f"Vehicle Name :{self.name}") # Prints the name of the vehicle.
        print(f"Rental price per day : {self.__price_per_day}")  # Prints the daily rental price.


    @abstractmethod # Ensures that child classes must implement this method.
    def calculate_rent(self,days): # Declares an abstract method to calculate rent based on the number of days.
        pass
