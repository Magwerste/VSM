# Import
import pickle

# Base Vehicle Class
class Vehicle:
    def __init__(self, reg_num, make, model, colour, price, cost, branch):
        self.reg_num = reg_num.upper().strip()
        self.make = make.title().strip()
        self.model = model.title().strip()
        self.colour = colour.title().strip()
        self.price = price
        self.cost = cost
        self.branch = branch.strip().title()

    def get_details(self):
        return f"Registration: {self.reg_num}, Make: {self.make}, Model: {self.model}, Colour: {self.colour}, Price: £{self.price}, Branch: {self.branch}"

# Child Classes
class Car(Vehicle):
    def __init__(self, reg_num, make, model, colour, price, cost, branch, doors):
        super().__init__(reg_num, make, model, colour, price, cost, branch)
        self.doors = doors

    def get_details(self):
        return super().get_details() + f", Doors: {self.doors}".strip()

class Van(Vehicle):
    def __init__(self, reg_num, make, model, colour, price, cost, branch, capacity):
        super().__init__(reg_num, make, model, colour, price, cost, branch)
        self.capacity = capacity

    def get_details(self):
        return super().get_details() + f", Capacity: {self.capacity}kg".strip()

class Minibus(Vehicle):
    def __init__(self, reg_num, make, model, colour, price, cost, branch, seats):
        super().__init__(reg_num, make, model, colour, price, cost, branch)
        self.seats = seats

    def get_details(self):
        return super().get_details() + f", Seats: {self.seats}".strip()

# Data Storage using a dictionary
vehicles = {}

# Load data from pickle file
try:
    with open("vehicles.pickle", "rb") as f:
        vehicles = pickle.load(f)
except FileNotFoundError:
    # If file is not found, start with an empty dictionary
    pass
except pickle.UnpicklingError:
    # Handle corrupted pickle files
    print("Error: Corrupted data file. Starting with an empty dictionary.")

# Menu Functions
def add_vehicle():
    print("\nAdd New Vehicle\n")
    vehicle_type = input("Enter vehicle type (Car/Van/Minibus): ").lower()

    if vehicle_type not in ["car", "van", "minibus"]:
        print("Invalid vehicle type!")
        return

    try:
        reg_num = input("Enter registration number (e.g. AB12CDE): ").upper().strip()

        if reg_num in vehicles:
            print(f"Vehicle with registration {reg_num} already exists.")
            return

        # Additional criteria for each vehicle
        make = input("Enter make (e.g., Ford, Toyota): ").title().strip()
        model = input("Enter model (e.g., Fiesta, Corolla): ").title().strip()
        colour = input("Enter colour (e.g., Red, Blue): ").title().strip()
        price = float(input("Enter selling price (e.g., 10000.00): "))
        cost = float(input("Enter cost (e.g., 8000.00): "))

        branch = input("Enter branch (Mail/Add/Sand/Temple): ").upper().strip()
        
        
        while branch not in ["MAIL", "ADD", "SAND", "TEMPLE"]:
            branch = input("Invalid branch. Please enter Mail, Add, Sand, or Temple: ").upper().strip()

        # Creating new vehicle based on type
        if vehicle_type == "car":
            doors = int(input("Enter number of doors (e.g., 2, 4): "))
            vehicles[reg_num] = Car(reg_num, make, model, colour, price, cost, branch, doors)

        elif vehicle_type == "van":
            capacity = float(input("Enter capacity in kg (e.g., 1000.0): "))
            vehicles[reg_num] = Van(reg_num, make, model, colour, price, cost, branch, capacity)

        elif vehicle_type == "minibus":
            seats = int(input("Enter number of seats (e.g., 12, 16): "))
            vehicles[reg_num] = Minibus(reg_num, make, model, colour, price, cost, branch, seats)

    except ValueError as e:
        print(f"Error: {e}. Please enter valid input.")

# View Stored Vehicles
def view_vehicles():
    print("\nAll Vehicles\n")
    if not vehicles:
        print("No vehicles in stock.")
    else:
        for vehicle in vehicles.values():
            print(vehicle.get_details())

