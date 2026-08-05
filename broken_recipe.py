# fruits = ["apple", "pineapple", "orange", "mango", "cherry"]

# print(fruits[0])

# numbers = [2, 3, 5, 4, 1]

# numbers.sort()
# print(numbers)


# value1 = "15"
# value2 = "banana"
# print(value1.isdigit())
# print(value2.isdigit())


# selected_drink = "coffe"
# target_temp = 100

# if selected_drink == "Green Tea":
#     target_temp = 80
# elif selected_drink == "coffe":
#     target_temp = 90


# print(target_temp)


# for count in range(5):
#     print("Grind" + str(count))

# weight = 0.0

# while weight < 1.5:
#     weight = weight + 0.5
#     print("current weight:" + str(weight))



#List
# students_names = ["tola","tosin", "Henry"]

# #Tuple
# students_name= ("tola","tosin", "Henry")

# total_student = students_name[0:2]

# print(total_student)

#SET
# cities = {"Ikeja", "Ado-ekiti", "oshogbo"}

# cities.discard("oshogbo")

# print(cities)

# cities = {"Ikeja", "Ado-ekiti", "oshogbo"}

# cities.add("akure")
# print(cities)

# print(len(cities))

# age = int(input("How old are you ?"))

# if age < 13:
#     print("You are a child")
# elif age < 20:
#     print("You are an teenager")
# elif age < 40:
#     print("you are an adult")
# else: 
#     print("not allowed here ")



class Cup:
    pass
my_cup = Cup()
print(my_cup)






class Cup:
    def __init__(self, color):
        self.color = color

blue_cup = Cup("blue")
print(blue_cup.color)


class Cup:
    def __init__(self,):
        self.contents = "empty"

my_cup = Cup()
my_cup.contents = "Mocha"
print(my_cup.contents)

class pet:
    def __init__(self, name, species):
        self.name = name 
        self.species = species

dog = pet("Rex", "Dog")
cat = pet("Mittens", "Cat")
print(dog.name)
print(dog.species)  
print(cat.name)



    

