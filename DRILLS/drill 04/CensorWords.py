# Implement censor_words(text, banned_word). Return a new string where every occurrence of banned_word is replaced with "***". 
# The match is case-sensitive. Do not use import or regular expressions.

def censor_words(text, banned_word):
    # Initialize an empty string to store the censored text
    censored_text = ""
    
    # Split the text into words
    words = text.split()
    
    # Iterate through each word in the list
    for word in words:
        # Check if the current word matches the banned word
        if word == banned_word:
            # If it matches, append "***" to the censored text
            censored_text += "*** "
        else:
            # If it doesn't match, append the original word to the censored text
            censored_text += word + " "
    
    # Remove the trailing space and return the censored text
    return censored_text.strip()
