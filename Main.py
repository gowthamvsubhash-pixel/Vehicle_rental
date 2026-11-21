from vehicle import vehicle # Imports the parent vehicle class from vehicle.py.
from car import car    # Imports the car class from car.py.
from bike import bike    # Imports the bike class from bike.py.


# Creates  objects with a daily rental price
car1 = car("Toyota Innova ",2000)
car2 = car("Maruthi WagonR",1500)


# Printing out the Output.
print("-----CAR RENTAL DETAILS-----")
print("*************************************")
car1.display_vehicle_details()  # Displays the name and daily rental price of the Innova.
car2.display_vehicle_details()   # Displays the name and daily rental price of the WagonR.
car_rent = car1.calculate_rent(3)
car_rent1 = car2.calculate_rent(3)
print(f"Final rental Amount for 3 days : {car_rent} For Innova")
print(f"Final Rental Amount for 3 days : {car_rent1} For WagonR ")

# Creates  objects with a daily rental price
bike1 =bike("Royal enfield 350 :",800)
bike2 = bike("Duke 390 :",900)

#print out the output.
print("----BIKE RENTAL DETAILS----")
print("************************************")
bike1.display_vehicle_details()
bike2.display_vehicle_details()
bike_rent = bike1.calculate_rent(3)
bike_rent2 = bike2.calculate_rent(3)
print(f"Final rental amount for 3 days :{bike_rent} For Royal Enfield 350")
print(f"Final rental amount for 3 days :{bike_rent2} For Duke 390")


# Output

# -----CAR RENTAL DETAILS-----
# *************************************
# Vehicle Name :Toyota Innova 
# Rental price per day : 2000
# Vehicle Name :Maruthi WagonR
# Rental price per day : 1500
# Final rental Amount for 3 days : 6500 For Innova
# Final Rental Amount for 3 days : 5000 For WagonR 




# ----BIKE RENTAL DETAILS----
# ************************************
# Vehicle Name :Royal enfield 350 :
# Rental price per day : 800
# Vehicle Name :Duke 390 :
# Rental price per day : 900
# Final rental amount for 3 days :None For Royal Enfield 350
# Final rental amount for 3 days :None For Duke 390