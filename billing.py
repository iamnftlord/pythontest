# This module handles transaction pricing

def calculate_subtotal(price, quantity):
    """Return the base cost of the items"""
    return price * quantity

def apply_discount(total, discount_rate):
    """Return the total after applying a percentage discount"""
    return total * (1.0 - discount_rate)

def format_receipt(customer_name, final_amount):
    """Return a formatted string receipt"""
    return f"Receipt for {customer_name}: ₦{final_amount:.2f}"