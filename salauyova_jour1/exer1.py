def word_inverse(word):
    inversed = " "
    for caracter in word: 
        inversed = caracter+inversed
    return inversed
word = "Bonjour"
print(word_inverse(word))