# Instructions
# Implement receipt_formatter(name, quantity, price). 
# Calculate subtotal as quantity multiplied by price. Calculate tax as 7.5 percent of subtotal. Calculate total as subtotal plus tax. Return a four-line 
# report with labels Customer, Subtotal, Tax, and Total. Round subtotal, tax, and total to 2 decimal places.

def receipt_formatter(name, quantity, price):
    quantity = float(quantity)
    price = float(price)
    subtotal = quantity*price 
    tax= round(subtotal*0.075,2)
    total = round(subtotal + tax, 2)
    subtotal = round(subtotal, 2)
    return(f"Customer: {name}\nSubtotal: {subtotal}\nTax: {tax}\nTotal: {total}")

print(receipt_formatter("Olamide", 2, 100))
print(receipt_formatter("Tunde", 3, 25.5))