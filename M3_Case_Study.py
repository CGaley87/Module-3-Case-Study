#Curtis Galey
#M3_Case_Study.py
#Program to output vehicle information entered in an orderly manner.
from datetime import datetime

class Vehicle:
    veh_options = 'car', 'truck', 'plane', 'boat', 'broomstick'

    def __init__(self,veh_type:str):
        self.veh_type = veh_type.strip().lower()


class Automobile(Vehicle):
    def __init__(self, veh_type: str):
        super().__init__(veh_type)
        
        #Year field must be a digit between 1886 and the current year + 1
        while True:
            year = input(f"Please enter the year of the {self.veh_type}: ")
            if year.isdigit():
                year = int(year)
                if 1886 <= year <= datetime.now().year + 1: #Using datetime keeps code current and + 1 for new model vehicles.
                    self.year = year
                    break
                else:
                    print(f"Invalid year. Please enter a year between 1885 and {datetime.now().year + 1}")
            else:
                print(f"Invalid year. Please enter a year between 1885 and {datetime.now().year + 1}")

        #Make field cannot be empty but too many potential options to limit in this context
        while True:
            make = input(f"Please enter the make of the {self.veh_type}: ").strip()
            if make:
                self.make = make
                break
            else:
                print("Make cannot be empty")

        #Model field cannot be empty but too many potential options to limit in this context
        while True:
            model = input(f"Please enter the model of the {self.veh_type}: ").strip()
            if model:
                self.model = model
                break
            else:
                print("Model cannot be empty")
        
        #Doors must be 2 or 4
        while True:
            doors = input(f"Please enter how many doors the {self.veh_type} has (2 or 4): ").strip()
            if doors in ("2", "4"):
                self.doors = doors
                break
            else:
                print("Door count must be 2 or 4.")
        
        #Roof must be solid or sunroof
        while True:
            roof = input(f"Please enter the type of roof of the {self.veh_type}(solid or sun roof): ").strip().lower()
            if roof in ("sun roof", "solid"):
                self.roof = roof
                break
            else:
                print("Please enter either 'solid' or 'sun roof' specifically.")

def prompt_vehicle_type():
    while True:
        choice = input("Please enter a Vehicle type: ").strip().lower()
        if choice in Vehicle.veh_options:
            return choice
        print(f"Vehicle not found in options. Please enter one of: {', '.join(Vehicle.veh_options)}.")

veh_choice = prompt_vehicle_type()

if veh_choice in ('car', 'truck'):
    choice1 = Automobile(veh_choice)
    print(f"Vehicle type: {choice1.veh_type}")
    print(f"Year: {choice1.year}")
    print(f"Make: {choice1.make}") #originally had .title() here but does not fit all brands or models.
    print(f"Model: {choice1.model}")
    print(f"Number of doors: {choice1.doors}")
    print(f"Type of roof: {choice1.roof}")

else:
    choice1 = Vehicle(veh_choice)
    print(f"You've entered {choice1.veh_type}. No specifics for this type of Vehicle.")