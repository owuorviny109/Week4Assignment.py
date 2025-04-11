#Assignment1 Designing a class
# Define a class to represent a Smartphone with various attributes
class Smartphone:
    # Constructor to initialize the smartphone attributes
    def __init__(self, brand, model, storage, ram, price, camera, battery):
        self.brand = brand  # Brand of the smartphone
        self.model = model  # Model name of the smartphone
        self.storage = storage  # Storage capacity in GB
        self.ram = ram  # RAM size in GB
        self.price = price  # Price in USD
        self.camera = camera  # Camera resolution in MP
        self.battery = battery  # Battery capacity in mAh

    # Method to display the details of the smartphone
    def myPhone(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Storage: {self.storage}GB")
        print(f"RAM: {self.ram}GB")
        print(f"Price: ${self.price}")
        print(f"Camera: {self.camera}MP")
        print(f"Battery: {self.battery}mAh")

# Subclass to represent a specialized type of smartphone for gaming
class GamingSmartphone(Smartphone):
    # Constructor to initialize gaming-specific attributes along with inherited attributes
    def __init__(self, brand, model, storage, ram, price, camera, battery, cooling_system, refresh_rate):
        super().__init__(brand, model, storage, ram, price, camera, battery)  # Initialize parent class attributes
        self.cooling_system = cooling_system  # Type of cooling system (e.g., liquid cooling)
        self.refresh_rate = refresh_rate  # Screen refresh rate in Hz

    # Override the myPhone method to include gaming-specific details
    def myPhone(self):
        super().myPhone()  # Call the parent class method to display common details
        print(f"Cooling System: {self.cooling_system}")
        print(f"Refresh Rate: {self.refresh_rate}Hz")

# Create instances of the Smartphone class with different attributes
myapplication1 = Smartphone("Apple", "iPhone 14", 128, 6, 799, 12, 3279)
myapplication2 = Smartphone("Samsung", "Galaxy S21", 256, 8, 799, 64, 4000)
myapplication3 = Smartphone("Google", "Pixel 6", 128, 8, 599, 50, 4614)
myapplication4 = Smartphone("OnePlus", "9 Pro", 256, 12, 969, 48, 4500)
myapplication5 = Smartphone("Xiaomi", "Mi 11", 256, 8, 749, 108, 4600)
myapplication6 = Smartphone("Sony", "Xperia 1 III", 256, 12, 1299, 12, 4500)
myapplication7 = Smartphone("Nokia", "G50", 128, 4, 299, 48, 5000)

# Call the myPhone method for each instance to display their details
myapplication1.myPhone()
print("-" * 30)  # Separator line
myapplication2.myPhone()
print("-" * 30)  # Separator line
myapplication3.myPhone()
print("-" * 30)  # Separator line
myapplication4.myPhone()
print("-" * 30)  # Separator line
myapplication5.myPhone()
print("-" * 30)  # Separator line
myapplication6.myPhone()
print("-" * 30)  # Separator line
myapplication7.myPhone()
print("-" * 30)  # Separator line

# Create an instance of the GamingSmartphone class
gaming_phone = GamingSmartphone("Asus", "ROG Phone 5", 256, 16, 999, 64, 6000, "Liquid Cooling", 144)

# Call the myPhone method for the gaming smartphone to display its details
gaming_phone.myPhone()
print("-" * 30)  # Separator line


print("challenge2 polimorphism challenge")
print("-" * 30)  # Separator line
# Parent class
class Transport:
    def move(self):
        pass  # Placeholder for polymorphism

# Derived classes with different implementations of move()
class Car(Transport):
    def move(self):
        print("Driving on the road.")

class Plane(Transport):
    def move(self):
        print("Flying in the sky.")

class Boat(Transport):
    def move(self):
        print("Sailing on the water.")

class Bicycle(Transport):
    def move(self):
        print("Pedaling on the street.")

class Train(Transport):
    def move(self):
        print("Running on the tracks.")

# List of different transports
vehicles = [Car(), Plane(), Boat(), Bicycle(), Train()]

# Loop through each transport and call the move() method
for vehicle in vehicles:
    vehicle.move()
