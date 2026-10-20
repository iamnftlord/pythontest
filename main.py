# main.py
# This file imports and uses the billing module

import billing

# Use the functions by prefixing them with the module name
base_cost = billing.calculate_subtotal(4.50, 3)
final_price = billing.apply_discount(base_cost, 0.10) # 10% discount

receipt = billing.format_receipt("Alice", final_price)
print(receipt)