from vehicle import vehicle    # Imports the vehicle class from the vehicle.py file.

class bike(vehicle):    # Creates a bike class that inherits from the vehicle class.

    def calculate_rent(self, days):   # Defines a method to calculate the bike rental cost based on the number of days.
        total_rent = (self.get_rental_price()*days)+100   # Calculates the total rent by multiplying the daily rental price by the number of days and adding a fixed charge of ₹100.
        return    # Returns the final rental amount.


