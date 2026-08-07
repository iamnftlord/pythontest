# Instructions
# Implement next_age(age_text). The function receives age as text. Convert it to an integer and return the age next year. 
# This fixes the common bug where text is used like a number.

def next_age(age_text):
   age_text = int(age_text, 10)

   return age_text + 1

print(next_age("9"))