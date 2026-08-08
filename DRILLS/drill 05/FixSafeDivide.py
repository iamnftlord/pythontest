# Instructions
# Implement safe_divide(a, b). Return a divided by b rounded to 2 decimal places. 
# If b is zero, return Cannot divide by zero. This fixes the common ZeroDivisionError bug.

def safe_divide(a, b):
    if b == 0:
        return "Cannot divide by zero"

    total = a / b
    return round(total, 2)


print(safe_divide(2, 0))
print(safe_divide(10, 3))
   
    