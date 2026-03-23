#1
number = []
print ("Enter your numbers, press enter to quit")
while True:
    user_input = input("Enter numbers:")
    if user_input == "":
        break
    try:
        num = float(user_input)
        number.append(num)
    except ValueError:
        print("Wrong number! please try again")
    
if len(number) >= 5:
    number.sort(reverse=True)
    print("5 biggest numbers,(from biggest to lowest):")
    for num in number[:5]:
        print(num)
else:
    print("Not enough numbers.", len(number),"numbers")

#2
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

number = int(input("Enter a prime number: "))

if is_prime(number):
    print(number, "Prime number")
else:
    print(number, "Not a prime number")


#3
cities = []

print("Enter 5 cities name:")

for i in range(5):
    city = input(f"City {i + 1}: ")
    cities.append(city)

print("\nYour city")
for city in cities:
    print(city)


#4
def sum_of_list(numbers):
    return sum(numbers)

# Main program for testing
test_list = [10, 20, 30, 40, 50]
result = sum_of_list(test_list)
print("Original list:", test_list)
print("All the numbers:", result)


#5
def remove_odds(numbers):
    return [num for num in numbers if num % 2 == 0]

# Main program for testing
test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered_list = remove_odds(test_list)

print("Original list: ", test_list)
print("Removed odd numbers: ", filtered_list)



