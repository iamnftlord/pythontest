# Instructions
# Implement exact_calculator(left, operator, right). Convert left and right to numbers. 
# Support addition, subtraction, multiplication, division, remainder, and exponent. 
# If either number cannot be converted, return Invalid number. If the operator is not supported, return Invalid operator. 
# If division or remainder uses zero on the right side, return Cannot divide by zero. Round numeric results to 2 decimal places

def exact_calculator(left, operator, right):
    try:
        left_num = float(left)
        right_num = float(right)
    except ValueError:
        return "Invalid number"

    if operator == "+":
        result = left_num + right_num
    elif operator == "-":
        result = left_num - right_num
    elif operator == "*":
        result = left_num * right_num
    elif operator == "/":
        if right_num == 0:
            return "Cannot divide by zero"
        result = left_num / right_num
    elif operator == "%":
        if right_num == 0:
            return "Cannot divide by zero"
        result = left_num % right_num
    elif operator == "**":
        result = left_num ** right_num
    else:
        return "Invalid operator"

    return round(result, 2)
