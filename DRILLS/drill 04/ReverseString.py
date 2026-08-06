# Instructions
# Implement reverse_string(value) without using slicing shorthand like [::-1]. Return a new string containing the input characters in reverse order.

def reverse_string(value):
    reversed_string = ""
    for char in value:
        reversed_string = char + reversed_string
    return reversed_string

print(reverse_string("tolu"))