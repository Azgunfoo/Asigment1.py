#1
import random

class Car:
    def __init__(self, license_plate, max_speed):
        self.license_plate = license_plate   
        self.max_speed = max_speed           
        self.current_speed = 0               
        self.distance_travelled = 0          

    def accelerate(self, speed_change):
        self.current_speed += speed_change
        
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed

        if self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours):
        self.distance_travelled += self.current_speed * hours

#2
def accelerate(self, change):
        self.current_speed += change
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed

        if self.current_speed < 0:
            self.current_speed = 0
        
def drive(self, hours):
        distance = self.current_speed * hours
        self.distance_travelled += distance

#3
cars = []

for i in range(1, 11):
    license_plate = f"ABC-{i}"
    max_speed = random.randint(150, 200)
    cars.append(Car(license_plate, max_speed))

#4
race_on = True
hours = 0

while race_on:
    hours += 1

    for car in cars:
        change = random.randint(-10, 15)
        car.accelerate(change)

        car.drive(1)

        if car.distance_travelled >= 10000:
            race_on = False

print("\nRace result")
print(f"{'Plate':<10} {'Max Speed':<12} {'Speed':<10} {'Distance':<10}")

for car in cars:
    print(f"{car.license_plate:<10} {car.max_speed:<12} {car.current_speed:<10} {int(car.distance_travelled):<10}")