from vehicle import vehicle


class car(vehicle):

    def calculate_rent(self, days):
        total_rent = (self.get_rental_price()*days)+500
        return total_rent


car1 = car("Toyota Innova ",2000)
car2 = car("Maruthi WagonR",1500)

print("-----CAR RENTAL DETAILS-----")
print("*************************************")
car1.display_vehicle_details()
car2.display_vehicle_details()
car_rent = car1.calculate_rent(3)
car_rent1 = car2.calculate_rent(3)
print(f"Final rental Amount for 3 days : {car_rent} For Innova")
print(f"Final Rental Amount for 3 days : {car_rent1} For WagonR ")