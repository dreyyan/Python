class Hotel:
    # Constructor
    def __init__(self, name, location, rooms, rate, rating):
        self.name = name
        self.location = location
        self.rooms = rooms
        self.rate = rate
        self.rating = rating

    # Return to Menu
    def return_to_menu(self):
        valid_choices = {'y': self.BankMenu, 'n': self.Exit}
        valid_choice = False
        while not valid_choice:
            choice = input("Return to menu?[y/n]: ")
            if choice not in valid_choices:
                print("ERROR | invalid_input")
            else:
                valid_choice = True
        valid_choices[choice]()

    # [1] | Build Hotel
    def BuildHotel(self):
        print("building hotel...")
        valid_hotel_name = False

        while valid_hotel_name == False:
            hotel_name = input("Hotel Name: ")
            if hotel_name.strip():
                valid_hotel_name = True
            else:
                print("ERROR | invalid_hotel_name_input")
        self.return_to_menu()

    # [2] | Add Hotel Rooms
    def AddHotelRoom(self):
        print("adding hotel room/s...")
        self.return_to_menu()

    # [3] | Display Hotel Info
    def DisplayHotelInfo(self):
        print("display hotel info...")
        self.return_to_menu()

    # [4] | Display Hotel Room Info
    def DisplayHotelRoomInfo(self):
        print("display hotel room info...")
        self.return_to_menu()

    # [5] | List Available Rooms
    def ListAvailableRooms(self):
        print("display available rooms...")
        self.return_to_menu()

    # [6] | Demolish Hotel
    def DemolishHotel(self):
        print("demolish hotel...")
        self.return_to_menu()

    # [7] | Demolish Hotel Room
    def DemolishHotelRoom(self):
        print("demolish hotel room...")
        self.return_to_menu()

    # [8] | Reserve Room
    def ReserveRoom(self):
        print("reserving room...")
        self.return_to_menu()

    # [9] | Check Out Room
    def CheckOutRoom(self):
        print("checking out room...")
        self.return_to_menu()

    # Display Hotel Menu
    def HotelMenu(self):
        print("===+==+==+== iHMS ==+==+==+===")
        print("| -Hotel-Management-System- |")
        print(" -_-_-_-_-_[HOTEL]_-_-_-_-_-")
        print("-------------------------------")
        print("[1] | Build Hotel")
        print("[2] | Add Hotel Room/s")
        print("[3] | Display Hotel Info")
        print("[4] | Display Hotel Room Info")
        print("[5] | List Available Rooms")
        print("[6] | Demolish Hotel")
        print("[7] | Demolish Hotel Room")
        print("[8] | Reserve Room")
        print("[9] | Check Out Room")
        print("[10] | Exit")
        print("-------------------------------")

        # Function Library
        input_choice = {
            1: self.BuildHotel,
            2: self.AddHotelRoom,
            3: self.DisplayHotelInfo,
            4: self.DisplayHotelRoomInfo,
            5: self.ListAvailableRooms,
            6: self.DemolishHotel,
            7: self.DemolishHotelRoom,
            8: self.ReserveRoom,
            9: self.CheckOutRoom
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
   
h1 = Hotel("Lafayette Park Square", "Megaworld, Iloilo City", 50, 4.99, 4.75)
