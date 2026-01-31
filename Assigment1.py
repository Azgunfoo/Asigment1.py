name = input("Hoang Tran")
print("Hello, Hoang Tran!")
radius = int (input("enter you radius of the circle: "))
pi = 3.14
circumference = (2 * pi * radius)
print("the circumference is:", circumference)
length = int(input("enter the length: "))
width = int(input ("enter the width: "))
perimeter = 2 * (length + width)
area = length * width
print("the perimeter is:", perimeter)
print("the area is:", area)
a = int(input("enter your first number: "))
b = int(input("enter your second number: "))
c = int(input("enter you third number: "))
total = a + b + c
product = a * b * c
average = total / 3
print("the total is:", total)
print("the product is:", product)
print("the average is:", average)
talent = int(input("enter talents: "))
pound = int(input("enter pound: "))
lots = int(input("enter lots: "))
gram= (talent * 20 * 32 * 13.3 + pound * 32 * 13.3 + lots * 13.3)
kilogram= int (gram // 1000)
remaining = gram % 1000
print("the gram is", gram)
print("the kilogram is", kilogram)
print("the remaining", remaining)
import random 
code1 = ""
for r in range (3):
    code1 = str(random.randint(0, 9))
code2 = ""
for r in range (4):
    code2 = str(random.randint(1, 6))
print("range (3)", code1)
print("range (4)", code2)

