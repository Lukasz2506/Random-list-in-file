print("Creating the list with natural numbers  from 1 to 100, which are shuffled.\
       The list is write to the directory which is arleady useed.")

print()

print("Solution no1 by for loop and choice command")

print()

from os import path, getcwd
from random import choice

numbers = []

for number in range (1,101):
    numbers.append(number)

print("Numbers list: \n ", numbers)

mixedNumbers = []

for number in range (1,101):
    
    drawNumber = choice(numbers)
    mixedNumbers.append(drawNumber)
    numbers.remove(drawNumber)

filename1 = path.join(getcwd(),'RandomNumbers1.txt') #creating the path were the data will be saved.

file1 = open(filename1, 'w')

for number in mixedNumbers:
    file1.write(str(number) + "\n") #each number is save in the next text line

file1.close()

print("\n")
print("-----------------------------------------------------------------")
print("\n")

print("Solution no 2 by list comprehension")

print()

from random import shuffle
from os import path, getcwd

numbers2 = [number for number in range(1, 101)]
shuffle(numbers2)
print("shuffle numbers list: ", numbers2) # display mixed numbers


filename2 = path.join(getcwd(),'RandomNumbers2.txt')

with open(filename2, "w") as file2:
    for number in numbers2:
        file2.write(str(number) + ", ") #each number is separated by comma

