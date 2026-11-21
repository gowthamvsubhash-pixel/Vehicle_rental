from vehicle import vehicle  # Imports the vehicle class from the vehicle.py file.


class car(vehicle):   # Creates a car class that inherits the properties and methods of the vehicle class.

    def calculate_rent(self, days): # Defines a method to calculate the total rental cost based on the number of days.
        total_rent = (self.get_rental_price()*days)+500 # Calculates the rent by multiplying the daily price by the number of days and adding a fixed charge of 500.
        return total_rent    # Returns the final rental amount.


