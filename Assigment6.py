#Question 1
numbers=[]
print("enter numbers(enter empty number to end):")

while True:
    user_input=input()
    if user_input == "":
        break
    numbers.append(float(user_input))
numbers.sort(reverse=True)
print("5 largest numbers:", numbers[5])

#Question 2
Seasons= ("Winter","Winter","Winter","Spring","Spring","Spring","Summer","Summer","Summer","Autumn","Autumn","Autumn")
Month = int(input("Enter month(1-12):"))
Seasons=Seasons[Month-1]
print(f"{Month} is {Seasons}")

#Question 3
names = set()
print("Enter name(enter empty to end)")
while True:
    name=input()
    if name == "":
        break
    if name in names:
        print("Existing name")
    else:
        print("New name")
        names.add(name)
print("\nname list:")
for name in names:
    print(name)

#Question 4
def count_word_frequency(text):
    word_count={}
    words = text.lower().split()
    for word in words:
        word_count[word]=word_count.get(word,0) +1
    return word_count
text=input("enter text:")
frequency=count_word_frequency (text)
print("words:",frequency)

#Question 5
def remove_odds(numbers):
    return[x for x in numbers if x % 2 == 0]
#test
original = [1,2,3,4,5,6,7,8,9,10]
even= remove_odds(original)
print("Original list:", original)
print("Only odds:", even)

#Question 6
import random
N=int(input("random number:"))
n=0
for _ in range(N):
    x= random.uniform(-1,1)
    y=random.uniform(-1,1)
    if x*x+y*y < 1:
        n+=1
pi_approx= 4*n/N
print(f"π ≈ {pi_approx:.6f} (sai số: {abs(pi_approx - 3.141593):.6f})")

    