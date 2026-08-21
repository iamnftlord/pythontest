# Instructions
# Implement manual_palindrome(text). Ignore spaces and letter case. 
# Return true if the cleaned text reads the same forward and backward, otherwise return false. 
# Do not use slicing shorthand or reversed. Students may need to research manual string reversal.

def manual_palindrome(text):
    text = text.replace(" ", "").lower()
    reversed_text = ""  

    for char in text:
        reversed_text = char + reversed_text

    return text == reversed_text

print(manual_palindrome("level"))


