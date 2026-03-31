class Elevator:
    def __init__(self, bottom, top):
        self.bottom = bottom
        self.top = top
        self.current = bottom

    def floor_up(self):
        if self.current < self.top:
            self.current += 1
            print("Going up... now at floor", self.current)

    def floor_down(self):
        if self.current > self.bottom:
            self.current -= 1
            print("Going down... now at floor", self.current)

    def go_to_floor(self, target):
        if target < self.bottom or target > self.top:
            print("Invalid floor")
            return

        print("Moving to floor", target)

        while self.current < target:
            self.floor_up()

        while self.current > target:
            self.floor_down()

        print("Arrived at floor", self.current)
#2
class Building:
    def __init__(self, bottom, top, num_elevators):
        self.bottom = bottom
        self.top = top
        self.elevators = []

        for i in range(num_elevators):
            self.elevators.append(Elevator(bottom, top))

    def run_elevator(self, elevator_number, destination):
        if elevator_number < 0 or elevator_number >= len(self.elevators):
            print("Invalid elevator number")
            return

        print("\nRunning elevator", elevator_number)
        self.elevators[elevator_number].go_to_floor(destination)

    #3
    def fire_alarm(self):
        print("\nFIRE ALARM!!! All elevators go to bottom floor!")

        for i in range(len(self.elevators)):
            print("\nElevator", i)
            self.elevators[i].go_to_floor(self.bottom)
bottom = int(input("Enter bottom floor: "))
top = int(input("Enter top floor: "))
num = int(input("Enter number of elevators: "))
building = Building(bottom, top, num)
elevator_num = int(input("Which elevator (0,1,2...): "))
target_floor = int(input("Enter destination floor: "))
building.run_elevator(elevator_num, target_floor)
building.fire_alarm()

#4
import random
class Car:
    def __init__(self, plate, max_speed):
        self.plate = plate
        self.max_speed = max_speed
        self.current_speed = 0
        self.distance = 0

    def accelerate(self, change):
        self.current_speed += change

        if self.current_speed < 0:
            self.current_speed = 0

        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed

    def drive(self, hours):
        self.distance += self.current_speed * hours
class Race:
    def __init__(self, name, km, cars):
        self.name = name
        self.km = km
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            change = random.randint(-10, 15)
            car.accelerate(change)
            car.drive(1)

    def print_status(self):
        print("\n--- Race Status ---")
        print("Plate\tSpeed\tDistance")

        for car in self.cars:
            print(car.plate, "\t", car.current_speed, "\t", car.distance)

    def race_finished(self):
        for car in self.cars:
            if car.distance >= self.km:
                return True
        return False
cars = []
for i in range(10):
    plate = "ABC-" + str(i+1)
    max_speed = random.randint(100, 200)
    cars.append(Car(plate, max_speed))
race = Race("Grand Demolition Derby", 8000, cars)
hours = 0
while not race.race_finished():
    hours += 1
    race.hour_passes()

    if hours % 10 == 0:
        print("\nAfter", hours, "hours:")
        race.print_status()
print("\nRace finished in", hours, "hours!")
race.print_status()