#task 1 

i = int((input("enter your number: ")))
while i <= 1000:
        if i % 3 == 0 :
         print(i)
         i += 3

#task 2
 
while True : 
 inches = float((input("enter your number (negative number to quit):" )))
 if inches < 0:
   print("programe end")
   break
 centimeter = inches * 2,54
 print(inches,"inches =", centimeter,"centimeter")

#task 3

number = input("enter your number (press Enter to quit)")
if number == "":
   print("stop")
change = number.split()
biggest = number[0]
smallest = number[0]
for things in change:
   if biggest < things:
    biggest = things
print(biggest)
for thing in change:
   if smallest > thing :
    smallest = thing
print(smallest)
   
#task 4

import random
secret = random.randint(1,10)
while True:
   guess = int(input("Guess the random number:"))
   if guess < secret:
    print("Too Low")
   elif guess > secret:
     print("Too High")
   else:
     print("Correct")
     break 

#task 5

correct_username = "python"
correct_password = "rules" 
attemp = 0
while attemp < 5:
  username = input("Enter your username:")
  password = input("Enter your password:")
  if username == correct_username and password == correct_password:
    print("WELCOME")
    break
  else:
    print("Incorrect Informations")
    attemp += 1
  if attemp == 5:
    print("Access denined")

#task 6

def middle_character(text):
  length = len(text)
  mid = length // 2
  if length % 2:
    return text[mid-1:mid+1]
  else:
    return text[mid]
user_text = input("enter any word:")
print("middle_character:",middle_character(user_text))

#task 7 

def acronym(phrase):
  words = phrase.split()
  result = ""
  for word in words:
    result += word[0].upper()
  return result
text = input("enter any words:")
print("acromym:",acronym(text))
  