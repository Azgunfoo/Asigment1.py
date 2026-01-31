length = float(input("enter zander length (cm): "))
if length >= 42: 
 print("KEEP!")
else:
 print("RELEASE!")

cabin = (input("enter cabin code:"))
if cabin == "LUX":
  print("upper deck with balcony")
elif cabin == "A":
  print("above the car deck, equipped with a window")
elif cabin == "B":
  print("windowless cabin above the car deck")
elif cabin =="C":
  print("windowless cabin below the car deck")
else:
  print("Invalid cabin class")

sex = input("enter sex(male or female:")
hgl = float(input("enter hemoglobin value:"))
if sex == "male":
  if hgl < 134:
    print("hemoglobin low")
  elif 134 <= hgl <= 167:
    print("hemoglobin normal")
  elif hgl >= 167:
    print("hemoglobin high")
if sex == "female":
  if hgl <134:
    print("hemoglobin low")
  elif 134 <= hgl <= 167:
    print("hemoglobin normal")
  elif hgl >= 167:
    print("hemoglobin high")

year = int(input("enter year:"))
if (year % 4 == 0) or (year % 100 == 0 or year % 400 == 0):
  print("is a leap year")
else:
  print("is not a leap year")

import math
def pizza_unit_price(diameter,price):
  radius = input(diameter / 2 /100)
  area = (pi * radius ** 2)
  unit_price = (price / area)
  return unit_price
d = float(input("enter diameter (cm):"))
p = float(input("enter price:"))
result = pizza_unit_price(d,p)
print("unit price:", result)




             
