# lambda, map, reduce and filter
from functools import reduce


class Car:

    def __init__(self, make, model, price):
        self.make = make
        self.model = model
        self.price = price


cars = [
    Car("Ford", "Anglia", 300.0),
    Car("Ford", "Cortina", 700.0),
    Car("Alfa Romeo", "Stradale 33", 190.0),
    Car("Alfa Romeo", "Giulia", 500.0),
    Car("Citroën", "2CV", 75.0),
    Car("Citroën", "Dyane", 105.0),
    Car("Bmw", "Coupe", 1200.0),
    Car("Bmw", "i-series", 2500.0),
    Car("Ford", "puma", 1750),
    Car("Ford", "focus", 4200),
    Car("Jeep", "Compass", 2350),
    Car("Jeep", "Cheroke", 7200),
    Car("Jeep", "Whatewer", 200)
]

def dash_print():
    print("----------------------------------")

# 1 all cars that is less than 120 euros

car_les100 = list(filter(lambda x: x.price < 120, cars))
print("Cars with a price less than 120:")
for i in car_les100:
    print(i.make, i.model, i.price)
dash_print()

# 2. cars above 300 euros
car_more300 = list(filter(lambda x: x.price > 300, cars))
print("Cars with a price more than 300:")
for i in car_more300:
    print(i.make, i.model, i.price)
dash_print()

# 3. what is the cheapest price for "ford" car
car_ford = list(filter(lambda x: x.make == "Ford", cars))
cheap_ford = reduce(lambda x, y: x if x.price < y.price else y, car_ford)
print("Cheapest Ford car:")
print(cheap_ford.make, cheap_ford.model, cheap_ford.price)
dash_print()

# 4. the most expensive car in the list
expensive = reduce(lambda x, y: y if x.price < y.price else x, cars)
print("Most expensive car:")
print(expensive.make, expensive.model, expensive.price)
dash_print()

# 5. total cost of the "ford" cars in the list
car_ford = list(filter(lambda x: x.make == "Ford", cars))
print("Sum of all Ford cars:")
suma = sum(x.price for x in car_ford)
print(suma)
dash_print()

# 6. Total count of the "Jeep" car in the list
car_jeep = list(filter(lambda x: x.make == "Jeep", cars))
print("Total of all Jeep cars:")
number_of_jeep_cars = len(car_jeep)
print(number_of_jeep_cars)
dash_print()
