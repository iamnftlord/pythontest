# Instructions
# Implement get_item(items, index). Return the item at the given index. 
# If the index is outside the list, return Index out of range. Negative indexes should also return Index out of range for this challenge.

def get_item(items, index):
    # Bug to fix: invalid indexes should not crash the program.
    if index < 0 or index >= len(items):
        return "Index out of range"

    else:
        return items[index] 

print(get_item(["ola", "yosin", "ogo"], 2)) 