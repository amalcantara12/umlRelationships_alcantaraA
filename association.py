class Phone:
    def __init__(self, brand: str, model: str):
        self.brand = brand
        self.model = model
        self.battery = None  

class Battery:
    def __init__(self, battery_type: str):
        self.type = battery_type
        self.phone_using = None  

    def in_phone(self):
        if self.phone_using:
            print(f"Battery is being used in: {self.phone_using.brand} {self.phone_using.model}")

my_phone = Phone("Apple", "iPhone 15")
my_battery = Battery("Lithium-Ion")


my_phone.battery = my_battery
my_battery.phone_using = my_phone

my_battery.in_phone()  