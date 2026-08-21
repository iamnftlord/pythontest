def calculate_subtotal(price, quantity):
    if price < 0 or quantity < 0:
        raise ValueError("Input values cannot be negative")
    return price * quantity

def apply_discount(total, discount_rate):
    return total * (1.0 - discount_rate)
    