# Instructions
# Implement error_hint(error_type). Return a helpful debugging hint for common Python errors. 
# For NameError return Check variable names and spelling. For TypeError return Check the types before using an 
# operator. For ValueError return Check whether the value can be converted. 
# For ZeroDivisionError return Check that the denominator is not zero. 
# For IndexError return Check the index is inside the valid range. 
# For anything else return Read the traceback carefully.

def error_hint(error_type):
    error_hints = {
        "NameError": "Check variable names and spelling.",
        "TypeError": "Check the types before using an operator.",
        "ValueError": "Check whether the value can be converted.",
        "ZeroDivisionError": "Check that the denominator is not zero.",
        "IndexError": "Check the index is inside the valid range."
    }

    return error_hints.get(error_type, "Read the traceback carefully.")

print(error_hint("NameError"))
print(error_hint("TypeError"))
print(error_hint("ValueError"))
print(error_hint("ZeroDivisionError"))
print(error_hint("IndexError"))
print(error_hint("RuntimeError"))
