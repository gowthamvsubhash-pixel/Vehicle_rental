from abc import ABC, abstractmethod

class vehicle(ABC):
    def __init__(self,name,price_per_day):
        self.name = name
        self.__price_per_day = price_per_day




    def get_rental_price(self):
        return self.__price_per_day

    def display_vehicle_details(self):
        print(f"Vehicle Name :{self.name}")
        print(f"Rental price per day : {self.__price_per_day}")


    @abstractmethod
    def calculate_rent(self,days):
        pass