# Vehicle Search
def search_vehicles():
    print("\nSearch Vehicles\n")
    search_criteria = input("Enter search criteria (Registration/Type/Make/Model/Colour/Price Range/Branch): ").lower()
    if search_criteria == "registration":
        reg_num = input("Enter registration number (e.g. AB12CDE): ").upper().strip()
        if reg_num in vehicles:
            print(vehicles[reg_num].get_details())
        else:
            print(f"No vehicle found with registration {reg_num}.")
    # Type
    elif search_criteria == "type":
        vehicle_type = input("Enter vehicle type (Car/Van/Minibus): ").lower()
        found = False
        for vehicle in vehicles.values():
            if isinstance(vehicle, Car) and vehicle_type == "car" or \
                isinstance(vehicle, Van) and vehicle_type == "van" or \
                isinstance(vehicle, Minibus) and vehicle_type == "minibus":
                print(vehicle.get_details())
                found = True
        if not found:
            print(f"No {vehicle_type}s found.")
    # Make
    elif search_criteria == "make":
        make = input("Enter make: ").title()
        found = False
        for vehicle in vehicles.values():
            if vehicle.make.lower() == make.lower():
                print(vehicle.get_details())
                found = True
        if not found:
            print(f"No vehicles found with make {make}.")
    # Model
    elif search_criteria == "model":
        model = input("Enter model: ").title()
        found = False
        for vehicle in vehicles.values():
            if vehicle.model.lower() == model.lower():
                print(vehicle.get_details())
                found = True
        if not found:
            print(f"No vehicles found with model {model}.")
    # Colour
    elif search_criteria == "colour":
        colour = input("Enter colour: ").title()
        found = False
        for vehicle in vehicles.values():
            if vehicle.colour.lower() == colour.lower():
                print(vehicle.get_details())
                found = True
        if not found:
            print(f"No vehicles found with colour {colour}.")
    # Price Range
    elif search_criteria == "price range":
        try:
            min_price = float(input("Enter minimum price: "))
            max_price = float(input("Enter maximum price: "))
            found = False
            for vehicle in vehicles.values():
                if min_price <= vehicle.price <= max_price:
                    print(vehicle.get_details())
                    found = True
            if not found:
                print(f"No vehicles found within the price range £{min_price} - £{max_price}.")
        except ValueError:
            print("Error: Invalid price input. Please enter a valid number.")
    # Branch
    elif search_criteria == "branch":
        branch = input("Enter branch (Mail/Add/Sand/Temple): ").title()
        while branch not in ["Mail", "Add", "Sand", "Temple"]:
            branch = input("Invalid branch. Please enter Mail, Add, Sand or Temple: ").title()
        found = False
        for vehicle in vehicles.values():
            if vehicle.branch == branch:
                print(vehicle.get_details())
                found = True
        if not found:
            print(f"No vehicles found at the {branch} branch.")

    else:
        print("Invalid search criteria!")

# Offer
def make_offer():
    print("\nMake Offer\n")
    reg_num = input("Enter registration number (e.g. AB12CDE): ").upper().strip()
    if reg_num in vehicles:
        vehicle = vehicles[reg_num]
        try:
            offer = float(input(f"Enter your offer for {vehicle.make} {vehicle.model}: "))
            if offer >= vehicle.cost * 1.5:
                print(f"Offer of £{offer:.2f} accepted for {vehicle.make} {vehicle.model}!")
                del vehicles[reg_num]
            else:
                print(f"Offer of £{offer:.2f} is too low for {vehicle.make} {vehicle.model}.")
        except ValueError:
            print("Error: Invalid offer input. Please enter a valid number.")
    else:
        print(f"No vehicle found with registration {reg_num}.")

# Main Menu
while True:
    print("\nUWS Vehicle Sales\n")
    print("1. Add Vehicle")
    print("2. View Vehicles")
    print("3. Search Vehicles")
    print("4. Make Offer")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")
    # Options 1-5
    if choice == "1":
        add_vehicle()
    elif choice == "2":
        view_vehicles()
    elif choice == "3":
        search_vehicles()
    elif choice == "4":
        make_offer()
    elif choice == "5":
        try:
            with open("vehicles.pickle", "wb") as f:
                pickle.dump(vehicles, f)
        except pickle.PicklingError:
            print("Error: Unable to save data to file.")
        break
    else:
        print("Invalid choice. Please try again.")

print("Thank you for using UWS Vehicle Sales!")