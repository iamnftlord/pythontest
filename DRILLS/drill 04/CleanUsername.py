# Instructions
# Implement clean_username(value). The function should remove leading and trailing spaces, 
# convert the text to lowercase, and replace every space with an underscore. Return the cleaned username.

def clean_username(value):
    username = value.strip()
    username = username.replace(" ", "_")

    return username.lower()

print(clean_username("Olami  oladele"))
    

