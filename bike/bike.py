from vehicle import vehicle

class bike(vehicle):

    def calculate_rent(self, days):
        total_rent = (self.get_rental_price()*days)+100
        return 


bike1 =bike("Royal enfield 350 :",800)
bike2 = bike("Duke 390 :",900)

print("----BIKE RENTAL DETAILS----")
print("************************************")
bike1.display_vehicle_details()
bike2.display_vehicle_details()
bike_rent = bike1.calculate_rent(3)
bike_rent2 = bike2.calculate_rent(3)
print(f"Final rental amount for 3 days :{bike_rent} For Royal Enfield 350")
print(f"Final rental amount for 3 days :{bike_rent2} For Duke 390")