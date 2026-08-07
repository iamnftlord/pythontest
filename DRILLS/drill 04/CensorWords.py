# Implement censor_words(text, banned_word). Return a new string where every occurrence of banned_word is replaced with "***". 
# The match is case-sensitive. Do not use import or regular expressions.

# def censor_words(text, banned_word):
#    censored_text = []

#    words = text.split()

# #    for word in words:
# #       if word == banned_word:
# #         censored_text.append("***")
# #       else:
# #         censored_text.append(word)

#    return " ".join(censored_text)
      

# print(censor_words("The boy went out to work on holiday.", "boy"))

def censor_words(text, banned_word):
    censor_text = text.replace(banned_word, "***")
    return censor_text

print(censor_words("The boy is good", "boy"))






