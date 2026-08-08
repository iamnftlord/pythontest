# Implement censor_words(text, banned_word). Return a new string where every occurrence of banned_word is replaced with "***". 
# The match is case-sensitive. Do not use import or regular expressions.

def censor_words(text, banned_word):
    censored_text = ""
    
    words = text.split()
    
    for word in words:
        if word == banned_word:
            censored_text += "*** "
        else:
            censored_text += word + " "
    
    return censored_text.strip()
