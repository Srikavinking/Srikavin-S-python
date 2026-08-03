#Food Delivery

'''class restaurant:
    def __int__(self,menu):
        self.__menu=menu
    def show_mnu(self):
        print("menu:", self._menu)

    def prepare_food(self):
        pass

class pizzarestaurant(restaurant):
    def prepare_food(self):
        print("preparing pizza...")

class burgerrestaurant(restaurant):
    def prepare_food(self):
        print("preparing burger...")

class southIndianrestaurant(restaurant):
    def prepare_food(self):
        print("preparing Dosa and Idli...")

p=pizzarestaurant(["Margherita","veg pizza"])
b=burgerrestaurant(["chess burger", "veg burger"])
s=southIndianrestaurant(["Dosa","Idli"])

p.show_menu()
p.prepare_food()

b.show_menu()
b.prepare_food()

s=show_menu()
b.prepare_food()'''


#E-commerce product Management

class Product:
    def __init__(self, name, price):
        self.name = name
        self.__price = price

    def get_price(self):
        return self.__price

    def calculate_discount(self):
        pass


class Electronics(Product):
    def calculate_discount(self):
        return self.get_price() * 0.10


class Clothing(Product):
    def calculate_discount(self):
        return self.get_price() * 0.20


class Books(Product):
    def calculate_discount(self):
        return self.get_price() * 0.05


e = Electronics("Laptop", 50000)
c = Clothing("Shirt", 1000)
b = Books("Python Book", 800)

print("Electronics Discount:", e.calculate_discount())
print("Clothing Discount:", c.calculate_discount())
print("Books Discount:", b.calculate_discount())

#Ride Booking Application (Uber/ola)

from abc import ABC, abstractmethod

class Ride(ABC):
    def __init__(self, fare, distance):
        self.__fare = fare
        self.__distance = distance

    def get_distance(self):
        return self.__distance

    @abstractmethod
    def calculate_fare(self):
        pass


class BikeRide(Ride):
    def calculate_fare(self):
        return self.get_distance() * 10


class AutoRide(Ride):
    def calculate_fare(self):
        return self.get_distance() * 15


class CabRide(Ride):
    def calculate_fare(self):
        return self.get_distance() * 25


rides = [
    BikeRide(0, 10),
    AutoRide(0, 10),
    CabRide(0, 10)
]

for ride in rides:
    print(type(ride).__name__, "Fare = ₹", ride.calculate_fare())


#Smart Home Automation

from abc import ABC, abstractmethod

class SmartDevice(ABC):
    def __init__(self):
        self.__status = "OFF"

    def turn_on(self):
        self.__status = "ON"

    def show_status(self):
        print("Status:", self.__status)

    @abstractmethod
    def operate(self):
        pass


class Fan(SmartDevice):
    def operate(self):
        print("Fan is rotating")


class Light(SmartDevice):
    def operate(self):
        print("Light is glowing")


class AirConditioner(SmartDevice):
    def operate(self):
        print("AC is cooling")


f = Fan()
f.turn_on()
f.show_status()
f.operate()

l = Light()
l.turn_on()
l.show_status()
l.operate()

ac = AirConditioner()
ac.turn_on()
ac.show_status()
ac.operate()

#payment Gateway system

from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    def __init__(self, account):
        self.__account = account

    @abstractmethod
    def process_payment(self, amount):
        pass


class UPI(PaymentMethod):
    def process_payment(self, amount):
        print(f"UPI Payment of ₹{amount} Successful")


class CreditCard(PaymentMethod):
    def process_payment(self, amount):
        print(f"Credit Card Payment of ₹{amount} Successful")


class NetBanking(PaymentMethod):
    def process_payment(self, amount):
        print(f"Net Banking Payment of ₹{amount} Successful")


u = UPI("upi@okaxis")
c = CreditCard("1234-5678")
n = NetBanking("SBI123")

u.process_payment(500)
c.process_payment(1200)
n.process_payment(2500)


        
            


















