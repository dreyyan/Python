from platform import system

class Vehicle:
    vehicle_manufacturers_list = ("ford", "volkswagen", "bmw", "mercedes-benz", "toyota", "general motors", "honda", "tesla", "nissan", "hyundai")
    # Constructor
    def __init__(self, manufacturer, model, licensePlate, numOfWheels):
        self.manufacturer = manufacturer
        self.model = model
        self.licensePlate = licensePlate
        self.numOfWheels = numOfWheels

    # Return to Menu
    def return_to_menu(self):
        valid_choices = {'y': self.VehicleMenu, 'n': self.Exit}
        valid_choice = False
        while not valid_choice:
            choice = input("Return to menu?[y/n]: ")
            if choice not in valid_choices:
                print("ERROR | invalid_input")
            else:
                valid_choice = True
        valid_choices[choice]()

    # [1] | Build Vehicle
    def BuildVehicle(self):
        print("building vehicle...")
        valid_vehicle_manufacturer = False

        while valid_vehicle_manufacturer == False:
            print("[ Ford | Volkswagen | BMW | Mercedes-Benz | Toyota ]")
            print("[ General Motors | Honda | Tesla | Nissan | Hyundai ]")
            vehicle_manufacturer = input("Manufacturer: ").lower()
            if vehicle_manufacturer.strip() and vehicle_manufacturer in Vehicle.vehicle_manufacturers_list:
                valid_vehicle_manufacturer = True
            else:
                print("ERROR | invalid_vehicle_manufacturer")

        valid_vehicle_model = False

        while valid_vehicle_model == False:
            vehicle_model = input("Model: ").lower()
            if vehicle_model.strip():
                valid_vehicle_model = True
            else:
                print("ERROR | invalid_vehicle_model")
        print("vehicle successfully built!")
        self.return_to_menu()

    # [2] | Display Vehicle Info
    def DisplayVehicleInfo(self):
        print("| Vehicle Info |")
        print(f'Brand: {self.manufacturer}')
        print(f'Model: {self.model}')
        self.return_to_menu()

    # [3] | Modify Vehicle
    def ModifyVehicle(self):
        print("modifying vehicle...")
        self.return_to_menu()

    # [4] | Customize Vehicle
    def CustomizeVehicle(self):
        print("customizing vehicle...")
        self.return_to_menu()

    # [5] | Destroy Vehicle
    def DestroyVehicle(self):
        print("destroying vehicle...")
        self.return_to_menu()

    # [6] | Test Run Vehicle
    def TestRunVehicle(self):
        print("test run vehicle...")
        print("starting engine...")
        self.return_to_menu()

    # [7] | Display Vehicle Condition
    def DisplayVehicleCondition(self):
        print("display vehicle condition...")
        self.return_to_menu()

    # [8] | Repair Vehicle
    def RepairVehicle(self):
        print("repairing vehicle...")
        self.return_to_menu()

    # [9] | Exit
    def Exit(self):
        print("exiting system...")
        exit()

    # Display Vehicle Menu
    def VehicleMenu(self):
        print("===+==+==+== iVMS ==+==+==+===")
        print("| -Vehicle-Management-System- |")
        print(" -_-_-_-_-_[VEHICLE]_-_-_-_-_-")
        print("-------------------------------")
        print("[1] | Build Vehicle")
        print("[2] | Display Vehicle Info")
        print("[3] | Modify Vehicle")
        print("[4] | Customize Vehicle")
        print("[5] | Destroy Vehicle")
        print("[6] | Test Run Vehicle")
        print("[7] | Display Vehicle Condition")
        print("[8] | Repair Vehicle")
        print("[9] | Exit")
        print("-------------------------------")

        # Function Library
        input_choice = {
            1: self.BuildVehicle,
            2: self.DisplayVehicleInfo,
            3: self.ModifyVehicle,
            4: self.CustomizeVehicle,
            5: self.DestroyVehicle,
            6: self.TestRunVehicle,
            7: self.RepairVehicle,
            8: self.Exit
        }

        # Exception Handling
        try:
            choice = int(input(">> "))
            if choice in input_choice:
                input_choice[choice]()
            else:
                print("ERROR | out_of_bounds_input")

        except ValueError:
            print("ERROR | invalid_input")

v1 = Vehicle("Honda", "Civic", "ABA-5146", 4)
v1.VehicleMenu()
