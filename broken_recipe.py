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



# class Cup:
#     pass
# my_cup = Cup()
# print(my_cup)






# class Cup:
#     def __init__(self, color):
#         self.color = color

# blue_cup = Cup("blue")
# print(blue_cup.color)


# class Cup:
#     def __init__(self,):
#         self.contents = "empty"

# my_cup = Cup()
# my_cup.contents = "Mocha"
# print(my_cup.contents)

# class pet:
#     def __init__(self, name, species):
#         self.name = name 
#         self.species = species

# dog = pet("Rex", "Dog")
# cat = pet("Mittens", "Cat")
# print(dog.name)
# print(dog.species)  
# print(cat.name)

# def my_generator():
#     yield 1
#     yield 2
#     yield 3

# for value in my_generator():
#     print(value)


# def count_up_to(n):
#     count = 1
#     while count <= n:
#         yield count 
#         count += 1

# for num in count_up_to(5):
#     print(num)

# def large_sequence(n):
#    for i in range(n):
#     yield i

# gen = large_sequence(1000000)
# print(next(gen))
# print(next(gen))
# print(next(gen))


import sys

# def get_orders_generator(n):
#     for i in range(n):
#         yield f"Order #{i}"

# massive_gen = get_orders_generator(1000000)
# print(f"Memory size: {sys.getsizeof(massive_gen)} bytes")
# next(get_orders_generator(10000))

# list_comp = [x*x for x in range(100000)]
# gen_expr = [x*x for x in range(100000)]
# print("List Comp Size:", sys.getsizeof(list_comp), "bytes")
# print("Gen expr Size:", sys.getsizeof(gen_expr), "bytes")


# def hello():
#     print("Hello!")

# print(type(hello))
# print(hasattr(hello, '_name_'))

# funcs = [hello, lambda: print("Hi!")]
# for f in funcs:
#     f()

# Try opening a file
# with open('test.txt', 'w') as f:
#     f.write('Hello, Coffee!')

# # Read it back
# with open('test.txt', 'r') as f:
#     print(f.read())  # Hello, Coffee!

# # Try suppressing an error
# from contextlib import suppress

# with suppress(FileNotFoundError):
#     with open('does_not_exist.txt') as f:
#         print(f.read())
#     print("This won't print, but no error!")


import time

class CoffeeMachine:
    def __init__(self, coffee_type):
        self.coffee_type = coffee_type
        print(f"⏳ Preparing {coffee_type} machine...")
    
    def __enter__(self):
        print(f"✅ {self.coffee_type} machine ready!")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"🧹 Cleaning {self.coffee_type} machine...")
        if exc_type:
            print(f"⚠️ Error occurred: {exc_val}")
        print("✅ Machine cleaned!")
        # Returning False re-raises exceptions, True suppresses them
        return False
    
    def make_coffee(self):
        print(f"☕ Making {self.coffee_type}...")
        time.sleep(0.5)
        return f"Here's your {self.coffee_type}!"

# Usage
with CoffeeMachine("Latte") as machine:
    result = machine.make_coffee()
    print(result)